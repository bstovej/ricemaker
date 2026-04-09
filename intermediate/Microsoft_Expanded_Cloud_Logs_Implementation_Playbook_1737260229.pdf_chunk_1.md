This document is a **CISA Implementation Playbook (January 2025)** designed to guide cybersecurity professionals in leveraging expanded Microsoft cloud logging capabilities to detect and defend against advanced persistent threats (APTs), specifically nation-state actors.

Below are the key insights and facts extracted from the provided segment:

### 1. Strategic Context & Motivation
*   **Response to 2023 Breaches:** The playbook was prompted by a summer 2023 incident where a PRC-backed threat actor (**Storm-0558**) compromised Microsoft Exchange Online. The attackers used a stolen Microsoft Services Account (MSA) key to forge tokens and access high-level U.S. government email accounts.
*   **The Role of Enhanced Logging:** The U.S. Department of State was only able to detect the 2023 intrusion because they possessed **Microsoft Purview Audit (Premium)**, which provided specific `MailItemsAccessed` telemetry that standard logs lacked.
*   **Objective:** To transition these advanced "Premium" level logs from a luxury available only to high-tier subscribers to a standard capability available to all organizations with **E3/G5 licenses**, enabling broader "defense-in-depth."

### 2. Key Technical Changes to Microsoft Services
*   **Expansion of Log Access:** Microsoft has expanded access to enhanced logs (previously restricted to "Premium" subscribers) to all commercial customers with **E3/G3 licenses and above**.
*   **Increased Retention:** The default retention period for Microsoft Purview Audit (Standard) has been increased from **90 days to 180 days**.
*   **Scope of Workloads:** The playbook focuses on three primary pillars of the M365 ecosystem:
    *   **Microsoft Exchange** (e.g., tracking mail access and sent items).
    *   **Microsoft SharePoint Online** (e.g., monitoring search activity and file access).
    *   **Microsoft Teams** (e.g., determining the impact of a compromise through user interactions).

### 3. Operational Intelligence & Detection Capabilities
The expanded logs are intended to move beyond mere compliance and into **active threat hunting**. Key detection scenarios mentioned include:
*   **Credential Access:** Detecting when an attacker accesses specific mail items after compromising an identity.
*   **Data Exfiltration:** Identifying anomalous search activity in SharePoint that suggests an attacker is "scoping" the environment for sensitive data.
*   **Impact Assessment:** Using Teams interaction logs to determine how far an attacker moved laterally or what information they may have gathered through chat.

### 4. Implementation & Integration
*   **Target Audience:** Technical personnel responsible for log collection, SIEM (Security Information and Event Management) integration, and incident response.
*   **SIEM Integration:** The playbook provides specific guidance on ingesting these expanded logs into **Microsoft Sentinel** and **Splunk**.
*   **Required Permissions:** To effectively use these logs, administrators must configure specific **Entra ID** roles (e.g., Security Reader, Audit Reader, or Compliance Administrator) and ensure the logs are flowing into the Unified Audit Log (UAL).

### Summary Fact Sheet
| Feature | Previous State | New/Expanded State |
| :--- | :--- | :--- |
| **Log Availability** | Limited to "Audit Premium" users | Available to **E3/G3** and above |
| **Retention (Standard)** | 90 Days | **180 Days** |
| **Primary Threat Focus** | Identity-based intrusion | Advanced nation-state/APT detection |
| **Key Log Sources** | Basic operational logs | `CloudAppEvents`, `MailItemsAccessed`, SharePoint/Teams telemetry |