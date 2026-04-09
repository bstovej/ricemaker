ricemaker/
├── app.py              # Flask Web Server & API
├── agent.py            # The "Ricemaker" Engine (Watcher + LiteLLM logic)
├── GEMINI.md           # Project Context for Gemini CLI
├── config.json         # Folders, Model ID, and Budget
├── keys.json           # API Keys (Git-ignored)
├── prompts.json        # System and Post-Processor Prompts
├── plan.json           # Persistent State Tracker
├── stats.csv           # Performance & Cost Logs
├── requirements.txt    # Python Dependencies
├── Dockerfile          # Desktop-optimized Build
├── docker-compose.yaml # Local Desktop Orchestration
├── templates/
│   └── index.html      # Frontend Dashboard
└── static/
    └── js/
        └── main.js     # Frontend Fetch/Polling logic

