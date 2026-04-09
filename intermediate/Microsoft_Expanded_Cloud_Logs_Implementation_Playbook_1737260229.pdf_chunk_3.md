This document is a technical forensic guide focused on using **Microsoft Teams audit logs and Graph API event data** to detect, investigate, and profile threat actor (TA) activity. The primary goal of the text is to demonstrate how specific metadata can be used to reconstruct timelines, identify compromised identities, and uncover automated "scraping" or intelligence-gathering techniques.

Below are the key insights and facts categorized by investigative utility.

### 1. Core Investigative Objectives
The document outlines three primary ways investigators can use Teams logs to identify malicious activity:
*   **Temporal Analysis:** Using timestamps (e.g., `InviteTime`, `JoinTime`, `CreationTime`) to build a timeline of when a threat actor accessed information and to correlate Teams activity with other logs (like `MailItemsAccessed`).
*   **Infrastructure & Tool Profiling:** Using `ClientIP`, `UserAgent`, `DeviceID`, and `ClientAppId` to identify the specific tools (e.g., Graph Explorer) and network infrastructure used by the attacker.
*   **Behavioral Analysis:** Distinguishing between **passive intelligence collection** (e.g., joining a meeting to listen) and **active interaction** (e.g., sending messages or updating messages to spread disinformation).

### 2. Key Event Analysis & Indicators
The document breaks down specific "Events" that occur within the Teams/Graph API ecosystem:

| Event Type | Forensic Value | Specific Threat Indicator |
| :---            | :--- | :--- |
| **MeetingParticipantDetail** | Identifies who was present and for how long. | Identifying unauthorized participants; detecting if an actor joined a meeting using info stolen via email. |
| **MessageSent** | Tracks outgoing communications and identifies external users. | Detecting a shift from "data collection" to "active interaction" with users; identifying use of guest/federated accounts. |
| **MessagesListed** | Monitors the viewing of chat threads via API. | **High volume** of these requests is a primary indicator of **automated scripting/scraping** via the Graph API. |
| **MessageUpdated** | Tracks edits to existing messages. | Identifying **disinformation campaigns** or data manipulation where an actor changes the content of a message. |
| **ChatRetrieved** | Records when a chat thread is accessed via API. | Identifying "mass collection" or "scraping" of entire chat histories by automated tools. |
| **MessageRead** | Tracks the reading of specific, individual messages. | Identifying **targeted intelligence collection** (near-real-time harvesting of specific sensitive messages). |
| **MessageHostedContentRead** | Tracks access to code snippets or images. | Identifying attempts to steal **embedded secrets** (e.g., credentials hidden in code snippets). |

### 3. Critical Forensic Metadata (The "Smoking Guns")
The text highlights specific fields that are essential for a successful investigation:
*   **`ClientAppId` & `ClientAppName`:** Essential for identifying whether the actor is using a standard interface or a malicious script/automation tool (like Graph Explorer).
*   **`ClientIP` & `UserAgent`:** Critical for identifying the geographical origin and the technical environment (OS/Device) of the attacker.
*   **`ParticipantInfo` (HasForeignTenantUsers/HasGuestUsers):** Vital for understanding the scope of information exposure to external or unauthenticated parties.
*   **`InviteTime` vs. `JoinTime`:** Comparing these allows investigators to see if an actor used intercepted meeting invites to gain access.

### 4. Notable Technical Distinctions
*   **Hosted Content vs. Attachments:** The document clarifies that `MessageHostedContentRead` applies to things like code snippets and images embedded in messages, but **not** to file attachments (which are stored in SharePoint or OneDrive).
*   **Graph API Triggering:** Several events (like `MessageSent` or `MessagesListed`) are specifically noted to be triggered when the **Graph API** is used, making this a key area for detecting programmatic/automated attacks.
*   **Threat Actor Motivation:** The document notes that attackers specifically target **user identities** (T1586) because humans are the "weakest link" and because identity compromise provides high ROI for the attacker.