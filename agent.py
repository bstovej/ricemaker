import os, json, time, wave, logging
import queue, threading
import litellm
from pathlib import Path
from markitdown import MarkItDown
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler

# Setup logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(message)s',
                    handlers=[logging.FileHandler('agent.log'), logging.StreamHandler()])

class RicemakerAgent:
    def __init__(self):
        self.config = self.load_json('config.json')
        self.keys = self.load_json('keys.json')
        
        self.file_queue = queue.PriorityQueue()

        # Session Stats
        self.session_start = time.time()
        self.session_processed = 0
        self.session_tokens = {"prompt": 0, "completion": 0}
        self.active_model = self.config.get('model_name', 'ollama/gemma4:26b')
        self._update_session_file()
        
        # Point to Host Ollama from inside Docker
        self.ollama_base = self.keys.get("OLLAMA_API_BASE", "http://host.docker.internal:11434")
        
        # litellm configuration for Ollama
        os.environ["OLLAMA_API_BASE"] = self.ollama_base
        
    def load_json(self, path):
        return json.loads(Path(path).read_text()) if Path(path).exists() else {}

    def _update_session_file(self):
        """Saves current session metrics to session_stats.json for the UI to read"""
        stats = {
            "session_start": self.session_start,
            "processed": self.session_processed,
            "tokens": self.session_tokens,
            "active_model": self.active_model,
            "last_active": time.time()
        }
        Path('session_stats.json').write_text(json.dumps(stats, indent=2))

    def _call_llm(self, system_prompt, user_content):
        """Internal helper to route LLM calls with retry-and-fallback logic"""
        primary = self.config.get('model_name')
        secondary = self.config.get('secondary_model_name')
        
        # Reset to primary for each call (as requested, or we can keep the state if preferred)
        # However, the user asked to "go back to try to use the primary model again" 
        # for each file. I'll handle that reset in process_file.
        
        models_to_try = [primary] * 3
        if secondary:
            models_to_try.append(secondary)
            
        last_error = None
        for attempt, model_name in enumerate(models_to_try):
            self.active_model = model_name
            self._update_session_file()
            
            # LiteLLM uses 'ollama/model' syntax for Ollama
            curr_model = model_name
            if curr_model.startswith("ollama:"):
                curr_model = curr_model.replace("ollama:", "ollama/")
                
            try:
                logging.info(f"Attempt {attempt+1}: Calling {curr_model}...")
                response = litellm.completion(
                    model=curr_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content}
                    ],
                    api_base=self.ollama_base if "ollama" in curr_model else None,
                    num_ctx=8192 if "ollama" in curr_model else None,
                    timeout=300
                )
                
                # Track Tokens (Session Only)
                usage = response.usage
                self.session_tokens["prompt"] += usage.prompt_tokens
                self.session_tokens["completion"] += usage.completion_tokens
                self._update_session_file()
                
                return response.choices[0].message.content
            except Exception as e:
                last_error = e
                logging.warning(f"Attempt {attempt+1} failed for {curr_model}: {e}")
                time.sleep(2) # Brief pause before retry
        
        raise last_error

    def load_history(self):
        """Loads the completion history to check for skips"""
        history_path = Path('history.csv')
        if not history_path.exists():
            return set()
        
        import pandas as pd
        try:
            df = pd.read_csv(history_path)
            # We skip if the original path exists in the history and status is 'completed'
            return set(df[df['status'] == 'completed']['original_path'].tolist())
        except Exception:
            return set()

    def log_history(self, original_path, summary_path, status, model_used=None):
        """Writes a detailed audit log to history.csv"""
        history_path = Path('history.csv')
        file_exists = history_path.exists()
        
        import pandas as pd
        from datetime import datetime
        
        new_entry = {
            "completion_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "model_used": model_used or self.active_model,
            "original_path": str(Path(original_path).absolute()),
            "summary_path": str(Path(summary_path).absolute()),
            "status": status
        }
        
        df = pd.DataFrame([new_entry])
        df.to_csv(history_path, mode='a', index=False, header=not file_exists)

    def log_stats(self, filename, file_type, model, prompt_tokens, completion_tokens, extraction_time, inference_time):
        """Writes detailed performance and token metrics to stats.csv"""
        stats_path = Path('stats.csv')
        file_exists = stats_path.exists()
        
        import pandas as pd
        from datetime import datetime
        
        total_tokens = prompt_tokens + completion_tokens
        total_time = extraction_time + inference_time
        
        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "filename": filename,
            "file_type": file_type,
            "model_used": model,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "extraction_time": round(extraction_time, 2),
            "inference_time": round(inference_time, 2),
            "total_time": round(total_time, 2)
        }
        
        df = pd.DataFrame([new_entry])
        df.to_csv(stats_path, mode='a', index=False, header=not file_exists)

    def process_file(self, file_path):
        """Logic to extract content and call LLM with recursive chunking"""
        file_path = Path(file_path)
        if file_path.name.startswith('.'): return
        
        # Reset to primary model for each new file
        self.active_model = self.config.get('model_name')
        self._update_session_file()
        
        if not file_path.exists():
            logging.error(f"File {file_path} not found. Marking as missing.")
            self.update_state(file_path.name, "error (missing)")
            return

        # --- NEW: Check History for Skips ---
        completed_paths = self.load_history()
        if str(file_path.absolute()) in completed_paths:
            logging.info(f"Skipping {file_path.name} (already found in history.csv)")
            # Update plan.json so UI doesn't think it's pending. Set timestamp=0 so it defaults to Archive view
            self.update_state(file_path.name, "completed", timestamp=0)
            return

        logging.info(f"Processing: {file_path.name}")
        
        # Also check plan.json for session-level status
        plan = self.load_json('plan.json')
        f_plan_status = plan.get('files', {}).get(file_path.name, {}).get('status', '')
        if f_plan_status in ('completed', 'archived') or f_plan_status.startswith('error'):
            logging.info(f"Skipping {file_path.name} (already processed with status {f_plan_status})")
            return

        # 1. Extraction
        self.update_state(file_path.name, "Processing (Extracting Text)")
        start_time = time.time()
        md = MarkItDown()
        try:
            content = md.convert(str(file_path)).text_content
            extraction_time = time.time() - start_time
            
            # 2. Memory-efficient Chunking
            content = content.replace('\x00', '') # Sanitize null bytes
            if not content.strip():
                raise ValueError("Extraction returned empty content. Unsupported or image-based file without OCR.")
                
            MAX_CHARS = 24000 
            num_chunks = (len(content) + MAX_CHARS - 1) // MAX_CHARS
            
            chunk_reviews = []
            file_prompt_tokens = 0
            file_completion_tokens = 0
            inference_start = time.time()
            
            for idx in range(num_chunks):
                start_pos = idx * MAX_CHARS
                chunk = content[start_pos : start_pos + MAX_CHARS]
                
                chunk_name = f"{file_path.name}_chunk_{idx+1}.md"
                chunk_path = Path(self.config['intermediate_folder']) / chunk_name
                
                # Check if chunk already exists (Resume logic)
                if chunk_path.exists():
                    logging.info(f"Loading cached chunk {idx+1}/{num_chunks} for {file_path.name}...")
                    chunk_reviews.append(chunk_path.read_text(encoding='utf-8'))
                    continue

                progress = f"Processing ({idx+1}/{num_chunks})"
                self.update_state(file_path.name, progress)
                
                if num_chunks > 1:
                    logging.info(f"Processing chunk {idx+1}/{num_chunks} for {file_path.name}...")
                
                pre_p = self.session_tokens["prompt"]
                pre_c = self.session_tokens["completion"]
                
                result = self._call_llm("Review this document segment. Provide key insights and facts.", chunk)
                
                chunk_reviews.append(result)
                file_prompt_tokens += (self.session_tokens["prompt"] - pre_p)
                file_completion_tokens += (self.session_tokens["completion"] - pre_c)
                
                # Save raw chunks to intermediate/
                chunk_path.write_text(result, encoding='utf-8')
                
                # Memory cleanup: don't hold the raw chunk once processed if we don't need it
                del chunk

            # Done with raw content, free it before consolidation
            del content

            # 3. Hierarchical Consolidation (Reduce Phase)
            # If we have many chunks, we consolidate them in batches to avoid context window limits (8192)
            MAX_CONSOLIDATION_BATCH = 10
            
            while len(chunk_reviews) > 1:
                logging.info(f"Consolidating {len(chunk_reviews)} segments for {file_path.name}...")
                
                # If we have too many reviews, we group them
                new_reviews = []
                for i in range(0, len(chunk_reviews), MAX_CONSOLIDATION_BATCH):
                    batch = chunk_reviews[i : i + MAX_CONSOLIDATION_BATCH]
                    if len(batch) == 1 and len(chunk_reviews) > MAX_CONSOLIDATION_BATCH:
                        new_reviews.append(batch[0])
                        continue
                        
                    batch_text = "\n\n---\n\n".join(batch)
                    
                    pre_p = self.session_tokens["prompt"]
                    pre_c = self.session_tokens["completion"]
                    
                    logging.info(f"Consolidating batch {i//MAX_CONSOLIDATION_BATCH + 1} of {len(chunk_reviews)//MAX_CONSOLIDATION_BATCH + 1}...")
                    
                    # Update UI Status
                    progress = f"Consolidating ({i//MAX_CONSOLIDATION_BATCH + 1}/{ (len(chunk_reviews) + MAX_CONSOLIDATION_BATCH - 1) // MAX_CONSOLIDATION_BATCH })"
                    self.update_state(file_path.name, progress)
                    
                    batch_summary = self._call_llm(
                        "You are a subject matter expert. Consolidate these segment reviews into a single, cohesive executive summary with clear headings.",
                        f"Segment Reviews:\n{batch_text}"
                    )
                    
                    new_reviews.append(batch_summary)
                    file_prompt_tokens += (self.session_tokens["prompt"] - pre_p)
                    file_completion_tokens += (self.session_tokens["completion"] - pre_c)
                
                chunk_reviews = new_reviews
                if len(chunk_reviews) == 1:
                    break

            final_result = chunk_reviews[0]
            
            # 3.5 Generate Content-Aware Tags
            logging.info(f"Generating categorization tags for {file_path.name}...")
            tag_resp = self._call_llm(
                "You are a metadata specialist. Based on the summary provided, generate 3-5 highly relevant Obsidian tags in 'domain/subject' format (e.g. 'science/physics', 'tech/ai'). Return ONLY a comma-separated list of tags without '#' symbols.",
                f"Document Summary:\n{final_result[:5000]}"
            )
            # Basic cleanup of LLM response
            tags = [t.strip().replace('#', '').lower() for t in tag_resp.split(',')]
            if not tags: tags = ["ai/research"]

            # 3.6 Generate MOC Blurb (Concise summary for Master Report)
            logging.info(f"Generating MOC blurb for {file_path.name}...")
            moc_blurb = self._call_llm(
                "You are a librarian creating a Map of Content (MOC). Summarize the key essence of this document in 150 words or less. Focus on its core value and main findings. Return ONLY the summary text.",
                f"Full Review:\n{final_result[:8000]}"
            )

            inference_time = time.time() - inference_start
            
            # 4. Update Plan & Stats
            summary_path = Path(self.config['output_folder']) / f"{file_path.name}.md"
            self.update_state(file_path.name, "completed", final_result, tags=tags, moc_blurb=moc_blurb)
            
            # Log to history
            self.log_history(file_path, summary_path, "completed", model_used=self.active_model)
            
            # --- NEW: Log detailed performance stats ---
            self.log_stats(
                filename=file_path.name,
                file_type=file_path.suffix.lower(),
                model=self.active_model,
                prompt_tokens=file_prompt_tokens,
                completion_tokens=file_completion_tokens,
                extraction_time=extraction_time,
                inference_time=inference_time
            )
            
            # --- Increment Session Stats ---
            self.session_processed += 1
            self._update_session_file()
            logging.info(f"Successfully processed {file_path.name}")
            
            # 5. Generate Global Master Summary
            self.generate_master_report()
            
        except Exception as e:
            logging.error(f"Error processing {file_path.name}: {e}")
            self.update_state(file_path.name, "error", error_msg=str(e))
            self.log_history(file_path, "N/A", "error", model_used=self.active_model)
            # Log failure stats if possible (with 0 tokens)
            self.log_stats(file_path.name, file_path.suffix.lower(), self.active_model, 0, 0, 0, 0)

    def _generate_master_frontmatter(self, title, session_files_count):
        """Generates YAML frontmatter for the master report based on tp resource note.md"""
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        frontmatter = [
            "---",
            f"created: {now}",
            f"modified: {now}",
            f"title: \"{title}\"",
            "source: Ricemaker Session",
            "category: Resources",
            "tags: [ai/summary, session/master]",
            "cssclasses:",
            "  - whiteRed-rounded",
            "classification: local",
            f"summary: \"Consolidated executive summary of {session_files_count} documents reviewed during this session.\"",
            "related:",
            "  - [[]]",
            "---",
            ""
        ]
        return "\n".join(frontmatter)

    def generate_master_report(self):
        """Consolidates session reports into an MOC-style summary with metadata and concise blurbs"""
        from datetime import datetime
        now_dt = datetime.now()
        now_str = now_dt.strftime("%Y%m%d_%H%M")
        output_dir = Path(self.config['output_folder'])
        
        plan = self.load_json('plan.json')
        # Only files from current session (post session_start) that are completed
        session_files = [name for name, info in plan.get('files', {}).items() 
                         if info['status'] == 'completed' and info['timestamp'] >= self.session_start]
        
        if not session_files:
            return

        reports = []
        for filename in session_files:
            info = plan['files'][filename]
            report_name = f"{filename}.md"
            moc_blurb = info.get('moc_blurb', "No blurb available.")
            
            # Format as MOC Entry
            entry = f"### [[{report_name}|{filename}]]\n"
            entry += f"- **Original File:** `{filename}`\n"
            entry += f"- **Model Used:** `{info.get('model', 'N/A')}`\n"
            entry += f"- **Review Date:** {datetime.fromtimestamp(info['timestamp']).strftime('%Y-%m-%d %H:%M')}\n"
            entry += f"\n**MOC Summary:** {moc_blurb}\n"
            
            reports.append(entry)
        
        if reports:
            master_filename = f"master_report_{now_str}.md"
            title = f"Ricemaker Session MOC - {now_dt.strftime('%Y-%m-%d %H:%M')}"
            
            frontmatter = self._generate_master_frontmatter(title, len(reports))
            
            master_content = frontmatter
            master_content += f"# {title}\n\n"
            master_content += f"**Session Timestamp:** {now_dt.strftime('%Y-%m-%d %H:%M:%S')}\n"
            master_content += f"**Documents Reviewed in this Session:** {len(reports)}\n\n"
            master_content += "---"
            master_content += "\n\n" + "\n\n---\n\n".join(reports)
            
            (output_dir / master_filename).write_text(master_content, encoding='utf-8')
            logging.info(f"Generated MOC master report: {master_filename}")

    def _generate_frontmatter(self, filename, summary_text, tags=None):
        """Generates YAML frontmatter based on the user's Obsidian template"""
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Use provided tags or default
        if not tags:
            tags = ["ai/research"]
            
        primary_category = tags[0].split('/')[0] if tags and '/' in tags[0] else tags[0]
        
        # Clean up summary for the frontmatter (single line, escaped quotes)
        clean_summary = summary_text.split('\n')[0].replace('"', '\\"').strip()
        if len(clean_summary) > 150:
            clean_summary = clean_summary[:147] + "..."

        frontmatter = [
            "---",
            f'source: "{filename}"',
            f"created: {now}",
            f"modified: {now}",
            "classification: local",
            f'summary: "{clean_summary}"',
            f'category: "{primary_category}"',
            "status: completed",
            "reviewed: false",
            f"last_reviewed: {now}",
            f"tags: [{', '.join(tags)}]",
            "related: []",
            "---",
            ""
        ]
        return "\n".join(frontmatter)

    def update_state(self, filename, status, result=None, tags=None, moc_blurb=None, error_msg=None, timestamp=None):
        plan = self.load_json('plan.json')
        if 'files' not in plan:
            plan['files'] = {}
        plan['files'][filename] = {
            "status": status, 
            "timestamp": timestamp if timestamp is not None else time.time(),
            "model": self.active_model,
            "moc_blurb": moc_blurb,
            "error_msg": error_msg
        }
        Path('plan.json').write_text(json.dumps(plan, indent=2))
        
        if result:
            # --- FIXED: Final reports go to output/ with Frontmatter ---
            os.makedirs(self.config['output_folder'], exist_ok=True)
            frontmatter = self._generate_frontmatter(filename, result, tags=tags)
            (Path(self.config['output_folder']) / f"{filename}.md").write_text(frontmatter + result, encoding='utf-8')

    def queue_file(self, file_path):
        """Adds a file to the priority queue based on modification time."""
        file_path = Path(file_path)
        if file_path.name.startswith('.'): return
        
        try:
            mtime = file_path.stat().st_mtime
            priority = -mtime
            
            # Adjust priority based on current file status
            plan = self.load_json('plan.json')
            f_status = plan.get('files', {}).get(file_path.name, {}).get('status', '')
            if f_status == 'pending':
                # Strong boost: negative number makes it highest priority
                priority -= 1000000000
            elif f_status.startswith('error'):
                # Strong penalty: positive number makes it lowest priority
                priority += 1000000000
                
            self.file_queue.put((priority, str(file_path.absolute())))
            logging.info(f"Queued {file_path.name}")
        except Exception as e:
            logging.error(f"Error queuing {file_path.name}: {e}")

    def run_worker(self):
        """Background thread to process files from the queue based on agent state."""
        logging.info("Agent worker thread started.")
        last_heartbeat = 0
        
        while True:
            # Heartbeat every 10 minutes
            if time.time() - last_heartbeat > 600:
                logging.info("Agent Heartbeat: Idle and waiting for files...")
                last_heartbeat = time.time()

            # Check agent state
            if Path('agent_state.json').exists():
                try:
                    state_data = self.load_json('agent_state.json')
                    agent_state = state_data.get('state', 'running').lower()
                except Exception:
                    agent_state = 'running'
            else:
                agent_state = 'running'
            
            if agent_state == 'stopped':
                logging.info("Agent state is STOPPED. Processing thread exiting...")
                break
                
            if agent_state == 'paused':
                time.sleep(2)
                continue
                
            # Running state: fetch next file
            try:
                # Use timeout so we can periodically check state
                priority, file_path_str = self.file_queue.get(timeout=2)
                
                # Check if file still exists before processing
                if not Path(file_path_str).exists():
                    logging.warning(f"File {file_path_str} disappeared before processing. Skipping.")
                    self.file_queue.task_done()
                    continue
                    
                self.process_file(Path(file_path_str))
                self.file_queue.task_done()
                
                # Reset heartbeat after processing to avoid immediate heartbeat after work
                last_heartbeat = time.time()
            except queue.Empty:
                pass
            except Exception as e:
                logging.error(f"Worker iteration error: {e}")
                time.sleep(1)

# Watcher Event Handler
class WatcherHandler(FileSystemEventHandler):
    def __init__(self, agent): self.agent = agent
    def on_created(self, event):
        if not event.is_directory: self.agent.queue_file(Path(event.src_path))
    def on_moved(self, event):
        if not event.is_directory: self.agent.queue_file(Path(event.dest_path))
    def on_modified(self, event):
        if not event.is_directory: self.agent.queue_file(Path(event.src_path))

if __name__ == "__main__":
    agent = RicemakerAgent()
    input_path = agent.config.get('input_folder', './input')
    
    # --- Connection Test ---
    logging.info(f"Testing connection to Ollama at {agent.ollama_base} (60s timeout)...")
    try:
        import requests
        resp = requests.get(f"{agent.ollama_base}/api/tags", timeout=60)
        if resp.status_code == 200:
            logging.info("Successfully connected to Ollama.")
            models = [m['name'] for m in resp.json().get('models', [])]
            logging.info(f"Available models: {models}")
            
            # Support both ollama:model and ollama/model syntax in config
            target_model = agent.config['model_name'].replace('ollama/', '').replace('ollama:', '')
            if target_model not in models:
                # Also check for tag-less match if user omitted :latest
                if f"{target_model}:latest" not in models and target_model.split(':')[0] not in [m.split(':')[0] for m in models]:
                    logging.warning(f"Model {agent.config['model_name']} not found in Ollama! Pull it using 'ollama pull {target_model}'")
        else:
            logging.error(f"Ollama returned status code {resp.status_code}")
    except Exception as e:
        logging.error(f"Failed to connect to Ollama: {e}")
    
    # Ensure directories exist
    # Only try to create if it's a relative path; for absolute paths (mounts), just check access
    if not os.path.isabs(input_path):
        os.makedirs(input_path, exist_ok=True)
    
    os.makedirs(agent.config.get('output_folder', './output'), exist_ok=True)
    os.makedirs(agent.config.get('intermediate_folder', './intermediate'), exist_ok=True)
    
    # --- Startup Scan ---
    # Use a more robust check for the input path
    is_accessible = False
    try:
        if os.path.isdir(input_path):
            is_accessible = True
    except PermissionError:
        # If we get a permission error on the dir itself, we might still be able to list it
        is_accessible = True 

    if is_accessible:
        logging.info(f"Performing startup scan of {input_path}...")
        try:
            for f in os.listdir(input_path):
                f_path = Path(input_path) / f
                try:
                    if f_path.is_file():
                        agent.queue_file(f_path)
                except (PermissionError, OSError) as e:
                    # Log but continue for other files
                    logging.error(f"Could not access {f_path}: {e}")
        except Exception as e:
            logging.error(f"Error during startup scan of {input_path}: {e}")
    else:
        logging.error(f"Input path {input_path} is not a directory or is inaccessible. Check your Docker volume mounts.")
    
    # Final check before starting observer
    if is_accessible:
        if not Path('agent_state.json').exists():
            Path('agent_state.json').write_text(json.dumps({"state": "running"}, indent=2))

        event_handler = WatcherHandler(agent)
        observer = Observer()
        observer.schedule(event_handler, input_path, recursive=False)
        
        logging.info(f"Ricemaker Agent started. Watching {input_path}...")
        observer.start()
        try:
            agent.run_worker()
        except KeyboardInterrupt:
            observer.stop()
        observer.stop()
        observer.join()
    else:
        logging.error(f"Cannot start watcher: {input_path} is missing.")

