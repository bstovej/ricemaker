import os, json, time, wave, logging, sys
import queue, threading
import litellm
from pathlib import Path

# Ensure config.json and keys.json are present and are files (prevent Docker from creating folders)
for filename, sample_name in [('config.json', 'sample_config.json'), ('keys.json', 'sample_keys.json')]:
    path = Path(filename)
    if not path.exists():
        print(f"CRITICAL ERROR: {filename} is missing! Please create it by copying the reference {sample_name} file.", file=sys.stderr)
        sys.exit(1)
    if path.is_dir():
        print(f"CRITICAL ERROR: {filename} exists as a directory! Please remove it and create a proper JSON file referencing {sample_name}.", file=sys.stderr)
        sys.exit(1)

from markitdown import MarkItDown
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler

# Setup logging
DATA_DIR = Path('data')
DATA_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(message)s',
                    handlers=[logging.FileHandler(DATA_DIR / 'agent.log'), logging.StreamHandler()])

class RicemakerAgent:
    def __init__(self):
        self.config = self.load_json('config.json')
        self.keys = self.load_json('keys.json')
        self.prompts = self.load_json(self.config.get('prompts_file', 'prompts.json'))
        
        self.file_queue = queue.PriorityQueue()
        self.queued_files = set()

        # Session Stats
        self.session_start = time.time()
        self.session_id_str = time.strftime("%Y%m%d_%H%M", time.localtime(self.session_start))
        self.session_processed = 0
        self.session_tokens = {"prompt": 0, "completion": 0}
        self.active_model = self.config.get('model_name', 'openai/local-model')
        self._update_session_file()
        
        # Point to llama.cpp/Ollama from inside Docker
        self.llama_cpp_base = self.keys.get("LLAMA_CPP_API_BASE", "http://host.docker.internal:8080/v1")
        self.ollama_base = self.keys.get("OLLAMA_API_BASE", "http://host.docker.internal:11434")
        
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
        (DATA_DIR / 'session_stats.json').write_text(json.dumps(stats, indent=2))

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
            
            curr_model = model_name
                
            try:
                logging.info(f"Attempt {attempt+1}: Calling {curr_model}...")
                
                llm_provider = self.config.get('llm_provider', 'llama_cpp').lower()
                api_base = None
                litellm_model = curr_model
                
                # Check if it's a cloud provider (e.g. google/gemini, anthropic/claude, openai/gpt)
                is_cloud = curr_model.startswith(("google/", "gemini/", "anthropic/", "claude/")) or \
                           (curr_model.startswith("openai/") and not curr_model.startswith("openai/local"))
                
                if not is_cloud:
                    if llm_provider == 'ollama':
                        if not litellm_model.startswith('ollama/'):
                            litellm_model = f"ollama/{litellm_model}"
                        api_base = self.ollama_base
                    elif llm_provider == 'llama_cpp':
                        if not litellm_model.startswith('openai/'):
                            litellm_model = f"openai/{litellm_model}"
                        api_base = self.llama_cpp_base
                else:
                    if curr_model.startswith("openai/"):
                        api_base = self.llama_cpp_base
                
                logging.info(f"Using LiteLLM model: {litellm_model} at api_base: {api_base}")
                
                response = litellm.completion(
                    model=litellm_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content}
                    ],
                    api_base=api_base,
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
        history_path = DATA_DIR / 'history.csv'
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
        history_path = DATA_DIR / 'history.csv'
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
        stats_path = DATA_DIR / 'stats.csv'
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

    def log_error(self, filename, file_type, model, error_message, traceback_str=None):
        """Logs structured processing errors to the configured error log file path"""
        try:
            import pandas as pd
            # Resolve error log file path
            configured_path = self.config.get('error_log_file')
            if configured_path and configured_path.strip():
                error_log_path = Path(configured_path.strip())
            else:
                # Default to output folder
                output_dir = Path(self.config.get('output_folder', './output'))
                error_log_path = output_dir / 'error_log.csv'
                
            # Ensure the parent directory exists
            error_log_path.parent.mkdir(parents=True, exist_ok=True)
            file_exists = error_log_path.exists()
            
            new_entry = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "filename": filename,
                "file_type": file_type,
                "model": model,
                "error_message": error_message,
                "traceback": traceback_str or ""
            }
            
            df = pd.DataFrame([new_entry])
            df.to_csv(error_log_path, mode='a', index=False, header=not file_exists)
            logging.info(f"Logged error for {filename} to {error_log_path}")
        except Exception as ex:
            logging.error(f"Failed to log error to csv: {ex}")

    def ocr_extract(self, file_path):
        """Attempts OCR on images or PDF pages using easyocr and fitz (PyMuPDF)"""
        file_path = Path(file_path)
        ext = file_path.suffix.lower()
        
        # Load easyocr
        try:
            import easyocr
            reader = easyocr.Reader(['en'])
        except Exception as e:
            logging.error(f"Cannot initialize easyocr: {e}")
            raise Exception("OCR engine (easyocr) not available.")
            
        text_content = []
        
        if ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'):
            logging.info(f"Performing OCR on image: {file_path.name}")
            try:
                result = reader.readtext(str(file_path.absolute()), detail=0)
                text = " ".join(result)
                if text.strip():
                    return text
                raise Exception("No text detected in image.")
            except Exception as e:
                logging.error(f"Image OCR failed for {file_path.name}: {e}")
                raise e
                
        elif ext == '.pdf':
            logging.info(f"Performing OCR fallback on PDF pages for: {file_path.name}")
            try:
                import fitz  # PyMuPDF
                doc = fitz.open(str(file_path.absolute()))
                
                # Limit to first 30 pages to avoid performance / timeout issues
                max_pages = min(len(doc), 30)
                for page_num in range(max_pages):
                    logging.info(f"OCRing page {page_num + 1}/{max_pages} for {file_path.name}...")
                    page = doc.load_page(page_num)
                    pix = page.get_pixmap(dpi=150) # Use reasonable resolution
                    
                    # Convert to bytes and run OCR
                    img_bytes = pix.tobytes("png")
                    result = reader.readtext(img_bytes, detail=0)
                    page_text = " ".join(result)
                    
                    if page_text.strip():
                        text_content.append(f"--- Page {page_num + 1} ---\n{page_text}")
                
                if text_content:
                    return "\n\n".join(text_content)
                raise Exception("No text detected in PDF via OCR.")
            except Exception as e:
                logging.error(f"PDF OCR failed for {file_path.name}: {e}")
                raise e
        else:
            raise Exception(f"Unsupported file type for OCR: {ext}")

    def convert_legacy_office(self, file_path, target_ext):
        """Converts legacy office formats (.doc, .ppt, .xls) to modern formats (.docx, .pptx, .xlsx) using LibreOffice soffice"""
        import shutil, subprocess
        file_path = Path(file_path)
        out_dir = Path("/tmp")
        out_dir.mkdir(parents=True, exist_ok=True)
        
        soffice_bin = "soffice"
        if os.name == "posix" and not shutil.which(soffice_bin):
            mac_soffice = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
            if Path(mac_soffice).exists():
                soffice_bin = mac_soffice
                
        if not shutil.which(soffice_bin) and soffice_bin == "soffice":
            raise Exception("LibreOffice (soffice) command not found. Please install LibreOffice to process legacy office formats.")
            
        logging.info(f"Converting legacy office file {file_path.name} to {target_ext} using LibreOffice...")
        cmd = [
            soffice_bin,
            "--headless",
            "--convert-to",
            target_ext,
            "--outdir",
            str(out_dir.absolute()),
            str(file_path.absolute())
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            raise Exception(f"LibreOffice conversion failed: {result.stderr}")
            
        out_file = out_dir / f"{file_path.stem}.{target_ext}"
        if out_file.exists():
            return out_file
        raise Exception(f"Converted file {out_file.name} was not found after LibreOffice conversion.")

    def safe_extract(self, file_path):
        """Extracts text with fallbacks and size-based strategies to avoid OOM"""
        file_path = Path(file_path)
        ext = file_path.suffix.lower()
        
        # 1. Check if it's a legacy office file and convert it
        if ext in ('.doc', '.xls', '.ppt'):
            target_ext = 'docx' if ext == '.doc' else ('xlsx' if ext == '.xls' else 'pptx')
            try:
                converted_file = self.convert_legacy_office(file_path, target_ext)
                content = self.safe_extract(converted_file)
                if converted_file.exists():
                    os.remove(converted_file)
                return content
            except Exception as e:
                logging.error(f"Legacy office conversion failed for {file_path.name}: {e}")
                raise e
        
        # 2. Check if it's a direct image file
        if ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'):
            return self.ocr_extract(file_path)
            
        # 3. Strategy: For large PDFs, try a simpler extractor first to avoid MarkItDown's heavy dependencies
        if ext == '.pdf' and file_path.stat().st_size > 15 * 1024 * 1024:
            logging.info(f"Large PDF detected ({file_path.stat().st_size / 1024 / 1024:.1f} MB). Using lightweight extractor first.")
            try:
                from pdfminer.high_level import extract_text
                content = extract_text(str(file_path))
                if content and len(content.strip()) > 500: # Ensure we got a meaningful amount of text
                    logging.info(f"Successfully extracted {len(content)} chars from large PDF using pdfminer.")
                    return content
            except Exception as e:
                logging.warning(f"Lightweight extraction failed for {file_path.name}: {e}")

        # 4. Strategy: Fallback to MarkItDown
        try:
            md = MarkItDown()
            content = md.convert(str(file_path)).text_content
            # If PDF text is extremely short or empty, it's likely a scanned document (image-only)
            if ext == '.pdf' and (not content or len(content.strip()) < 100):
                logging.info(f"PDF content too short ({len(content.strip()) if content else 0} chars). Retrying with OCR...")
                return self.ocr_extract(file_path)
            return content
        except Exception as e:
            logging.warning(f"MarkItDown extraction failed for {file_path.name}: {e}")
            # If MarkItDown failed and it's a PDF, try OCR as a final fallback
            if ext == '.pdf':
                logging.info(f"MarkItDown failed on PDF. Retrying with OCR...")
                return self.ocr_extract(file_path)
            raise e

    def process_file(self, file_path):
        """Logic to extract content and call LLM with recursive chunking"""
        file_path = Path(file_path)
        if file_path.name.startswith('.'): return
        
        # Reset to primary model for each new file
        self.active_model = self.config.get('model_name')
        self._update_session_file()
        
        if not file_path.exists():
            logging.error(f"File {file_path} not found. Marking as missing.")
            self.update_state(file_path.name, "error (missing)", session_id=self.session_id_str)
            return

        # --- NEW: Check History for Skips ---
        completed_paths = self.load_history()
        
        # Only skip if found in history AND NOT marked as 'pending' in plan.json
        plan = self.load_json(DATA_DIR / 'plan.json')
        f_plan_status = plan.get('files', {}).get(file_path.name, {}).get('status', '')
        
        if str(file_path.absolute()) in completed_paths and f_plan_status != 'pending':
            logging.info(f"Skipping {file_path.name} (already found in history.csv and status is {f_plan_status})")
            # Update plan.json so UI doesn't think it's pending. Set timestamp=0 so it defaults to Archive view
            if f_plan_status == 'pending': # This should not happen now but for safety
                self.update_state(file_path.name, "completed", timestamp=0, session_id=self.session_id_str)
            return

        logging.info(f"Processing: {file_path.name}")
        
        if f_plan_status in ('completed', 'archived'):
            logging.info(f"Skipping {file_path.name} (already processed with status {f_plan_status})")
            return

        # 1. Extraction
        self.update_state(file_path.name, "Processing (Extracting Text)", session_id=self.session_id_str)
        start_time = time.time()
        
        try:
            content = self.safe_extract(file_path)
            extraction_time = time.time() - start_time
            
            # 2. Memory-efficient Chunking
            content = content.replace('\x00', '') # Sanitize null bytes
            if not content.strip():
                raise ValueError("Extraction returned empty content. Unsupported or image-based file without OCR.")
                
            # --- NEW: Large Document Handling ---
            # If document is extremely large, truncate it to focus on introductory sections
            # 120,000 characters (approx. 30,000 tokens) captures the Preface, Foreword, Introduction, Abstract, and TOC.
            LARGE_DOC_CHAR_LIMIT = 120000 
            is_large_document = len(content) > LARGE_DOC_CHAR_LIMIT
            
            if is_large_document:
                logging.info(f"Document is extremely large ({len(content)} chars). Truncating to first {LARGE_DOC_CHAR_LIMIT} chars to focus on Preface, Foreword, Introduction, Abstract, and TOC.")
                content = content[:LARGE_DOC_CHAR_LIMIT]
                
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
                self.update_state(file_path.name, progress, session_id=self.session_id_str)
                
                if num_chunks > 1:
                    logging.info(f"Processing chunk {idx+1}/{num_chunks} for {file_path.name}...")
                
                pre_p = self.session_tokens["prompt"]
                pre_c = self.session_tokens["completion"]
                
                result = self._call_llm(self.prompts.get("segment_review", "Review this document segment. Provide key insights and facts."), chunk)
                
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
                    self.update_state(file_path.name, progress, session_id=self.session_id_str)
                    
                    batch_summary = self._call_llm(
                        self.prompts.get("consolidation", "You are a subject matter expert. Consolidate these segment reviews into a single, cohesive executive summary with clear headings."),
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
                self.prompts.get("categorization", "You are a metadata specialist. Based on the summary provided, generate 3-5 highly relevant Obsidian tags in 'domain/subject' format (e.g. 'science/physics', 'tech/ai'). Return ONLY a comma-separated list of tags without '#' symbols."),
                f"Document Summary:\n{final_result[:5000]}"
            )
            # Basic cleanup of LLM response
            tags = [t.strip().replace('#', '').lower() for t in tag_resp.split(',')]
            if not tags: tags = ["ai/research"]

            # 3.6 Generate MOC Blurb (Concise summary for Master Report)
            logging.info(f"Generating MOC blurb for {file_path.name}...")
            moc_blurb = self._call_llm(
                self.prompts.get("moc_blurb", "You are a librarian creating a Map of Content (MOC). Summarize the key essence of this document in 150 words or less. Focus on its core value and main findings. Return ONLY the summary text."),
                f"Full Review:\n{final_result[:8000]}"
            )

            inference_time = time.time() - inference_start
            
            # 4. Update Plan & Stats
            summary_path = Path(self.config['output_folder']) / f"{file_path.name}.md"
            self.update_state(file_path.name, "completed", final_result, tags=tags, moc_blurb=moc_blurb, session_id=self.session_id_str)
            
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
            
            # Master report feature has been retired
            # self.generate_master_report()
            
        except Exception as e:
            import traceback
            tb_str = traceback.format_exc()
            logging.error(f"Error processing {file_path.name}: {e}")
            self.update_state(file_path.name, "error", error_msg=str(e), session_id=self.session_id_str)
            self.log_history(file_path, "N/A", "error", model_used=self.active_model)
            # Log failure stats if possible (with 0 tokens)
            self.log_stats(file_path.name, file_path.suffix.lower(), self.active_model, 0, 0, 0, 0)
            self.log_error(file_path.name, file_path.suffix.lower(), self.active_model, str(e), tb_str)

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
        output_dir = Path(self.config['output_folder'])
        
        plan = self.load_json(DATA_DIR / 'plan.json')
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
            master_filename = f"master_report_{self.session_id_str}.md"
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
            
        # Use category from config if available, otherwise fallback to tags
        config_category = self.config.get('category', 'Resources')
        primary_category = config_category
        
        # Clean up summary for the frontmatter (single line, escaped quotes, no newlines)
        clean_summary = summary_text.replace('\n', ' ').replace('\r', ' ').replace('"', '\\"').strip()
        while '  ' in clean_summary:
            clean_summary = clean_summary.replace('  ', ' ')
        if len(clean_summary) > 250:
            clean_summary = clean_summary[:247] + "..."

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

    def update_state(self, filename, status, result=None, tags=None, moc_blurb=None, error_msg=None, timestamp=None, session_id=None):
        plan = self.load_json(DATA_DIR / 'plan.json')
        if 'files' not in plan:
            plan['files'] = {}
        plan['files'][filename] = {
            "status": status, 
            "timestamp": timestamp if timestamp is not None else time.time(),
            "model": self.active_model,
            "tags": tags,
            "moc_blurb": moc_blurb,
            "error_msg": error_msg,
            "session_id": session_id or plan.get('files', {}).get(filename, {}).get('session_id')
        }
        (DATA_DIR / 'plan.json').write_text(json.dumps(plan, indent=2))
        
        if result:
            # --- FIXED: Final reports go to output/ with Frontmatter ---
            os.makedirs(self.config['output_folder'], exist_ok=True)
            # Use moc_blurb if provided as the YAML summary
            summary_text = moc_blurb if moc_blurb else result
            frontmatter = self._generate_frontmatter(filename, summary_text, tags=tags)
            (Path(self.config['output_folder']) / f"{filename}.md").write_text(frontmatter + result, encoding='utf-8')

    def queue_file(self, file_path):
        """Adds a file to the priority queue based on modification time."""
        file_path = Path(file_path)
        if file_path.name.startswith('.'): return
        
        file_abs = str(file_path.absolute())
        if file_abs in self.queued_files:
            return
            
        try:
            mtime = file_path.stat().st_mtime
            priority = -mtime
            
            # Adjust priority based on current file status
            plan = self.load_json(DATA_DIR / 'plan.json')
            f_status = plan.get('files', {}).get(file_path.name, {}).get('status', '')
            if f_status == 'pending':
                # Strong boost: negative number makes it highest priority
                priority -= 1000000000
            elif f_status.startswith('error'):
                # Strong penalty: positive number makes it lowest priority
                priority += 1000000000
                
            self.queued_files.add(file_abs)
            self.file_queue.put((priority, file_abs))
            logging.info(f"Queued {file_path.name}")
        except Exception as e:
            logging.error(f"Error queuing {file_path.name}: {e}")

    def run_worker(self):
        """Background thread to process files from the queue based on agent state."""
        logging.info("Agent worker thread started.")
        last_heartbeat = 0
        last_scan = 0
        
        while True:
            # Heartbeat every 10 minutes
            if time.time() - last_heartbeat > 600:
                logging.info("Agent Heartbeat: Idle and waiting for files...")
                last_heartbeat = time.time()

            # Periodic Scan of input folder every 5 seconds (to detect files watchdog missed, e.g. Docker mounts)
            if time.time() - last_scan > 5:
                last_scan = time.time()
                input_path = self.config.get('input_folder', './input')
                try:
                    if os.path.isdir(input_path):
                        completed_paths = self.load_history()
                        plan = self.load_json(DATA_DIR / 'plan.json')
                        
                        for f in os.listdir(input_path):
                            f_path = Path(input_path) / f
                            if f_path.is_file() and not f.startswith('.'):
                                f_abs = str(f_path.absolute())
                                
                                # Only queue if not already in queue
                                if f_abs not in self.queued_files:
                                    # And not already successfully completed or archived
                                    plan_status = plan.get('files', {}).get(f, {}).get('status', '')
                                    is_done = f_abs in completed_paths or plan_status in ('completed', 'archived')
                                    
                                    # Unless it's explicitly marked as 'pending' (like when requesting re-review)
                                    if not is_done or plan_status == 'pending':
                                        self.queue_file(f_path)
                except Exception as e:
                    logging.error(f"Error during periodic scan of {input_path}: {e}")

            # Check agent state
            state_file = DATA_DIR / 'agent_state.json'
            if state_file.exists():
                try:
                    state_data = self.load_json(state_file)
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
                if file_path_str in self.queued_files:
                    self.queued_files.remove(file_path_str)
                
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
    logging.info(f"Testing connection to llama.cpp at {agent.llama_cpp_base} (60s timeout)...")
    try:
        import requests
        # Check OpenAI-compatible models endpoint
        resp = requests.get(f"{agent.llama_cpp_base}/models", timeout=60)
        if resp.status_code == 200:
            logging.info("Successfully connected to llama.cpp server.")
            models = [m['id'] for m in resp.json().get('data', [])]
            logging.info(f"Available models: {models}")
        else:
            logging.error(f"llama.cpp server returned status code {resp.status_code}")
    except Exception as e:
        logging.error(f"Failed to connect to llama.cpp: {e}")
    
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

        # --- NEW: Auto-recover stuck pending or processing files ---
        try:
            plan = agent.load_json(DATA_DIR / 'plan.json')
            archive_folder = Path(agent.config.get('archive_folder', './reviewed'))
            host_legacy = Path('/Users/bstove/Library/CloudStorage/SynologyDrive-local/projects/ricemaker/reviewed')
            legacy_archive = Path('./reviewed')

            for filename, info in plan.get('files', {}).items():
                status = info.get('status', '')
                if status == 'pending' or status.startswith('Processing'):
                    if status.startswith('Processing'):
                        logging.warning(f"File {filename} was stuck in {status}. Marking as error to prevent crash loops.")
                        agent.update_state(filename, "error (crashed during processing)", session_id=agent.session_id_str)
                        continue

                    orig_file = Path(input_path) / filename
                    if not orig_file.exists():
                        logging.info(f"Pending file {filename} missing from input. Attempting to recover...")
                        found_path = None
                        
                        # Search archive_folder
                        if archive_folder.exists():
                            for p in archive_folder.rglob(filename):
                                if p.is_file():
                                    found_path = p
                                    break
                        
                        # Search host-mapped legacy archive
                        if not found_path and host_legacy.exists():
                            for p in host_legacy.rglob(filename):
                                if p.is_file():
                                    found_path = p
                                    break

                        # Search container legacy archive
                        if not found_path and legacy_archive.exists() and legacy_archive.absolute() != archive_folder.absolute():
                            for p in legacy_archive.rglob(filename):
                                if p.is_file():
                                    found_path = p
                                    break

                        if found_path:
                            try:
                                import shutil
                                shutil.move(str(found_path), str(orig_file))
                                logging.info(f"Successfully recovered {filename} to {input_path}.")
                                agent.queue_file(orig_file)
                            except Exception as e:
                                logging.error(f"Failed to move {filename}: {e}")
                        else:
                            logging.warning(f"File {filename} not found in archives. Marking as missing.")
                            agent.update_state(filename, "error (missing)", session_id=agent.session_id_str)
        except Exception as e:
            logging.error(f"Error during auto-recovery scan: {e}")

    else:
        logging.error(f"Input path {input_path} is not a directory or is inaccessible. Check your Docker volume mounts.")
    
    # Final check before starting observer
    if is_accessible:
        state_file = DATA_DIR / 'agent_state.json'
        if not state_file.exists():
            state_file.write_text(json.dumps({"state": "running"}, indent=2))

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

