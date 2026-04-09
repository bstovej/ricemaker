# 🌾 Ricemaker
**Durable AI File Reviewer Agent for Mac & Windows (Desktop Edition)**

Ricemaker is a high-reliability "MapReduce" agent that transforms raw local files (PDFs, Office Docs, Audio, Video) into structured AI reviews. Optimized for local inference with **Ollama** and **LiteLLM**, it bridges your local desktop files directly to modern LLMs without sacrificing privacy.

## 🚀 Key Features
- **Watcher Mode:** Real-time monitoring of any local or NAS folder.
- **Obsidian Integration:** Generates Markdown reports with rich YAML frontmatter and file lineage (`source` tracing).
- **Dual-Panel Dashboard:** Separates "Live Queue" (active work) from "File Archive" (thousands of processed items) for efficient batch management.
- **MapReduce Processing:** Handles massive files by chunking them before consolidation.
- **Local Privacy:** Optimized to use your Mac/Windows GPU via Ollama to keep data on your machine.
- **Durable Progress:** Persistent checkpoints (`plan.json` and `history.csv`) ensure zero work is lost on restart.

---

## 🛠️ Installation & Setup

### 1. Prerequisite: Ollama
For local inference, install **Ollama** on your **Host OS**.
- **Download:** [ollama.com](https://ollama.com)
- **Settings:** Ensure `OLLAMA_HOST=0.0.0.0` is set in your environment if using custom network setups (default usually works).

### 2. Prepare Configuration
1. Clone this repository.
2. Edit `keys.json`: Add your `OLLAMA_API_BASE` (e.g., `http://host.docker.internal:11434`) and any Cloud API keys.
3. Edit `config.json`:
   - `input_folder`: Absolute path to your source files (e.g., `/Volumes/NAS/Papers`).
   - `output_folder`: Absolute path to your Obsidian vault or result folder.

### 3. Deploy with Docker
Ricemaker is fully containerized. To start:
```bash
docker-compose up --build -d
```
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
- **Privacy:** Content stays local when using `ollama/*` models.
- **Support:** Handles PDF, DOCX, XLSX, PPTX, TXT, MD, and more via Microsoft `MarkItDown`.
