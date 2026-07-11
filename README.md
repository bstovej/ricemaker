# Ricemaker (v0.2.2, 2026-07-10)
**Durable AI File Reviewer Agent for Mac & Windows (Desktop Edition)**


Ricemaker is a high-reliability "MapReduce" agent that transforms raw local files (PDFs, Office Docs, Audio, Video) into structured AI reviews. Optimized for local inference with **llama.cpp** and **LiteLLM**, it bridges your local desktop files directly to modern LLMs without sacrificing privacy.

## 🚀 Key Features
- **Watcher Mode:** Real-time monitoring of any local or NAS folder.
- **Obsidian Integration:** Generates Markdown reports with rich YAML frontmatter and file lineage (`source` tracing).
- **Dual-Panel Dashboard:** Separates "Live Queue" (active work) from "File Archive" (thousands of processed items) for efficient batch management.
- **MapReduce Processing:** Handles massive files by chunking them before consolidation.
- **Local Privacy:** Optimized to use your Mac/Windows GPU via llama.cpp to keep data on your machine.
- **Durable Progress:** Persistent checkpoints (`data/plan.json` and `data/history.csv`) ensure zero work is lost on restart.

---

## 🏁 Getting Started

### 1. Clone the Repository
Open your terminal (macOS/Linux) or PowerShell/Command Prompt (Windows) and run the following commands to clone the repository to your local machine:

**macOS / Linux:**
```bash
git clone https://github.com/bstove/ricemaker.git
cd ricemaker
```

**Windows:**
```powershell
git clone https://github.com/bstove/ricemaker.git
cd ricemaker
```

### 2. Configuration
The system relies on JSON configuration files that are ignored by Git for security and local flexibility. Use the provided sample files as a starting point:

1. **Copy the samples:**
   ```bash
   cp sample_keys.json keys.json
   cp sample_config.json config.json
   ```
2. **Edit `keys.json`** with your API keys and local backend bases (e.g., `LLAMA_CPP_API_BASE`, `OLLAMA_API_BASE`).
3. **Edit `config.json`** to define your local folder paths (absolute paths recommended), selected `llm_provider` (`llama_cpp` or `ollama`), model names, and batch category.

> **Note on Archiving:** When files are archived, they are moved to tag-based subfolders inside the `archive_folder` for easier retrieval and structured organization.

> **Note on Windows Paths:** In `config.json`, use forward slashes (e.g., `C:/Users/name/input`) or escaped backslashes (`C:\\Users\\name\\input`).

### 3. Docker Deployment
Ricemaker is designed to run in Docker while bridging to your host machine's local LLM instances.

#### Prepare Docker Configuration
1. **Copy the sample:**
   ```bash
   cp sample_docker-compose.yaml docker-compose.yaml
   ```
2. **Edit `docker-compose.yaml`** to ensure your host directories (like `/Users/your-user`) are correctly mapped so the agent can access your files.

#### Build the System
If this is your first time or you've made changes to the code:
```bash
docker-compose build
```

#### Run the System
Start the agent and the dashboard in the background:
```bash
docker-compose up -d
```

#### Monitor Logs
To see the agent's real-time analysis logs:
```bash
docker-compose logs -f ai-agent
```

#### Stop the System
```bash
docker-compose down
```

### 4. Hardware Acceleration (Local LLMs)
To use your local GPU for llama.cpp or Ollama, ensure the corresponding service is running on your **Host OS** (not inside Docker). The `docker-compose.yaml` file uses `host.docker.internal` to bridge the container's requests back to your machine's hardware.

---

Access the dashboard at: `http://localhost:1688`

---

## Audio/Video Transcription

Ricemaker supports local Speech-to-Text (STT) transcription for audio and video files.

### 1. Default (Whisper Model)
By default, Ricemaker is configured to use a local Whisper model served via Ollama:
- **Model:** `karanchopda333/whisper:latest` (or any other Whisper model)
- **Routing:** Automatically resolves through Ollama's `/v1` compatibility layer if `llm_provider` is set to `ollama`.

### 2. Alternative (Gemma 4 Multimodal STT)
As an alternative to Whisper, you can use Google's native multimodal audio model **Gemma 4** (`e2b` or `e4b` variants) running in Ollama to transcribe directly:
1. Pull the Gemma 4 variant on your host machine:
   ```bash
   ollama pull gemma4:e2b
   ```
2. Update your `config.json` to define the target model under the `"whisper_model"` parameter:
   ```json
   "whisper_model": "gemma4:e2b"
   ```

---

## 📁 File Structure & Lineage
Ricemaker maintains a clean record of its operations:
- **`input_folder`**: Raw files to be reviewed.
- **`output_folder`**: Final `.md` reports with frontmatter.
- **`intermediate/`**: Raw AI chunks before consolidation.
- **`data/`**: Persistent state memory, audit logs, and metrics.
- **`data/history.csv`**: Permanent audit log of original paths vs. summary paths.

---

## ⚖️ License & Constraints
- **Reliability:** Built for high-volume batch processing.
- **Privacy:** Content stays local when using local models (e.g., `openai/llama-cpp`).
- **Support:** Handles PDF, DOCX, XLSX, PPTX, TXT, MD, and more via Microsoft `MarkItDown`.

---

## Changelog

### v0.2.2 (2026-07-10)
- Implemented structured error logging that captures detailed traceback stack traces, active model, and exception details to a CSV format.
- Standardized error log filenames to `ricemaker_error_log_<date_time_started>.csv`.
- Made the error log destination folder configurable via the new `"error_log_path"` key in `config.json` (defaults to the output folder path).
- Added `libreoffice` and `easyocr` dependencies to the Docker setup to enable legacy file translation and scanned PDF fallback OCR out of the box.
- Bypassed hard Flask crashes on startup when keys/config files are missing, allowing the web service to launch and report diagnostic connection/configuration failures directly inside a dynamic dashboard banner.
- Updated UI layout for Dashboard and File Archives sections

### v0.2.1 (2026-07-09)
- Added support for switching between llama.cpp server and Ollama local LLM models via `llm_provider` configuration.
- Configured dedicated local endpoint bases (`LLAMA_CPP_API_BASE` and `OLLAMA_API_BASE`) in `keys.json`.
- Updated background agent routing logic to dynamically prepend model prefixes and map endpoints.
- Updated documentation across prd.md and README.md.
