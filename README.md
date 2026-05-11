# 🌾 Ricemaker
**Durable AI File Reviewer Agent for Mac & Windows (Desktop Edition)**

Ricemaker is a high-reliability "MapReduce" agent that transforms raw local files (PDFs, Office Docs, Audio, Video) into structured AI reviews. Optimized for local inference with **llama.cpp** and **LiteLLM**, it bridges your local desktop files directly to modern LLMs without sacrificing privacy.

## 🚀 Key Features
- **Watcher Mode:** Real-time monitoring of any local or NAS folder.
- **Obsidian Integration:** Generates Markdown reports with rich YAML frontmatter and file lineage (`source` tracing).
- **Dual-Panel Dashboard:** Separates "Live Queue" (active work) from "File Archive" (thousands of processed items) for efficient batch management.
- **MapReduce Processing:** Handles massive files by chunking them before consolidation.
- **Local Privacy:** Optimized to use your Mac/Windows GPU via llama.cpp to keep data on your machine.
- **Durable Progress:** Persistent checkpoints (`plan.json` and `history.csv`) ensure zero work is lost on restart.

---

## 🏁 Getting Started

### 1. Clone the Repository
Open your terminal (macOS/Linux) or PowerShell/Command Prompt (Windows) and run the following commands to clone the repository to your local machine:

**macOS / Linux:**
```bash
git clone https://github.com/your-username/ricemaker.git
cd ricemaker
```

**Windows:**
```powershell
git clone https://github.com/your-username/ricemaker.git
cd ricemaker
```

### 2. Configuration
The system relies on JSON configuration files that are ignored by Git for security and local flexibility. Use the provided sample files as a starting point:

1. **Copy the samples:**
   ```bash
   cp sample_keys.json keys.json
   cp sample_config.json config.json
   ```
2. **Edit `keys.json`** with your API keys and endpoint configuration.
3. **Edit `config.json`** to define your local folder paths (absolute paths recommended), default model, and batch category.

> **Note on Archiving:** When files are archived, they are moved to a flat structure inside the `archive_folder` for easier retrieval and searching.

> **⚠️ Note on Windows Paths:** In `config.json`, use forward slashes (e.g., `C:/Users/name/input`) or escaped backslashes (`C:\\Users\\name\\input`).

### 3. Docker Deployment
Ricemaker is designed to run in Docker while bridging to your host machine's llama.cpp instance.

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
To use your local GPU for llama.cpp, ensure **llama.cpp** is running on your **Host OS** (not inside Docker). The `docker-compose.yaml` file uses `host.docker.internal` to bridge the container's requests back to your machine's hardware.

---

Access the dashboard at: `http://localhost:1688`

---

## 📁 File Structure & Lineage
Ricemaker maintains a clean record of its operations:
- **`input_folder`**: Raw files to be reviewed.
- **`output_folder`**: Final `.md` reports with frontmatter.
- **`intermediate/`**: Raw AI chunks before consolidation.
- **`history.csv`**: Permanent audit log of original paths vs. summary paths.

---

## ⚖️ License & Constraints
- **Reliability:** Built for high-volume batch processing.
- **Privacy:** Content stays local when using local models (e.g., `openai/llama-cpp`).
- **Support:** Handles PDF, DOCX, XLSX, PPTX, TXT, MD, and more via Microsoft `MarkItDown`.
