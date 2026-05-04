# Work Log: LLM Backend Transition (Ollama -> llama.cpp)
**Date:** 2026-05-04

## Task Overview
Transition the Ricemaker agent's local LLM backend from Ollama (port 11434) to a llama.cpp server (port 8080).

## Changes Made
- **Config & Keys:**
  - Modified `keys.json`: Replaced `OLLAMA_API_BASE` with `LLAMA_CPP_API_BASE` set to `http://host.docker.internal:8080/v1`.
  - Modified `config.json`: Updated `model_name` and `secondary_model_name` to use the `openai/` prefix for LiteLLM routing.
- **Core Engine (`agent.py`):**
  - Refactored `RicemakerAgent.__init__` to load the llama.cpp API base.
  - Updated `_call_llm` to use LiteLLM's OpenAI-compatible completion call when the model name starts with `openai/`.
  - Removed Ollama-specific parameters (`num_ctx`) and syntax conversions.
  - Updated the startup connection test to verify reachability via the `/v1/models` endpoint.
- **Infrastructure:**
  - Updated `docker-compose.yaml` comments to reflect the llama.cpp bridge.
- **Documentation:**
  - Exhaustively replaced "Ollama" references with "llama.cpp" in `README.md` and `prd.md`.
  - Updated example configurations and port numbers in documentation.

## Outcome
The system is now configured to perform all local LLM inference through the llama.cpp server. The bridge between the Docker container and the host machine is maintained via `host.docker.internal`.

## Next Steps
- Ensure the llama.cpp server is running on the host at port 8080 with the `--api` flag enabled.
- Verify processing with a sample file in the `input/` folder.
