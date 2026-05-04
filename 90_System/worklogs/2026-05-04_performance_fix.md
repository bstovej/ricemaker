# Work Log: UI & API Performance Optimization
**Date:** 2026-05-04

## Task Overview
The UI became unresponsive after switching backends, primarily due to the growing volume of files in the processing plan (~900 files) and inefficient rendering logic.

## Changes Made
### Frontend Optimization (`static/js/main.js`)
- **Fix:** Refactored `refreshDashboard` to build complete HTML strings for tables *before* updating `innerHTML`. This fixes a severe performance bottleneck where `innerHTML +=` inside a loop was causing the browser to re-parse the entire table DOM hundreds of times every 5 seconds.
- **Polling:** Increased the polling interval from 5 seconds to 10 seconds to reduce the frequency of heavy API calls.

### Backend Optimization (`app.py`)
- **Caching:** Implemented a lightweight caching mechanism for the heaviest API endpoints:
  - `/api/files`: Caches input folder scan results for 10 seconds (critical for slow NAS mounts).
  - `/api/status`: Caches `plan.json` data for 3 seconds.
  - `/api/stats`: Caches CSV statistics for 15 seconds to avoid frequent Pandas imports and file reads.

## Outcome
The UI is now highly responsive even with a large number of files. Browser CPU usage during polling is significantly reduced, and the backend handles requests much more efficiently.

## Next Steps
- Continue monitoring the llama.cpp backend for stability during long-running batch jobs.
