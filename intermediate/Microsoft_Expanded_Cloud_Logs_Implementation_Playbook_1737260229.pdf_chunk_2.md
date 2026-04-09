This document is a technical guide (likely a security playbook) focused on **configuring, verifying, and utilizing Microsoft 365 (M365) audit logs for forensic investigations.** It provides specific instructions on how to track threat actor activity within Exchange Online, SharePoint Online, and Microsoft Teams.

The following are the key insights and facts extracted from the document:

### 1. Configuration and Enablement Requirements
*   **Licensing:** Advanced Auditing requires specific licenses, such as **Microsoft 365 E5** or appropriate add-on licenses.
*   **Manual Activation:** Even with the correct license, "Microsoft 365 Advanced Auditing" may need to be manually enabled within the M365 Admin Center or Entra ID.
*   **The "SearchQuery" Exception:** A critical technical detail is that **`SearchQueryInitiated` logging for both Exchange and SharePoint is disabled by default** and must be manually enabled via PowerShell.
*   **Verification Methods:** Administrators can verify audit settings via the M365 Admin Center, the Entra ID portal, or using Exchange Online PowerShell commands (e.g., `Get-Mailbox | FL *audit*`).

### 2. Critical Forensic Logs & Investigative Value
The document highlights three primary event types in Exchange and one in SharePoint that are vital for detecting and scoping a compromise:

#### **A. `MailItemsAccessed` (Exchange Online)**
This is the most significant event for identifying **data exfiltration.**
*   **Two Access Methods:**
    *   **Sync:** Used by Outlook desktop; indicates entire folders were synced/accessed.
    *   **Bind:** Used by web clients (OWA/IMAP/POP3); records the access of **individual** email messages.
*   **Forensic Use:** Helps investigators establish a "left-right" timeline, determine the scope of compromise (which mailboxes were targeted), and identify threat actor intent.
*   **Throttling Alert:** If more than 1,000 records are generated on a mailbox within 24 hours, logging is throttled for 24 hours. **The document notes that seeing throttling can itself be an indicator of mailbox misuse or compromise.**

#### **B. `Send` (Exchange Online)**
*   **Purpose:** Tracks when a user sends, replies to, or forwards an email.
*   **Forensic Use:** Helps identify if a threat actor has moved from "reconnaissance" (reading emails) to "active operations" (sending phishing emails from a compromised account). It also helps identify the subject lines and recipients of malicious communications.

#### **C. `SearchQueryInitiated` (Exchange & SharePoint)**
*   **Purpose:** Records the actual text typed into the search bar in Outlook or SharePoint.
*   **Forensic Use:** Provides direct insight into **attacker intent.** By analyzing search terms, investigators can determine if the actor was looking for intellectual property, financial data, or specific personnel.
*   **Behavioral Analysis:** Allows for "outlier analysis" (e.g., a user suddenly searching for "payroll" at 3:00 AM from a new device).

#### **D. `MeetingParticipantDetail` (Microsoft Teams)**
*   **Purpose:** Records when participants join and leave Teams meetings.
*   **Forensic Use:** Used for temporal analysis to reconstruct timelines of how a threat actor interacted with a meeting.

### 3. Technical Summary Table for Investigators

| Feature | Key Data Points to Watch | Investigative Value |
| :--- | :--- | :--- |
| **`MailItemsAccessed`** | `ClientIPAddress`, `MailAccessType` (Sync vs. Bind), `AppId` | Identifying data exfiltration and scope of breach. |
| **`Send`** | `Subject`, `InternetMessageID`, `ClientIPAddress` | Identifying phishing campaigns and movement from recon to attack. |
| **`SearchQuery...`** | `QueryText`, `ClientUserAgent`, `ScenarioName` | Determining attacker intent and identifying targeted sensitive information. |
| **`MeetingParticipant`** | Join/Leave timestamps, User IDs | Reconstructing timelines of unauthorized meeting access. |

### 4. Integration & Tooling
*   **SIEM Integration:** The document references the use of **Microsoft Sentinel** and **Splunk** for centralized log management and analysis.
*   **Log Discovery:** Logs can be queried via the **Microsoft Purview portal** (for GUI-based searching) or **Exchange Online PowerShell** (for automated or advanced querying).