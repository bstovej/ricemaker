let selectedFile = null;
let currentView = 'dashboard';

function showView(view) {
    currentView = view;
    
    // Default visibility
    const controlPanel = document.getElementById('agent-controls');
    if (controlPanel) controlPanel.style.display = view === 'dashboard' ? 'flex' : 'none';
    document.getElementById('view-dashboard').style.display = view === 'dashboard' ? 'block' : 'none';
    document.getElementById('view-archive').style.display = view === 'archive' ? 'flex' : 'none';
    document.getElementById('view-stats').style.display = view === 'stats' ? 'flex' : 'none';
    document.getElementById('view-settings').style.display = view === 'settings' ? 'flex' : 'none';
    
    // Update nav active state
    document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));
    const activeNav = document.getElementById(`nav-${view}`);
    if (activeNav) activeNav.classList.add('active');

    const title = document.getElementById('page-title');
    const subtitle = document.getElementById('page-subtitle');

    if (view === 'dashboard') {
        title.innerText = "Rice Making Status";
        subtitle.innerText = "Real-time file processing and synthesis.";
    } else if (view === 'archive') {
        title.innerText = "File Archive";
        subtitle.innerText = "History of all reviewed and failed documents.";
    } else if (view === 'stats') {
        title.innerText = "Stats & Tokens";
        subtitle.innerText = "Detailed performance and consumption analytics.";
        refreshStats();
    } else if (view === 'settings') {
        title.innerText = "System Settings";
        subtitle.innerText = "Modify config.json and prompt templates.";
        loadSettings();
    }
    
    if (view !== 'settings') refreshDashboard();
}

async function loadSettings() {
    try {
        const res = await fetch('/api/settings');
        const data = await res.json();
        
        const configContainer = document.getElementById('config-fields');
        const promptContainer = document.getElementById('prompt-fields');
        
        if (!configContainer || !promptContainer) return;
        
        configContainer.innerHTML = '';
        promptContainer.innerHTML = '';
        
        // Render Config
        Object.entries(data.config).forEach(([key, value]) => {
            const div = document.createElement('div');
            div.style.display = 'flex';
            div.style.flexDirection = 'column';
            div.style.gap = '0.4rem';
            
            const label = document.createElement('label');
            label.innerText = key;
            label.style.fontSize = '0.75rem';
            label.style.color = 'var(--text-secondary)';
            label.style.fontWeight = '600';
            
            let input;
            if (typeof value === 'boolean') {
                input = document.createElement('select');
                input.innerHTML = `<option value="true" ${value ? 'selected' : ''}>True</option><option value="false" ${!value ? 'selected' : ''}>False</option>`;
            } else if (typeof value === 'number') {
                input = document.createElement('input');
                input.type = 'number';
                input.value = value;
                input.step = '0.1';
            } else {
                input = document.createElement('input');
                input.type = 'text';
                input.value = value;
            }
            
            input.id = `config-${key}`;
            input.className = 'btn btn-outline';
            input.style.textAlign = 'left';
            input.style.cursor = 'text';
            input.style.width = '100%';
            
            div.appendChild(label);
            div.appendChild(input);
            configContainer.appendChild(div);
        });
        
        // Render Prompts
        Object.entries(data.prompts).forEach(([key, value]) => {
            const div = document.createElement('div');
            div.style.display = 'flex';
            div.style.flexDirection = 'column';
            div.style.gap = '0.4rem';
            
            const label = document.createElement('label');
            label.innerText = key;
            label.style.fontSize = '0.75rem';
            label.style.color = 'var(--text-secondary)';
            label.style.fontWeight = '600';
            
            const input = document.createElement('textarea');
            input.value = value;
            input.id = `prompt-${key}`;
            input.className = 'btn btn-outline';
            input.style.textAlign = 'left';
            input.style.cursor = 'text';
            input.style.width = '100%';
            input.style.minHeight = '100px';
            input.style.fontFamily = 'inherit';
            input.style.resize = 'vertical';
            input.style.padding = '0.75rem';
            
            div.appendChild(label);
            div.appendChild(input);
            promptContainer.appendChild(div);
        });
        
    } catch (err) {
        console.error("Load Settings Error:", err);
    }
}

window.saveSettings = async function() {
    const configContainer = document.getElementById('config-fields');
    const promptContainer = document.getElementById('prompt-fields');
    
    if (!configContainer || !promptContainer) return;
    
    const config = {};
    configContainer.querySelectorAll('input, select').forEach(input => {
        const key = input.id.replace('config-', '');
        let value = input.value;
        if (input.type === 'number') value = parseFloat(value);
        if (input.tagName === 'SELECT') value = value === 'true';
        config[key] = value;
    });
    
    const prompts = {};
    promptContainer.querySelectorAll('textarea').forEach(input => {
        const key = input.id.replace('prompt-', '');
        prompts[key] = input.value;
        console.log(`Collecting prompt [${key}]: ${input.value.substring(0, 30)}...`);
    });
    
    console.log("Saving full payload:", { config, prompts });

    try {
        const res = await fetch('/api/settings', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ config, prompts })
        });
        const data = await res.json();
        if (data.success) {
            alert('Settings saved and agent restarted.');
            showView('dashboard');
        } else {
            alert('Error saving settings: ' + data.error);
        }
    } catch (err) {
        console.error("Save Settings Error:", err);
        alert('Failed to save settings.');
    }
};

function resetToMaster() {
    selectedFile = null;
    showView('dashboard');
}

/**
 * Shared helper to render Markdown content with YAML Frontmatter support
 */
function renderMarkdownWithYaml(container, content) {
    if (!content) return;
    
    const yamlRegex = /^---\n([\s\S]*?)\n---/;
    const match = content.match(yamlRegex);
    
    let htmlContent = "";
    let markdownContent = content;
    
    if (match) {
        const yaml = match[1];
        markdownContent = content.replace(yamlRegex, '');
        htmlContent = `
            <div style="background-color: var(--bg-tertiary); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem; margin-bottom: 1.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.8125rem; color: var(--text-secondary); line-height: 1.4;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">
                    <span style="color: var(--accent-primary); font-weight: 600;">Resource Metadata</span>
                    <span style="opacity: 0.5;">YAML Frontmatter</span>
                </div>
                <pre style="white-space: pre-wrap; margin: 0;">${yaml}</pre>
            </div>
        `;
    }
    
    container.innerHTML = htmlContent + marked.parse(markdownContent);
}

async function viewReport(filename) {
    selectedFile = filename;
    
    // Highlight selected row in both tables if they exist
    document.querySelectorAll('.file-row').forEach(r => {
        r.style.backgroundColor = 'transparent';
    });
    
    const rows = document.querySelectorAll(`[id="row-${filename}"]`);
    rows.forEach(row => {
        row.style.backgroundColor = 'var(--bg-tertiary)';
    });

    try {
        const res = await fetch(`/api/report/${encodeURIComponent(filename)}`);
        const data = await res.json();
        
        if (currentView === 'archive') {
            const container = document.getElementById('archive-summary-content');
            if (container && data.content) renderMarkdownWithYaml(container, data.content);
            const btnArchive = document.getElementById('btn-archive-current');
            const btnReReview = document.getElementById('btn-rereview');
            if (btnArchive) btnArchive.style.display = 'inline-flex';
            if (btnReReview) btnReReview.style.display = 'inline-flex';
        } else {
            // Use Modal for Dashboard file previews
            const modal = document.getElementById('report-modal');
            const modalContent = document.getElementById('modal-content');
            const modalTitle = document.getElementById('modal-title');
            
            if (modal && modalContent) {
                modalTitle.innerText = `File Report: ${filename}`;
                renderMarkdownWithYaml(modalContent, data.content || "# No Content\nReport text not found.");
                modal.style.display = 'flex';
                if (typeof lucide !== 'undefined') lucide.createIcons();
            }
        }
    } catch (err) {
        console.error("Fetch Report Error:", err);
    }
}

window.closeModal = function() {
    const modal = document.getElementById('report-modal');
    if (modal) modal.style.display = 'none';
};

async function refreshStats() {
    try {
        const res = await fetch('/api/stats');
        const stats = await res.json();
        const tableBody = document.getElementById('stats-table-body');
        
        if (!tableBody) return;
        tableBody.innerHTML = '';
        
        if (stats && stats.length > 0) {
            let totalTokens = 0;
            let totalInfTime = 0;
            let totalExtTime = 0;
            
            stats.reverse().forEach(s => {
                totalTokens += (s.total_tokens || 0);
                totalInfTime += (s.inference_time || 0);
                totalExtTime += (s.extraction_time || 0);
                
                tableBody.innerHTML += `
                    <tr>
                        <td style="white-space: nowrap;">${s.date}</td>
                        <td style="font-family: 'JetBrains Mono', monospace;">${s.filename}</td>
                        <td>${s.file_type}</td>
                        <td>${s.total_tokens}</td>
                        <td>${s.extraction_time}s</td>
                        <td>${s.inference_time}s</td>
                        <td><strong>${s.total_time}s</strong></td>
                    </tr>
                `;
            });
            
            document.getElementById('alltime-tokens').innerText = totalTokens > 1000 ? (totalTokens / 1000).toFixed(1) + 'k' : totalTokens;
            document.getElementById('avg-inference').innerText = (totalInfTime / stats.length).toFixed(1) + 's';
            document.getElementById('avg-extraction').innerText = (totalExtTime / stats.length).toFixed(1) + 's';
            document.getElementById('alltime-files').innerText = stats.length;
            document.getElementById('stats-record-count').innerText = `${stats.length} records`;
        }
    } catch (err) {
        console.error("Stats Load Error:", err);
    }
}

let lastMasterReportFilename = null;
let currentMasterReportSelection = ""; // empty means "Latest"

window.loadSpecificMasterReport = async function(filename) {
    currentMasterReportSelection = filename;
    const url = filename ? `/api/summary/${encodeURIComponent(filename)}` : '/api/summary';
    
    try {
        const res = await fetch(url);
        const summary = await res.json();
        const summaryContent = document.getElementById('summary-content');
        
        if (summaryContent && summary.content) {
            lastMasterReportFilename = summary.filename;
            renderMarkdownWithYaml(summaryContent, summary.content);
        }
    } catch (err) {
        console.error("Load Specific Master Error:", err);
    }
};

async function refreshDashboard() {
    try {
        const lastUpdatedEl = document.getElementById('last-updated');
        const syncIcon = document.getElementById('sync-icon');
        
        if (syncIcon && currentView === 'dashboard') syncIcon.style.transform = 'rotate(180deg)';
        
        // Sync Agent State
        try {
            const stateRes = await fetch('/api/agent/state');
            const stateData = await stateRes.json();
            const btnMain = document.getElementById('btn-agent-main');
            const btnStop = document.getElementById('btn-agent-stop');
            
            if (btnMain && btnStop) {
                if (stateData.state === 'running') {
                    btnMain.innerHTML = `<i data-lucide="pause" style="width: 14px; height: 14px;"></i> Pause`;
                    btnMain.className = 'btn btn-warning';
                    btnStop.style.display = 'inline-flex';
                } else if (stateData.state === 'paused') {
                    btnMain.innerHTML = `<i data-lucide="play" style="width: 14px; height: 14px;"></i> Resume`;
                    btnMain.className = 'btn btn-success';
                    btnStop.style.display = 'inline-flex';
                } else {
                    btnMain.innerHTML = `<i data-lucide="play" style="width: 14px; height: 14px;"></i> Start`;
                    btnMain.className = 'btn btn-primary';
                    btnStop.style.display = 'none';
                }
                if (typeof lucide !== 'undefined') lucide.createIcons();
            }
        } catch (e) {
            console.error("Failed to sync agent state", e);
        }
        
        const ts = Date.now();
        const statusRes = await fetch(`/api/status?t=${ts}`);
        const plan = await statusRes.json();
        const planFiles = plan.files || {};

        const sessionRes = await fetch(`/api/session?t=${ts}`);
        const sessionData = await sessionRes.json();
        const sessionStart = sessionData.session_start || 0;

        const filesRes = await fetch(`/api/files?t=${ts}`);
        const folderFiles = await filesRes.json();
        
        const queueBody = document.getElementById('status-table-body');
        const completedBody = document.getElementById('archive-completed-body');
        const errorBody = document.getElementById('archive-error-body');
        
        if (queueBody) queueBody.innerHTML = ''; 
        if (completedBody) completedBody.innerHTML = '';
        if (errorBody) errorBody.innerHTML = '';
        
        let completedCount = 0;
        let errorCount = 0;
        let pendingCount = 0;
        let missingCount = 0;
        
        const folderFileNames = new Set(folderFiles.map(f => f.name));
        const mergedList = folderFiles.map(f => {
            const planInfo = planFiles[f.name];
            return {
                name: f.name,
                status: planInfo ? planInfo.status : 'pending',
                timestamp: planInfo ? planInfo.timestamp : f.modified,
                model: planInfo ? planInfo.model : 'N/A',
                exists: true
            };
        });

        Object.entries(planFiles).forEach(([name, info]) => {
            if (!folderFileNames.has(name)) {
                mergedList.push({ 
                    name, 
                    status: info.status, 
                    timestamp: info.timestamp, 
                    model: info.model,
                    exists: false 
                });
            }
        });

        mergedList.sort((a, b) => b.timestamp - a.timestamp).forEach(f => {
            const isSelected = selectedFile === f.name;
            const dateStr = new Date(f.timestamp * 1000).toLocaleString();
            const modelName = f.model || 'Unknown';
            
            const isCurrentSession = f.timestamp >= sessionStart;
            const isError = f.status.startsWith('error');
            const isProcessing = f.status === 'pending' || f.status.includes('Processing');
            const isArchived = f.status === 'archived';
            const isCompleted = f.status === 'completed';
            
            // A file is a "Ghost" if it's supposed to be processed (pending/processing) but is missing from the folder.
            const isGhost = !f.exists && isProcessing;

            let displayStatus = f.status;
            let badgeClass = f.status.toLowerCase().split(' ')[0].replace('(', '').replace(')', '');
            
            if (isGhost) {
                displayStatus = 'Missing from Folder';
                badgeClass = 'error';
            }

            // Dashboard logic:
            // - Show it if it's currently processing/pending (even if missing/ghost)
            // - Show it if it was completed in the CURRENT session AND it's still in the input folder
            const showInDashboard = !isError && !isArchived && (isProcessing || (isCompleted && isCurrentSession && f.exists));

            if (showInDashboard) {
                // Show in Live Queue (Dashboard)
                pendingCount++;
                if (isGhost) missingCount++;
                
                if (queueBody) {
                    let statusHtml = `<span class="status-badge ${badgeClass}">${displayStatus}</span>`;
                    if (f.status === 'completed' && f.exists) statusHtml = `<span class="status-badge completed">Completed</span>`;
                    
                    const removeBtn = isGhost ? `<button onclick="event.stopPropagation(); window.removeFile('${f.name}')" class="btn btn-outline" style="padding: 0.1rem 0.4rem; font-size: 0.65rem; margin-left: 0.5rem;"><i data-lucide="trash-2" style="width: 10px; height: 10px;"></i></button>` : '';

                    queueBody.innerHTML += `
                        <tr onclick="viewReport('${f.name}')" style="cursor: pointer; background-color: ${isSelected ? 'var(--bg-tertiary)' : 'transparent'};" class="file-row" id="row-${f.name}">
                            <td style="width: 25%;">${statusHtml}${removeBtn}</td>
                            <td style="font-family: 'JetBrains Mono', monospace; width: 55%;">${f.name}</td>
                            <td style="color: var(--text-secondary); width: 20%;">${dateStr}</td>
                        </tr>`;
                }
            } else {
                // Show in Archive
                if (f.status === 'completed' || f.status === 'archived') {
                    completedCount++;
                    if (completedBody) {
                        let statusBadge = f.status === 'archived' ? '<span class="status-badge" style="margin-right: 0.5rem; background-color: var(--bg-secondary); color: var(--text-secondary); border: 1px solid var(--border-color); padding: 0.1rem 0.3rem;">Archived</span>' : '';
                        completedBody.innerHTML += `
                            <tr onclick="viewReport('${f.name}')" style="cursor: pointer; background-color: ${isSelected ? 'var(--bg-tertiary)' : 'transparent'};" class="file-row" id="row-${f.name}">
                                <td style="font-family: 'JetBrains Mono', monospace; width: 50%;">${statusBadge}${f.name}</td>
                                <td style="color: var(--text-secondary); font-size: 0.75rem; width: 25%;">${modelName}</td>
                                <td style="color: var(--text-secondary); width: 25%;">${dateStr}</td>
                            </tr>`;
                    }
                } else if (f.status.startsWith('error')) {
                    errorCount++;
                    if (errorBody) {
                        errorBody.innerHTML += `
                            <tr onclick="viewReport('${f.name}')" style="cursor: pointer; background-color: ${isSelected ? 'var(--bg-tertiary)' : 'transparent'};" class="file-row" id="row-${f.name}">
                                <td style="font-family: 'JetBrains Mono', monospace; width: 50%;">${f.name}</td>
                                <td style="color: var(--text-secondary); font-size: 0.75rem; width: 25%;">${modelName}</td>
                                <td style="color: var(--text-secondary); width: 25%;">${dateStr}</td>
                            </tr>`;
                    }
                }
            }
        });

        // The "Queue Size" header should show items that are still to be done
        const truePendingCount = mergedList.filter(f => !f.status.startsWith('error') && f.status !== 'archived' && (f.status === 'pending' || f.status.includes('Processing'))).length;
        document.getElementById('stat-total').innerText = truePendingCount;
        
        // Show cleanup button if there are missing files
        const cleanupBtn = document.getElementById('btn-cleanup-missing');
        if (cleanupBtn) {
            cleanupBtn.style.display = missingCount > 0 ? 'inline-flex' : 'none';
            cleanupBtn.innerHTML = `<i data-lucide="trash-2" style="width: 14px; height: 14px;"></i> Clean ${missingCount} Ghost Files`;
            if (typeof lucide !== 'undefined') lucide.createIcons();
        }

        if (document.getElementById('archive-completed-count')) document.getElementById('archive-completed-count').innerText = `${completedCount} files`;
        if (document.getElementById('archive-error-count')) document.getElementById('archive-error-count').innerText = `${errorCount} files`;

        if (sessionData) {
            document.getElementById('stat-session-processed').innerText = sessionData.processed || 0;
            const activeModelEl = document.getElementById('stat-active-model');
            if (activeModelEl) activeModelEl.innerText = sessionData.active_model || 'Idle';
            
            const tokens = sessionData.tokens || { prompt: 0, completion: 0 };
            const totalTokens = tokens.prompt + tokens.completion;
            
            let tokenStr = totalTokens;
            if (totalTokens > 1000) {
                tokenStr = (totalTokens / 1000).toFixed(1) + 'k';
            }
            document.getElementById('stat-session-tokens').innerText = tokenStr;
        }

        // Master Summary Panel Refresh
        if (currentView === 'dashboard') {
            const summaryUrl = currentMasterReportSelection ? `/api/summary/${encodeURIComponent(currentMasterReportSelection)}` : '/api/summary';
            const summaryRes = await fetch(summaryUrl);
            const summary = await summaryRes.json();
            const summaryContent = document.getElementById('summary-content');
            const reportsListBody = document.getElementById('master-reports-list');
            const selectEl = document.getElementById('master-report-select');

            // 1. Update Dropdown and Table List
            if (summary.reports) {
                if (selectEl) {
                    const currentValue = selectEl.value;
                    selectEl.innerHTML = '<option value="">Latest</option>';
                    summary.reports.forEach(r => {
                        const option = document.createElement('option');
                        option.value = r.name;
                        option.innerText = r.name;
                        selectEl.appendChild(option);
                    });
                    selectEl.value = currentValue;
                }

                if (reportsListBody) {
                    reportsListBody.innerHTML = "";
                    summary.reports.forEach(r => {
                        const dateStr = new Date(r.modified * 1000).toLocaleString();
                        const isSelected = (currentMasterReportSelection === r.name) || (!currentMasterReportSelection && r.name === summary.filename);
                        
                        reportsListBody.innerHTML += `
                            <tr onclick="window.loadSpecificMasterReport('${r.name}')" style="cursor: pointer; background-color: ${isSelected ? 'rgba(59, 130, 246, 0.1)' : 'transparent'};">
                                <td style="padding: 0.4rem 1rem; color: ${isSelected ? 'var(--accent-primary)' : 'var(--text-primary)'};">
                                    <i data-lucide="file-text" style="width: 12px; height: 12px; vertical-align: middle; margin-right: 0.5rem;"></i>
                                    ${r.name}
                                </td>
                                <td style="padding: 0.4rem 1rem; text-align: right; color: var(--text-secondary); font-size: 0.7rem;">${dateStr}</td>
                            </tr>
                        `;
                    });
                    if (typeof lucide !== 'undefined') lucide.createIcons();
                }
            }

            // 2. Update Display Content
            if (summaryContent && summary.content && summary.filename !== lastMasterReportFilename) {
                lastMasterReportFilename = summary.filename;
                if (summary.content !== "No master report generated yet.") {
                    renderMarkdownWithYaml(summaryContent, summary.content);
                }
            }
        }

        lastUpdatedEl.innerText = `Last sync: ${new Date().toLocaleTimeString()}`;
        if (syncIcon) setTimeout(() => syncIcon.style.transform = 'rotate(0deg)', 500);

    } catch (err) {
        console.error("Dashboard Sync Error:", err);
        document.getElementById('last-updated').innerText = "Sync Failed";
    }
}

// Initial load
refreshDashboard();
setInterval(refreshDashboard, 5000);

document.getElementById('sync-icon').addEventListener('click', refreshDashboard);

window.toggleAgentState = async function() {
    const btn = document.getElementById('btn-agent-main');
    if (!btn) return;
    const currentStateStr = btn.innerText.toLowerCase();
    
    let requestedState = 'running';
    if (currentStateStr.includes('pause')) {
        requestedState = 'paused';
    } else if (currentStateStr.includes('resume') || currentStateStr.includes('start')) {
        requestedState = 'running';
    }
    
    btn.innerHTML = '<i data-lucide="loader" style="width: 14px; height: 14px;"></i> Updating...';
    try {
        await fetch('/api/agent/state', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({state: requestedState})
        });
        refreshDashboard();
    } catch(err) {
        console.error(err);
    }
};

window.stopAgent = async function() {
    if (!confirm('Are you sure you want to completely stop the processing agent?')) return;
    try {
        await fetch('/api/agent/state', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({state: 'stopped'})
        });
        refreshDashboard();
    } catch(err) {
        console.error(err);
    }
};

window.archiveAllFiles = async function() {
    if (!confirm('Move all completed files from the input folder to the reviewed archive?')) return;
    try {
        await fetch('/api/files/move', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({files: []}) });
        refreshDashboard();
    } catch (err) { console.error(err); }
};

window.archiveCurrentFile = async function() {
    if (!selectedFile) return;
    try {
        const checkRes = await fetch(`/api/check_exists/${encodeURIComponent(selectedFile)}`);
        const { exists } = await checkRes.json();
        
        if (!exists) {
            if (confirm('File not found in input folder. Would you like to remove it from the file list altogether? (Cancel to put it back manually)')) {
                await fetch(`/api/remove/${encodeURIComponent(selectedFile)}`, { method: 'POST' });
                refreshDashboard();
            }
            return;
        }

        if (!confirm('Move this file to the reviewed archive?')) return;
        
        const res = await fetch('/api/files/move', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({files: [selectedFile]}) });
        const resJson = await res.json();
        if (resJson.errors && resJson.errors.length > 0) {
            alert('Failed to move file: ' + resJson.errors[0].error);
        }
        refreshDashboard();
    } catch (err) { console.error(err); }
};

window.rereviewCurrentFile = async function() {
    if (!selectedFile) return;
    
    if (!confirm('Force a re-review of this file? If it was archived, it will be moved back to the input folder.')) return;
    
    try {
        const res = await fetch(`/api/rereview/${encodeURIComponent(selectedFile)}`, { method: 'POST' });
        const data = await res.json();
        
        if (data.success) {
            refreshDashboard();
        } else {
            if (data.error === 'file_not_found') {
                if (confirm('File not found in input or archive. Would you like to remove it from the file list altogether?')) {
                    await fetch(`/api/remove/${encodeURIComponent(selectedFile)}`, { method: 'POST' });
                    refreshDashboard();
                }
            } else {
                alert('Failed to re-review: ' + (data.error || 'Unknown error'));
            }
        }
    } catch (err) { 
        console.error(err); 
        alert('An error occurred while attempting to re-review.');
    }
};

window.removeFile = async function(filename) {
    if (!confirm('Remove "' + filename + '" from the plan? This will NOT delete the actual file if it exists.')) return;
    try {
        await fetch('/api/remove/' + encodeURIComponent(filename), { method: 'POST' });
        refreshDashboard();
    } catch (err) { console.error(err); }
};

window.cleanupMissingFiles = async function() {
    if (!confirm('Remove all "ghost" files from the plan (files that are pending but missing from the input folder)?')) return;
    
    const statusRes = await fetch('/api/status');
    const plan = await statusRes.json();
    const planFiles = plan.files || {};
    
    const filesRes = await fetch('/api/files');
    const folderFiles = await filesRes.json();
    const folderFileNames = new Set(folderFiles.map(f => f.name));
    
    const missingFiles = Object.keys(planFiles).filter(name => {
        const info = planFiles[name];
        const isProcessing = info.status === 'pending' || info.status.includes('Processing');
        return !folderFileNames.has(name) && isProcessing;
    });
    
    for (const filename of missingFiles) {
        await fetch('/api/remove/' + encodeURIComponent(filename), { method: 'POST' });
    }
    refreshDashboard();
};
