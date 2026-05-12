ricemaker/
├── app.py              # Flask Web Server & API
├── agent.py            # The "Ricemaker" Engine (Watcher + LiteLLM logic)
├── GEMINI.md           # Project Context for Gemini CLI
├── config.json         # Folders, Model ID, and Budget
├── keys.json           # API Keys (Git-ignored)
├── prompts.json        # System and Post-Processor Prompts
├── data/               # Persistent state and logs
│   ├── plan.json       # State Tracker
│   ├── history.csv     # Audit Log
│   └── stats.csv       # Token/Cost Metrics
├── Dockerfile          # Desktop-optimized Build
├── docker-compose.yaml # Local Desktop Orchestration
├── templates/
│   └── index.html      # Frontend Dashboard
└── static/
    └── js/
        └── main.js     # Frontend Fetch/Polling logic

