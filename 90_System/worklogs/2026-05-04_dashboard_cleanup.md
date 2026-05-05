# Work Log: Dashboard Master Report Cleanup
**Date:** 2026-05-04

## Task Overview
Ensured that purged master reports no longer clutter the "Master Summaries (MOCs)" section of the dashboard, even though the actual `.md` files are preserved in the output folder.

## Changes Made
### Backend API (`app.py`)
- **Updated `summary` endpoint**: 
    - Added logic to scan `plan.json` for all active `session_id` tags.
    - When generating the list of available master reports, the system now extracts the session ID from each `master_report_{sid}.md` file found in the output directory.
    - A report is only included in the dashboard's list if at least one file associated with that session is still present in the plan.
    - Legacy `master_report.md` (no session ID) is explicitly preserved to ensure older reports remain accessible if they haven't been migrated.

## Outcome
The dashboard now only displays "active" processing sessions. Once a session is purged (clearing the tracking data and intermediate chunks), it automatically disappears from the Ricemaker UI, while the permanent record remains untouched in your Notes/Obsidian vault.

## Next Steps
- None. This completes the requested file management enhancements.
