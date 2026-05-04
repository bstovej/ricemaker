from flask import Flask, jsonify, render_template, request
from pathlib import Path
import json, subprocess, shutil, os, time, re
import pandas as pd
app = Flask(__name__)

def get_data(file):
    path = Path(file)
    return json.loads(path.read_text()) if path.exists() else {}

@app.route('/')
def index():
    return render_template('index.html')

agent_process = None

def start_agent():
    global agent_process
    if agent_process is None or agent_process.poll() is not None:
        agent_process = subprocess.Popen(["python", "agent.py"])

def stop_agent():
    global agent_process
    if agent_process is not None and agent_process.poll() is None:
        agent_process.terminate()
        agent_process = None

@app.route('/api/agent/state', methods=['GET', 'POST'])
def agent_state():
    state_file = Path('agent_state.json')
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
    return jsonify(get_cached_data('plan.json', lambda: get_data('plan.json'), ttl=3))

@app.route('/api/session')
def session_stats():
    """Returns current session progress and token counts"""
    return jsonify(get_cached_data('session_stats.json', lambda: get_data('session_stats.json'), ttl=3))

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
        if Path('stats.csv').exists():
            df = pd.read_csv('stats.csv')
            return df.to_dict(orient='records')
        return []
    
    return jsonify(get_cached_data('stats_csv', _get_stats, ttl=15))

@app.route('/api/report/<path:filename>')
def get_report(filename):
    """Fetches a specific AI report from the output folder defined in config.json"""
    import urllib.parse
    config = get_data('config.json')
    output_dir = Path(config.get('output_folder', './output'))
    
    # Flask <path:filename> might already be decoded, but let's be safe
    decoded_name = urllib.parse.unquote(filename)
    
    # The agent saves as "filename.ext.md"
    report_path = output_dir / f"{decoded_name}.md"
    
    # Check if there is an error message in plan.json
    plan = get_data('plan.json')
    file_plan = plan.get('files', {}).get(decoded_name, {})
    if file_plan.get('status', '').startswith('error') and file_plan.get('error_msg'):
        return jsonify({"content": f"# Extraction Failed\n\n**File:** `{decoded_name}`\n\n**Error Result:**\n```text\n{file_plan.get('error_msg')}\n```"})

    if not report_path.exists():
        # Fallback: maybe the filename already has .md in the request?
        if not decoded_name.endswith('.md'):
            report_path = output_dir / f"{decoded_name}.md"
        else:
            report_path = output_dir / decoded_name

    if report_path.exists():
        try:
            return jsonify({"content": report_path.read_text(encoding='utf-8')})
        except Exception as e:
            return jsonify({"error": f"Read failed: {str(e)}"}), 500
    
    return jsonify({"error": f"Report not found at {report_path}"}), 404

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
    
    plan_path = Path('plan.json')
    history_path = Path('history.csv')
    
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
    
    plan_path = Path('plan.json')
    history_path = Path('history.csv')
    
    config = get_data('config.json')
    input_folder = Path(config.get('input_folder', './input'))
    archive_folder = Path(config.get('archive_folder', './reviewed'))

    # 0. Check legacy archives (prioritize host-mapped path if accessible)
    host_legacy = Path('/Users/bstove/LocalDocs/projects/ricemaker/reviewed')
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
        
    plan = get_data('plan.json')
    files_to_move = target_files
    if not target_files:
        files_to_move = [k for k, v in plan.get('files', {}).items() if v.get('status') == 'completed']
    
    moved = []
    errors = []
    
    for filename in files_to_move:
        orig_file = input_dir / filename
        if not orig_file.exists():
            if target_files:
                return jsonify({"success": False, "error": "file_not_found", "message": f"{filename} not found in input directory."})
            continue
            
        report_path = output_dir / f"{filename}.md"
        category = "General"
        
        file_plan = plan.get('files', {}).get(filename, {})
        if file_plan.get('status', '').startswith('error'):
            category = "error_files"
        elif report_path.exists():
            content = report_path.read_text(encoding='utf-8')
            match = re.search(r'^tags:\s*\[?(?:["\'])?([^/"\',\]\s]+)', content, re.MULTILINE | re.IGNORECASE)
            if match:
                category = match.group(1).strip()
            else:
                # Fallback to category if tags not found
                match_cat = re.search(r'^category:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
                if match_cat and match_cat.group(1).lower() != 'resource':
                    category = match_cat.group(1).replace('/', '_')
        
        cat_lower = category.lower()
        existing_folders = [d.name for d in archive_dir.iterdir() if d.is_dir()]
        matched_folder = None
        for folder in existing_folders:
            if cat_lower in folder.lower() or folder.lower() in cat_lower:
                matched_folder = folder
                break
                
        if not matched_folder:
            matched_folder = category
            (archive_dir / matched_folder).mkdir(exist_ok=True)
            
        dest_file = archive_dir / matched_folder / filename
        try:
            shutil.move(str(orig_file), str(dest_file))
            moved.append(filename)
            
            if report_path.exists():
                content = report_path.read_text(encoding='utf-8')
                new_content = re.sub(r'(^source:\s*").*?(")', f'\\1{dest_file.absolute()}\\2', content, flags=re.MULTILINE)
                report_path.write_text(new_content, encoding='utf-8')
                
            if filename in plan.get('files', {}):
                plan['files'][filename]['status'] = 'archived'
                
        except Exception as e:
            errors.append({"file": filename, "error": str(e)})
            
    if moved:
        try:
            Path('plan.json').write_text(json.dumps(plan, indent=2))
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
    history_path = Path('history.csv')
    if history_path.exists():
        try:
            df = pd.read_csv(history_path)
            # Match by original filename in the path
            df = df[~df['original_path'].fillna('').str.endswith(filename)]
            df.to_csv(history_path, index=False)
        except: pass

@app.route('/api/cleanup/archived', methods=['POST'])
def cleanup_archived():
    plan = get_data('plan.json')
    files_to_purge = [name for name, info in plan.get('files', {}).items() if info.get('status') == 'archived']
    
    for filename in files_to_purge:
        _purge_file_data(filename, plan)
        
    Path('plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({"success": True, "count": len(files_to_purge)})

@app.route('/api/rereview/errors', methods=['POST'])
def rereview_errors():
    plan = get_data('plan.json')
    config = get_data('config.json')
    input_folder = Path(config.get('input_folder', './input'))
    
    count = 0
    for name, info in plan.get('files', {}).items():
        if info.get('status', '').startswith('error'):
            info['status'] = 'pending'
            info['timestamp'] = time.time()
            # Touch the file
            orig_file = input_folder / name
            if orig_file.exists():
                try: os.utime(orig_file, None)
                except: pass
            count += 1
            
    Path('plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({"success": True, "count": count})

@app.route('/api/master_report/purge/<path:filename>', methods=['POST'])
def purge_master_report(filename):
    import urllib.parse
    decoded_name = urllib.parse.unquote(filename)
    
    # 1. Extract session ID: master_report_20260504_1107.md -> 20260504_1107
    match = re.search(r'master_report_(.*?)\.md', decoded_name)
    if not match:
        return jsonify({"success": False, "error": "Invalid master report filename"}), 400
    
    session_id = match.group(1)
    plan = get_data('plan.json')
    
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
    # (Re-using logic from move_files internally)
    config = get_data('config.json')
    input_dir = Path(config.get('input_folder', './input'))
    archive_dir = Path(config.get('archive_folder', './reviewed'))
    output_dir = Path(config.get('output_folder', './output'))
    
    for name in files_to_archive:
        orig_file = input_dir / name
        if not orig_file.exists(): continue
        
        report_path = output_dir / f"{name}.md"
        category = "General"
        if report_path.exists():
            content = report_path.read_text(encoding='utf-8')
            match_tags = re.search(r'^tags:\s*\[?(?:["\'])?([^/"\',\]\s]+)', content, re.MULTILINE | re.IGNORECASE)
            if match_tags: category = match_tags.group(1).strip()
            
        target_folder = archive_dir / category
        target_folder.mkdir(parents=True, exist_ok=True)
        dest_file = target_folder / name
        
        try:
            shutil.move(str(orig_file), str(dest_file))
            if report_path.exists():
                content = report_path.read_text(encoding='utf-8')
                new_content = re.sub(r'(^source:\s*").*?(")', f'\\1{dest_file.absolute()}\\2', content, flags=re.MULTILINE)
                report_path.write_text(new_content, encoding='utf-8')
        except: pass

    # 5. Purge all (now) archived files in session
    for name in files_to_purge:
        _purge_file_data(name, plan)
        
    # 6. Delete master report
    master_path = output_dir / decoded_name
    if master_path.exists():
        try: master_path.unlink()
        except: pass
        
    Path('plan.json').write_text(json.dumps(plan, indent=2))
    return jsonify({"success": True})

if __name__ == '__main__':
    # Initialize the agent state to match logic on startup
    state_file = Path('agent_state.json')
    if not state_file.exists():
        state_file.write_text(json.dumps({'state': 'running'}))
    else:
        # Don't auto-start if previously stopped
        pass
        
    start_agent()
    # Run Flask on all interfaces so your desktop browser can reach it
    app.run(host='0.0.0.0', port=1688, debug=False)

