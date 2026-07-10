from flask import Flask, jsonify, render_template, request
from pathlib import Path
import json, subprocess, shutil, os, time, re, sys
import pandas as pd

# Check config.json and keys.json presence and log warnings, but don't exit so Flask can serve the error UI
config_warnings = []
for filename, sample_name in [('config.json', 'sample_config.json'), ('keys.json', 'sample_keys.json')]:
    path = Path(filename)
    if not path.exists():
        config_warnings.append(f"WARNING: {filename} is missing! Use {sample_name} as reference.")
    elif path.is_dir():
        config_warnings.append(f"WARNING: {filename} exists as a directory! Remove it and create a file using {sample_name} as reference.")

for warning in config_warnings:
    print(warning, file=sys.stderr)

app = Flask(__name__, static_folder='data/static')

DATA_DIR = Path('data')
DATA_DIR.mkdir(parents=True, exist_ok=True)

# --- NEW: Zombie Process Reaper ---
import signal
def setup_reaper():
    """Sets up a signal handler to reap child processes automatically"""
    if os.name != 'nt':
        try:
            signal.signal(signal.SIGCHLD, lambda signum, frame: os.waitpid(-1, os.WNOHANG))
        except Exception:
            pass

setup_reaper()

def get_data(file):
    path = Path(file)
    return json.loads(path.read_text()) if path.exists() else {}

@app.route('/')
def index():
    return render_template('index.html')

agent_process = None

def start_agent():
    global agent_process
    # Verify config/keys are files before starting the agent process
    for filename in ('config.json', 'keys.json'):
        path = Path(filename)
        if not path.exists() or path.is_dir():
            return
            
    if agent_process is None or agent_process.poll() is not None:
        agent_process = subprocess.Popen(["python", "agent.py"])

def stop_agent():
    global agent_process
    if agent_process is not None and agent_process.poll() is None:
        agent_process.terminate()
        agent_process = None

@app.route('/api/agent/state', methods=['GET', 'POST'])
def agent_state():
    state_file = DATA_DIR / 'agent_state.json'
    if request.method == 'POST':
        new_state = request.json.get('state', 'running').lower()
        if new_state == 'stopped':
            stop_agent()
        elif new_state in ['running', 'paused']:
            if new_state == 'running':
                start_agent()
        state_file.write_text(json.dumps({'state': new_state}))
        return jsonify({'state': new_state})
        
    try:
        current_state = json.loads(state_file.read_text()).get('state', 'running')
    except:
        current_state = 'running'
    
    global agent_process
    if current_state != 'stopped' and (agent_process is None or agent_process.poll() is not None):
        start_agent()
        
    return jsonify({'state': current_state})

@app.route('/api/settings', methods=['GET', 'POST'])
def settings():
    config_file = Path('config.json')
    if request.method == 'POST':
        data = request.json
        new_config = data.get('config')
        new_prompts = data.get('prompts')
        
        if new_config:
            config_file.write_text(json.dumps(new_config, indent=2))
        
        if new_prompts:
            prompts_file_name = new_config.get('prompts_file', 'prompts.json') if new_config else 'prompts.json'
            prompts_file = Path(prompts_file_name)
            prompts_file.write_text(json.dumps(new_prompts, indent=2))
        
        # Trigger agent restart
        stop_agent()
        start_agent()
        
        return jsonify({"success": True})
        
    config = get_data('config.json')
    prompts_file = config.get('prompts_file', 'prompts.json')
    prompts = get_data(prompts_file)
    
    return jsonify({
        "config": config,
        "prompts": prompts
    })

_cache = {}

def get_cached_data(key, getter, ttl=5):
    now = time.time()
    if key in _cache and (now - _cache[key]['time']) < ttl:
        return _cache[key]['data']
    data = getter()
    _cache[key] = {'data': data, 'time': now}
    return data

@app.route('/api/status')
def status():
    """Returns the current processing plan for the dashboard"""
    return jsonify(get_cached_data('plan.json', lambda: get_data(DATA_DIR / 'plan.json'), ttl=3))

def check_llm_connection():
    try:
        config = get_data('config.json')
        keys = get_data('keys.json')
        if not config or not keys:
            return None
            
        provider = config.get('llm_provider', 'llama_cpp')
        
        if provider == 'llama_cpp':
            base_url = keys.get('LLAMA_CPP_API_BASE', 'http://host.docker.internal:8080/v1')
            import requests
            resp = requests.get(f"{base_url}/models", timeout=2)
            if resp.status_code == 200:
                return None
            return f"LLM Connection Error: llama.cpp server at {base_url} returned status code {resp.status_code}."
        elif provider == 'ollama':
            base_url = keys.get('OLLAMA_API_BASE', 'http://host.docker.internal:11434')
            import requests
            resp = requests.get(base_url, timeout=2)
            if resp.status_code in (200, 404):
                return None
            return f"LLM Connection Error: Ollama server at {base_url} returned status code {resp.status_code}."
    except Exception as e:
        return f"LLM Connection Error: Failed to connect to local LLM server. Please check if your LLM server/Ollama is running. Details: {e}"
    return None

@app.route('/api/session')
def session_stats():
    """Returns current session progress, token counts, and connection/configuration errors"""
    # Force fresh read of state/session rather than caching forever if there are errors
    session_data = get_data(DATA_DIR / 'session_stats.json')
    if not session_data:
        session_data = {
            "session_start": time.time(),
            "processed": 0,
            "tokens": {"prompt": 0, "completion": 0},
            "active_model": "Syncing...",
            "last_active": time.time()
        }
    
    plan = get_data(DATA_DIR / 'plan.json')
    session_data['total_received_count'] = plan.get('total_received_count', 0)
        
    # Check config/keys presence first
    config_errors = []
    for filename, sample_name in [('config.json', 'sample_config.json'), ('keys.json', 'sample_keys.json')]:
        path = Path(filename)
        if not path.exists():
            config_errors.append(f"CRITICAL ERROR: {filename} is missing! Please create it by copying the reference {sample_name} file.")
        elif path.is_dir():
            config_errors.append(f"CRITICAL ERROR: {filename} exists as a directory! Please remove it and create a proper JSON file referencing {sample_name}.")
            
    if config_errors:
        session_data['status_message'] = " | ".join(config_errors)
        session_data['status_type'] = 'error'
    else:
        llm_error = check_llm_connection()
        if llm_error:
            session_data['status_message'] = llm_error
            session_data['status_type'] = 'error'
        else:
            config = get_data('config.json')
            input_folder = Path(config.get('input_folder', './input'))
            
            current_input_files = set()
            if input_folder.exists() and input_folder.is_dir():
                for f in input_folder.iterdir():
                    if f.is_file() and not f.name.startswith('.'):
                        current_input_files.add(f.name)
            
            plan = get_data(DATA_DIR / 'plan.json')
            plan_files = plan.get('files', {})
            
            # Union of physically present input files and historically recorded files
            all_file_names = current_input_files.union(plan_files.keys())
            
            # Total Files Received
            total_received = plan.get('total_received_count', 0)
            if total_received <= 0:
                total_received = len(all_file_names)
            
            # Active Queue Size
            queue_size = 0
            for name in all_file_names:
                info = plan_files.get(name, {})
                status = info.get('status', 'pending')
                if not status.startswith('error') and status != 'archived' and (status == 'pending' or 'Processing' in status):
                    queue_size += 1
            
            # Ensure total_received is at least as large as the queue size for safety
            if total_received < queue_size:
                total_received = queue_size
                
            if total_received > 0:
                pct = int(((total_received - queue_size) / total_received) * 100)
                session_data['status_message'] = f"Ricemaking in progress - {pct}% completed"
                session_data['status_type'] = 'progress'
            else:
                session_data['status_message'] = "Ricemaking in progress - 0% completed"
                session_data['status_type'] = 'progress'
                
    return jsonify(session_data)

@app.route('/api/files')
def list_files():
    """Scans the input folder from config.json and returns all files"""
    def _get_files():
        config = get_data('config.json')
        input_folder = Path(config.get('input_folder', './input'))
        files = []
        if input_folder.exists():
            for f in input_folder.iterdir():
                if f.is_file() and not f.name.startswith('.'):
                    try:
                        stats = f.stat()
                        files.append({
                            "name": f.name,
                            "size": stats.st_size,
                            "modified": stats.st_mtime
                        })
                    except: continue
        return files
    
    return jsonify(get_cached_data('input_files', _get_files, ttl=10))

@app.route('/api/stats')
def stats():
    """Returns cost and latency data from stats.csv"""
    def _get_stats():
        import pandas as pd
        stats_path = DATA_DIR / 'stats.csv'
        if stats_path.exists():
            df = pd.read_csv(stats_path)
            return df.to_dict(orient='records')
        return []
    
    return jsonify(get_cached_data('stats_csv', _get_stats, ttl=15))

@app.route('/api/report/<path:filename>')
def get_report(filename):
    """Fetches a specific AI report from the output folder defined in config.json"""
    import urllib.parse
    config = get_data('config.json')
    output_dir = Path(config.get('output_folder', './output'))
    
    # Flask <path:filename> usually decodes slashes and spaces, but let's ensure clean decoding
    decoded_name = urllib.parse.unquote(filename)
    
    # Check if there is an error message in plan.json
    plan = get_data(DATA_DIR / 'plan.json')
    file_plan = plan.get('files', {}).get(decoded_name, {})
    if file_plan.get('status', '').startswith('error') and file_plan.get('error_msg'):
        return jsonify({"content": f"# Extraction Failed\n\n**File:** `{decoded_name}`\n\n**Error Result:**\n```text\n{file_plan.get('error_msg')}\n```"})

    # The agent normally saves as "filename.ext.md"
    report_filename = f"{decoded_name}.md" if not decoded_name.endswith('.md') else decoded_name
    report_path = output_dir / report_filename
    
    # 1. Primary check: direct hit in output_dir
    if not report_path.exists():
        # 2. Fallback: Search recursively in output_dir
        matches = list(output_dir.rglob(report_filename))
        if matches:
            report_path = matches[0]
        else:
            # 3. Fallback: Search in the vault root (parent of output_dir or grandparent)
            # We'll try searching from the grandparent if output_dir is nested (like 00_Inbox/ricepack)
            vault_root = output_dir.parent
            if "00_Inbox" in vault_root.name:
                vault_root = vault_root.parent
            
            if vault_root.exists():
                matches = list(vault_root.rglob(report_filename))
                if matches:
                    report_path = matches[0]

    if report_path.exists():
        try:
            return jsonify({"content": report_path.read_text(encoding='utf-8')})
        except Exception as e:
            return jsonify({"error": f"Read failed: {str(e)}"}), 500
    
    return jsonify({"error": f"Report not found. Looked for '{report_filename}' in {output_dir} and its parent."}), 404

@app.route('/api/summary')
@app.route('/api/summary/<path:filename>')
def summary(filename=None):
    """Reads master reports from the configured output folder"""
    config = get_data('config.json')
    output_dir = Path(config.get('output_folder', './output'))
    
    # Find all master reports
    master_files = list(output_dir.glob('master_report_*.md'))
    
    # Also check for the old master_report.md
    old_master = output_dir / 'master_report.md'
    if old_master.exists():
        master_files.append(old_master)
    
    # Sort by modification time (newest first)
    master_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    
    # --- NEW: Filter by active plan entries (Hide purged reports) ---
    plan = get_data(DATA_DIR / 'plan.json')
    active_sessions = set()
    for f_info in plan.get('files', {}).values():
        sid = f_info.get('session_id')
        if sid: active_sessions.add(sid)
        
    filtered_master_files = []
    for f in master_files:
        # 1. Check for session ID in filename
        match = re.search(r'master_report_(.*?)\.md', f.name)
        if match:
            if match.group(1) in active_sessions:
                filtered_master_files.append(f)
        # 2. Always show legacy master_report.md if it exists
        elif f.name == 'master_report.md':
            filtered_master_files.append(f)
            
    master_files = filtered_master_files
    report_list = [{"name": f.name, "modified": f.stat().st_mtime} for f in master_files]
    
    if not master_files:
        return jsonify({
            "content": "No master report generated yet.",
            "reports": []
        })
    
    # If a specific filename is requested, find it
    selected_report = None
    if filename:
        import urllib.parse
        decoded_name = urllib.parse.unquote(filename)
        selected_report = next((f for f in master_files if f.name == decoded_name), None)
    
    # Default to the newest report if none specified or not found
    if not selected_report:
        selected_report = master_files[0]
    
    return jsonify({
        "content": selected_report.read_text(encoding='utf-8'),
        "filename": selected_report.name,
        "reports": report_list
    })

@app.route('/api/check_exists/<path:filename>', methods=['GET'])
def check_exists(filename):
    import urllib.parse
    decoded_name = urllib.parse.unquote(filename)
    config = get_data('config.json')
    input_folder = Path(config.get('input_folder', './input'))
    orig_file = input_folder / decoded_name
    return jsonify({"exists": orig_file.exists()})

@app.route('/api/remove/<path:filename>', methods=['POST'])
def remove_file(filename):
    import urllib.parse
    decoded_name = urllib.parse.unquote(filename)
    
    plan_path = DATA_DIR / 'plan.json'
    history_path = DATA_DIR / 'history.csv'
    
    if plan_path.exists():
        try:
            plan = json.loads(plan_path.read_text())
            if 'files' in plan and decoded_name in plan['files']:
                del plan['files'][decoded_name]
                plan_path.write_text(json.dumps(plan, indent=2))
        except Exception as e:
            print(f"Error removing from plan: {e}")
            
    if history_path.exists():
        try:
            df = pd.read_csv(history_path)
            df = df[~df['original_path'].fillna('').str.endswith(decoded_name)]
            df.to_csv(history_path, index=False)
        except Exception as e:
            print(f"Error updating history: {e}")
            
    return jsonify({"success": True})

@app.route('/api/rereview/<path:filename>', methods=['POST'])
def rereview(filename):
    import urllib.parse
    decoded_name = urllib.parse.unquote(filename)
    
    plan_path = DATA_DIR / 'plan.json'
    history_path = DATA_DIR / 'history.csv'
    
    config = get_data('config.json')
    input_folder = Path(config.get('input_folder', './input'))
    archive_folder = Path(config.get('archive_folder', './reviewed'))

    # 0. Check legacy archives (prioritize host-mapped path if accessible)
    host_legacy = Path('/Users/bstove/Library/CloudStorage/SynologyDrive-local/projects/ricemaker/reviewed')
    legacy_archive = Path('./reviewed')

    orig_file = input_folder / decoded_name

    # 1. Check if it's already in the input folder
    if not orig_file.exists():
        # 2. Try to find it in the archive_folder (recursively)
        found_path = None
        if archive_folder.exists():
            for p in archive_folder.rglob(decoded_name):
                if p.is_file():
                    found_path = p
                    break

        # 3. Try to find it in the host-mapped legacy archive folder
        if not found_path and host_legacy.exists():
            for p in host_legacy.rglob(decoded_name):
                if p.is_file():
                    found_path = p
                    break

        # 4. Try to find it in the container-local legacy archive folder
        if not found_path and legacy_archive.exists() and legacy_archive.absolute() != archive_folder.absolute():
            for p in legacy_archive.rglob(decoded_name):
                if p.is_file():
                    found_path = p
                    break

        # 5. If found in any archive, move it back to input_folder
        if found_path:
            try:
                shutil.move(str(found_path), str(orig_file))
            except Exception as e:
                return jsonify({"success": False, "error": f"Failed to move from archive: {str(e)}"})
        else:
            return jsonify({"success": False, "error": "file_not_found"})

    # 6. Reset status and history
    if plan_path.exists():
        plan = json.loads(plan_path.read_text())
        if 'files' in plan and decoded_name in plan['files']:
            plan['files'][decoded_name]['status'] = 'pending'
            # Reset timestamp so it shows up at the top of the dashboard
            plan['files'][decoded_name]['timestamp'] = time.time()
            plan_path.write_text(json.dumps(plan, indent=2))
    if history_path.exists():
        try:
            df = pd.read_csv(history_path)
            # Remove all entries for this file
            df = df[~df['original_path'].fillna('').str.endswith(decoded_name)]
            df.to_csv(history_path, index=False)
        except Exception as e:
            print(f"Error updating history: {e}")
            
    # Touch the file so the watcher picks it up
    try:
        os.utime(orig_file, None)
    except:
        pass
        
    return jsonify({"success": True})

def get_best_archive_folder(tags, archive_dir):
    """
    Finds the best sub-folder in archive_dir based on tags.
    If no match found, returns a new folder name based on the primary tag.
    """
    if not tags:
        return "General"
        
    # 1. List existing sub-folders
    existing_subfolders = []
    if archive_dir.exists():
        existing_subfolders = [d.name for d in archive_dir.iterdir() if d.is_dir()]
    
    # 2. Try to find a match among existing sub-folders
    for tag in tags:
        tag_lower = tag.lower()
        # Direct match
        for sub in existing_subfolders:
            if tag_lower == sub.lower():
                return sub
        
        # Partial match for "domain/subject" -> "subject"
        if '/' in tag:
            subject = tag.split('/')[-1].lower()
            for sub in existing_subfolders:
                if subject == sub.lower():
                    return sub
                    
    # 3. No match found, create a new folder name based on the first tag
    primary_tag = tags[0]
    # Use "Subject" part of "Domain/Subject" if possible, otherwise use full tag
    new_folder = primary_tag.split('/')[-1] if '/' in primary_tag else primary_tag
    # Capitalize for aesthetics if it was all lowercase
    if new_folder.islower():
        new_folder = new_folder.title()
    elif '/' in primary_tag and new_folder == primary_tag.split('/')[-1]:
        # If it was domain/subject, and we took subject, title case it
        new_folder = new_folder.title()
        
    return new_folder

def _move_file_to_archive(filename, input_dir, archive_dir, output_dir, plan):
    """Internal helper to move a file and update its report/plan status"""
    orig_file = input_dir / filename
    if not orig_file.exists():
        return False, "file_not_found"
        
    file_info = plan.get('files', {}).get(filename, {})
    tags = file_info.get('tags', [])
    
    subfolder_name = get_best_archive_folder(tags, archive_dir)
    target_dir = archive_dir / subfolder_name
    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)
        
    dest_file = target_dir / filename
    report_path = output_dir / f"{filename}.md"
    
    try:
        shutil.move(str(orig_file), str(dest_file))
        
        # Update Report Frontmatter
        if report_path.exists():
            content = report_path.read_text(encoding='utf-8')
            # Update source path to new absolute path
            new_content = re.sub(r'(^source:\s*").*?(")', f'\\1{dest_file.absolute()}\\2', content, flags=re.MULTILINE)
            report_path.write_text(new_content, encoding='utf-8')
            
        # Update Plan status
        if filename in plan.get('files', {}):
            plan['files'][filename]['status'] = 'archived'
            
        return True, None
    except Exception as e:
        return False, str(e)

@app.route('/api/files/move', methods=['POST'])
def move_files():
    data = request.json or {}
    target_files = data.get('files', [])
    config = get_data('config.json')
    output_dir = Path(config.get('output_folder', './output'))
    input_dir = Path(config.get('input_folder', './input'))
    archive_dir = Path(config.get('archive_folder', './reviewed'))
    
    if not archive_dir.exists():
        archive_dir.mkdir(parents=True)
        
    plan = get_data(DATA_DIR / 'plan.json')
    files_to_move = target_files
    if not target_files:
        files_to_move = [k for k, v in plan.get('files', {}).items() if v.get('status') == 'completed']
    
    moved = []
    errors = []
    
    for filename in files_to_move:
        success, err = _move_file_to_archive(filename, input_dir, archive_dir, output_dir, plan)
        if success:
            moved.append(filename)
        else:
            if err == "file_not_found" and target_files:
                return jsonify({"success": False, "error": "file_not_found", "message": f"{filename} not found in input directory."})
            if err != "file_not_found":
                errors.append({"file": filename, "error": err})
            
    if moved:
        try:
            (DATA_DIR / 'plan.json').write_text(json.dumps(plan, indent=2))
        except Exception as e:
            print(f"Error saving plan.json: {e}")
            
    return jsonify({"moved": moved, "errors": errors})

def _purge_file_data(filename, plan):
    """Helper to remove a file from plan, history, and delete intermediate chunks"""
    # 1. Delete intermediate chunks
    config = get_data('config.json')
    intermediate_dir = Path(config.get('intermediate_folder', './intermediate'))
    if intermediate_dir.exists():
        for p in intermediate_dir.glob(f"{filename}_chunk_*.md"):
            try: p.unlink()
            except: pass
            
    # 2. Remove from plan
    if filename in plan.get('files', {}):
        del plan['files'][filename]
        
    # 3. Remove from history.csv
    history_path = DATA_DIR / 'history.csv'
    if history_path.exists():
        try:
            df = pd.read_csv(history_path)
            # Match by original filename in the path
            df = df[~df['original_path'].fillna('').str.endswith(filename)]
            df.to_csv(history_path, index=False)
        except: pass

@app.route('/api/cleanup/archived', methods=['POST'])
def cleanup_archived():
    plan = get_data(DATA_DIR / 'plan.json')
    files_to_purge = [name for name, info in plan.get('files', {}).items() if info.get('status') == 'archived']
    
    for filename in files_to_purge:
        _purge_file_data(filename, plan)
        
    # Reset total received count to count of remaining active files in plan
    plan['total_received_count'] = len(plan.get('files', {}))
    
    (DATA_DIR / 'plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({"success": True, "count": len(files_to_purge)})

@app.route('/api/rereview/errors', methods=['POST'])
def rereview_errors():
    plan = get_data(DATA_DIR / 'plan.json')
    config = get_data('config.json')
    input_folder = Path(config.get('input_folder', './input'))
    
    count_reset = 0
    count_purged = 0
    
    # We need to iterate over a copy of keys because we might delete items
    filenames = list(plan.get('files', {}).keys())
    
    for name in filenames:
        info = plan['files'][name]
        if info.get('status', '').startswith('error'):
            orig_file = input_folder / name
            if orig_file.exists():
                # 1. Reset for re-review
                info['status'] = 'pending'
                info['timestamp'] = time.time()
                try: os.utime(orig_file, None)
                except: pass
                count_reset += 1
            else:
                # 2. File missing, purge data instead of resetting
                _purge_file_data(name, plan)
                count_purged += 1
            
    (DATA_DIR / 'plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({
        "success": True, 
        "reset_count": count_reset, 
        "purged_count": count_purged
    })

@app.route('/api/archive/errors', methods=['POST'])
def archive_errors():
    plan = get_data('plan.json')
    config = get_data('config.json')
    input_folder = Path(config.get('input_folder', './input'))
    archive_dir = Path(config.get('archive_folder', './reviewed'))
    error_archive_dir = archive_dir / "Error Processing"
    
    if not error_archive_dir.exists():
        error_archive_dir.mkdir(parents=True, exist_ok=True)
        
    count_archived = 0
    errors = []

    filenames = list(plan.get('files', {}).keys())
    for name in filenames:
        info = plan['files'][name]
        if info.get('status', '').startswith('error'):
            orig_file = input_folder / name
            if orig_file.exists():
                dest_file = error_archive_dir / name
                try:
                    shutil.move(str(orig_file), str(dest_file))
                    _purge_file_data(name, plan)
                    count_archived += 1
                except Exception as e:
                    errors.append({"file": name, "error": str(e)})
            else:
                # If file doesn't exist, purge from plan
                _purge_file_data(name, plan)

    Path('plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({
        "success": True,
        "archived_count": count_archived,
        "errors": errors
    })

@app.route('/api/master_report/purge/<path:filename>', methods=['POST'])
def purge_master_report(filename):
    import urllib.parse
    decoded_name = urllib.parse.unquote(filename)
    
    # 1. Extract session ID: master_report_20260504_1107.md -> 20260504_1107
    match = re.search(r'master_report_(.*?)\.md', decoded_name)
    if not match:
        return jsonify({"success": False, "error": "Invalid master report filename"}), 400
    
    session_id = match.group(1)
    plan = get_data(DATA_DIR / 'plan.json')
    
    # 2. Identify files in this session
    files_in_session = []
    for name, info in plan.get('files', {}).items():
        if info.get('session_id') == session_id:
            files_in_session.append(name)
            
    # 3. Process files (Skip errors)
    files_to_archive = []
    files_to_purge = []
    
    for name in files_in_session:
        status = plan['files'][name].get('status', '')
        if status.startswith('error'):
            continue # Skip errors
        
        if status == 'completed':
            files_to_archive.append(name)
            files_to_purge.append(name)
        elif status == 'archived':
            files_to_purge.append(name)
            
    # 4. Archive completed files first
    if files_to_archive:
        # We can't easily call move_files() directly due to request context, 
        # so we'll implement the move logic or refactor it.
        # For simplicity, I'll just trigger the archive logic here.
        # Note: move_files needs a request with JSON.
        pass # We will handle this in the next step by refactoring move_files
        
    # Trigger archiving for files_to_archive
    for name in files_to_archive:
        _move_file_to_archive(name, input_dir, archive_dir, output_dir, plan)

    # 5. Purge tracking data and intermediate files for all (now) archived files in session
    for name in files_to_purge:
        _purge_file_data(name, plan)
        
    # 6. We do NOT delete the master report markdown file or individual summaries.
    # By removing the session files from plan.json, the master report will naturally
    # stop showing up in the "Master Summaries" list because the list is derived
    # from files currently tracked in the plan.
        
    (DATA_DIR / 'plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({"success": True})

if __name__ == '__main__':
    # Initialize the agent state to match logic on startup
    state_file = DATA_DIR / 'agent_state.json'
    if not state_file.exists():
        state_file.write_text(json.dumps({'state': 'running'}))
    else:
        # Don't auto-start if previously stopped
        pass
        
    start_agent()
    # Run Flask on all interfaces so your desktop browser can reach it
    app.run(host='0.0.0.0', port=1688, debug=False)

