# Project: Ricemaker (Durable AI File Reviewer)

## 1. Vision
An automated agent that "cooks" raw local files into structured AI insights. It is designed for high-reliability batch processing on Windows/macOS desktops using Docker.

## 2. Architecture
- **Inference:** `LiteLLM` (provider/model) routing to local Ollama or Cloud APIs.
- **Local Engine:** Ollama running on the HOST machine (accessible via `host.docker.internal`).
- **Durable Logic:** - **Watcher:** Real-time monitoring of `/input` via `watchdog`.
    - **Planner:** Checkpoint system using `plan.json`.
    - **Extractor:** `MarkItDown` + `Whisper` (for Audio/PCM) + `OpenCV` (for Video frames).
- **Web UI:** Flask (Backend) + Vanilla JS (Frontend) on Port 5000.

## 3. Deployment Constraints
- **Target:** Docker Desktop (Windows/macOS).
- **Networking:** Must bridge to Host GPU for Ollama.
- **Persistence:** All logs (`stats.csv`), states (`plan.json`), and folders are bind-mounted.

## 4. Feature Requirements
- [x] Recursive Directory Scanning.
- [x] Token Overflow (Recursive Chunking).
- [x] Intermediate Checkpointing (Map Phase).
- [x] Master Summary Generation (Reduce Phase).
- [x] Audio Translation Toggle (.mp3, .wav, .pcm).
- [x] USD Cost & Latency Tracking.
- [ ] Responsive HTML/JS Frontend (Dashboard).

## 5. Next Steps for Gemini CLI
1. Generate `templates/index.html` using a clean, modern CSS layout.
2. Generate `static/js/main.js` to poll `/api/plan` and `/api/stats`.
3. Finalize the `agent.py` "Extractor" class for all 10+ specified file types.

