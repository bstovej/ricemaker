This document segment provides a detailed forensic timeline and technical analysis of the 2017 Equifax data breach. The following key insights and facts are categorized by the stages of the attack and the underlying security failures.

### 1. The Root Cause: Unpatched Vulnerability
*   **The Entry Point:** The attackers gained access to Equifax’s network via a known vulnerability in the **Apache Struts** software (CVE-2017-5638) located in the "ACIS" system.
*   **Failure of Detection:** Although US-CERT and other entities had alerted organizations to this vulnerability, and Equifax had implemented some patches, the specific instance of the software remained unpatched. 
*   **Failed Scanning:** Equifax ran scans that failed to identify the vulnerability. The document notes that "internal scans were not effective" in finding the flaw.

### 2. Critical Security Failures (The "Chain of Exploitation")
The document highlights a cascading series of security lapses that allowed a single vulnerability to turn into a massive breach:
*   **Expired SSL Certificates:** A major contributor to the lack of visibility was an **expired SSL certificate** on a security appliance. This prevented the company from inspecting encrypted traffic for malicious activity for an extended period.
*   **Lack of Network Segmentation:** Once inside, the attackers were able to move laterally from the initial entry point to other parts of the network because the systems were not sufficiently isolated.
*   **Failure of Integrity Monitoring:** The company failed to use "file integrity monitoring" to detect when attackers modified system files or installed web shells.
*   **Inadequate Monitoring/Visibility:** Because the SSL certificate for the monitoring tool had expired, the security team was "blind" to the encrypted traffic used by the attackers.
*   **Unencrypted Credentials/Sensitive Data:** The attackers were able to find and use credentials to access other databases, and sensitive data was stored without adequate encryption.

### 3. The Mechanics of the Breach
*   **Timeline of Attack:** The breach was active for a significant period. The attackers used "web shells" (malicious scripts) to maintain access and move through the network.
*   **Data Exfiltration:** The attackers successfully accessed multiple databases, including those containing sensitive personally identifiable information (PII), and exfiltrated large amounts of data.
*   **Detection Timeline:** The breach was eventually discovered not through an automated alert, but when the company updated its expired SSL certificate, which finally allowed the security tools to inspect the traffic and see the malicious activity.

### 4. Key Technical Findings
*   **Vulnerability:** Apache Struts (CVE-2017-5638).
*   **Method of Attack:** Exploitation of a web vulnerability $\rightarrow$ installation of web shells $\rightarrow$ lateral movement $\rightarrow$ credential theft $\rightarrow$ data exfiltration.
*   **Detection Gap:** The "blind spot" created by the expired certificate was the primary reason the attackers remained undetected while exfiltrating data.

### Summary Table of Failures
| Category | Specific Failure | Consequence |
| :--- | :---_ | :_|
| **Patch Management** | Failed to patch Apache Struts | Provided the initial entry point for attackers. |
| **Certificate Management** | Expired SSL/TLS certificate | Created a "blind spot," preventing inspection of encrypted traffic. |
| **Network Security** | Lack of segmentation | Allowed attackers to move from the web server to sensitive databases. |
| **Identity Management** | Compromised credentials | Allowed attackers to masquerade as legitimate users/processes. |
| **Security Monitoring** | Lack of file/integrity monitoring | Prevented the detection of unauthorized software (web shells) on servers. |