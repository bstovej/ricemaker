# Work Log: Error Management & Missing File Purging
**Date:** 2026-05-04

## Task Overview
Improved the "Re-review All" functionality to handle cases where files that previously errored have been manually deleted from the input folder.

## Changes Made
### Backend API (`app.py`)
- **Updated `rereview_errors`**: 
    - Added a file existence check for every entry in the error list.
    - If the file exists: It is reset to "pending" as before.
    - If the file is missing: It is automatically passed to `_purge_file_data`, which removes it from `plan.json`, `history.csv`, and deletes its `intermediate/` data.
    - Changed the return format to provide separate counts for `reset_count` and `purged_count`.

### Frontend UI (`static/js/main.js`)
- **Updated `rereviewAllErrors`**:
    - Updated the confirmation message to warn that missing files will be removed.
    - Updated the result alert to show how many files were reset and how many were purged.

## Outcome
The "Re-review All" button now serves as an intelligent cleanup tool. It tries to re-process files that are still present and automatically wipes the records of files that the user has already manually removed, keeping the dashboard clean.

## Next Steps
- Monitor the counts in the alert box to ensure they match user expectations.
