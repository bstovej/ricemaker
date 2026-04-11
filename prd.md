# Project Requirements: Ricemaker
## 1. Executive Summary
**Project Name:** Ricemaker  
**Purpose:** An automated, durable AI agent designed to "process" raw local files (text, documents, audio, video) into structured AI reviews and consolidated executive summaries.  
**Core Value:** Provides a "set-and-forget" workflow for personal knowledge management (PKM) and professional document auditing, prioritizing local privacy and execution reliability.

## 2. Operating Model & Strategy
Ricemaker operates on a **MapReduce** strategy to handle large volumes of data without overwhelming LLM context windows:
* **The Map Phase:** The agent watches an `input` folder. When a file is added, it is normalized to Markdown and reviewed individually. These results are stored in an `intermediate` folder.
* **The Reduce Phase:** A post-processor gathers all intermediate reviews and synthesizes them into a single `master_report.md`.
* **State Persistence:** Every step is tracked in `plan.json` and `history.csv`. If the system restarts, it resumes from the last unfinished task rather than starting over.

## 3. System Architecture

### 3.1 Components
| Component | Technology |
| :--- | :--- |
| **Inference Wrapper** | `LiteLLM` (standardized `provider/model` syntax) |
| **File Watcher** | `watchdog` (OS-level event listening) |
| **Document Extractor** | `MarkItDown` (Microsoft) for PDF, Office, and text |
| **Multimedia Handler** | `Whisper` (via OpenAI SDK) for Audio/Video transcription |
| **Backend API** | `Flask` (Python) serving REST endpoints |
| **Frontend UI** | Vanilla JavaScript + HTML5 (Self-polling dashboard) |

### 3.2 Data Flow
1.  **Ingestion:** User drops a file into the configured `input_folder`.
2.  **Detection:** `WatcherHandler` triggers the `RicemakerAgent`.
3.  **Extraction:** File is converted to Markdown (Docs) or Transcribed (Audio/Video).
4.  **Inference:** `LiteLLM` calls the configured model (e.g., `ollama/llama3` or `google/gemini-1.5-flash`).
5.  **Output Generation:** A Markdown report with Obsidian-compliant YAML frontmatter (including `source` lineage) is saved to the `output_folder`.
6.  **Logging:** Costs and latency are written to `stats.csv` and audit logs to `history.csv`.
7.  **UI Update:** JavaScript frontend polls the Flask API and updates the browser view, separating active queue items from the archive.

## 4. Implementation & Deployment Strategy

### 4.1 Deployment Environment
* **Target:** Docker Desktop on Windows 11 or macOS (M-series/Intel).
* **Resource Strategy:** Use the Host machine's GPU for Ollama to maximize speed and handle large files, while keeping the application logic isolated in Docker.

### 4.2 Docker Configuration
* **Networking:** The container uses `host.docker.internal` to bridge to the Ollama service running on the host OS.
* **Volumes:** Root-level bind mounts (e.g., `/Volumes` and `/Users`) allow the agent to access NAS drives and local iCloud/Obsidian folders directly as defined in `config.json`.

### 4.3 Setup Steps
1.  **Host Config:** Install Ollama on the Mac/Windows host.
2.  **Secrets:** Populate `keys.json` with API keys and `OLLAMA_API_BASE`.
3.  **Config:** Set absolute paths for input/output in `config.json`.
4.  **Build:** Run `docker-compose up --build -d` to initialize the environment.
5.  **Access:** Open `http://localhost:1688` to monitor the agent.

## 5. Technical Requirements & Constraints
* **Lineage Traceability:** Every output `.md` file MUST contain a `source` field in its YAML frontmatter pointing to the original filename.
* **Large Volume Handling:** The UI must separate "Live Queue" (Pending/Processing) from "File Archive" (Completed/Errors) to handle thousands of files efficiently.
* **Path Flexibility:** The system must support absolute paths across mapped volumes (NAS, iCloud, Local).
* **Privacy:** If the model is set to `ollama:*`, no document content should leave the local network.
* **Budget Guardrail:** The system must stop processing if the total cost in `stats.csv` exceeds the `max_budget_usd`.

## 6. Project Manifest (File Structure)
* `agent.py`: The background worker/brain (Watcher + LLM logic).
* `app.py`: Flask REST API serving statuses, files, and reports.
* `static/js/main.js`: Dashboard & Archive UI logic.
* `templates/index.html`: Modern, dual-panel dashboard.
* `config.json`: Master configuration for paths and models.
* `plan.json`: Current session state memory.
* `history.csv`: Permanent audit log of all processed files.

## 7. Outstanding Tasks (from Work Logs)
- [ ] **Multimedia Integration:** Implement Whisper-based transcription for Audio/Video files.
- [ ] **Cost Calculation:** Enhance the stats engine to track USD costs for cloud LLM providers accurately.
- [X] **Settings UI:** Implement a Settings page to modify `config.json` contents directly from the browser (triggering backend restarts).
- [X] **Prompt Template:** Allow for the agent prompt to be configurable based on a template file specified in `config.json`. Restart review after changes are saved.
- [X] **File Archives Re-review:** Allow for completed files in the file archives to be reviewed again.
- [X] **Agent Controls:** Add a dashboard button with four states: start, pause, continue, and stop.
- [X] **Dashboard File Management:** Add a dashboard button to move completed files to archive folder based on the category tag in the YAML frontmatter.
- [X] **Agent Categorization:** Agent must add a category tag to the YAML during analysis.
- [X] **Agent Traceability:** Agent must add the new file location in the YAML after moving the original file.
- [ ] **Search & Filter:** Add search functionality to the File Archive panels.
- [X] **Prioritized Review:** Prioritize the review of files that are newest (based on date modified).
