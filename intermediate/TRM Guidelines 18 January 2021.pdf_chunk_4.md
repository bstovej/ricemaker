This document is an excerpt from the **Monetary Authority of Singapore (MAS) Technology Risk Management Guidelines (January 2021)**. It outlines the regulatory expectations for Financial Institutions (FIs) regarding cybersecurity, data protection, and infrastructure resilience.

Below are the key insights and facts categorized by functional area:

### 1. Data Security & Protection
*   **Lifecycle Management:** FIs must protect data in three states: **in motion** (network transit), **at rest** (storage/endpoints), and **in use** (processing). 
*   **Data Loss Prevention (DLP):** FIs are required to implement policies to detect and prevent unauthorized access, modification, or transmission of confidential data.
*   **Production vs. Non-Production:** The use of sensitive production data in non-production environments is restricted. If necessary, it requires senior management approval and must be **masked** or strictly controlled to prevent leakage.
*   **Disposal:** Confidential data must be **irrevocably deleted** from all media and devices before they are disposed of or redeployed.
*   **Cryptographic Integrity:** 
    *   Expired or revoked keys must be destroyed securely so they are unrecoverable.
    *   New keys must be generated such that they cannot be derived from previous keys (cryptographic independence).
    *   Backups of keys are mandatory to recover from corruption or accidental deletion.

### 2. Network & Infrastructure Security
*   **Segmentation & Control:** FIs should use network segmentation (based on system criticality or data sensitivity) to prevent **lateral movement** by attackers and mitigate insider threats.
*   **Perimeter Defense:** Use of firewalls, Intrusion Prevention Systems (IPS), and Network Access Controls (NAC) is required to block malicious traffic and unauthorized devices.
*   **Web & Internet Security:** To reduce the attack surface, FIs should consider isolating internet web browsing from core endpoint devices.
*   **DoS Protection:** Robust protection against Denial of Service (DoS) attacks (including volumetric and application-layer attacks) is mandatory.
*   **IoT Management:** FIs must maintain an inventory of all Internet of Things (IoT) devices. Because these devices often lack native security, they should be hosted in **separate network segments** to prevent them from being used as launchpads for attacks.

### 3. System & Endpoint Security
*   **Configuration Standards:** FIs must establish and periodically review security configurations for all hardware and software to minimize exposure.
*   **Malware Defense:** Implementation of both **signature-based** and **behavior-based** endpoint protection is required. Anti-malware signatures must be kept up to date.
*   **Application Control:** FIs should use **application whitelisting** to ensure only authorized software is installed.
*   **BYOD (Bring Your Own Device):** Using personal devices for corporate access requires a comprehensive risk assessment and specific security measures.
*   **Virtualization Risks:** FIs must recognize the "contagion" risk (where a breach in one Virtual Machine affects others) and implement strong access controls on hypervisors and host operating systems.

### 4. Cyber Security Operations (SOC)
*   **Intelligence-Led Defense:** FIs should establish processes to collect and analyze cyber threat intelligence and actively participate in information-sharing arrangements within the financial ecosystem.
*   **Monitoring & Detection:**
    *   FIs should establish a **Security Operations Centre (SOC)** or use managed services.
    *   Continuous monitoring of system logs is required, and logs must be protected from unauthorized access.
    *   FIs should establish **baselines** of normal activity and use **User Behavioural Analytics (UBA)** or machine learning to identify anomalies.
*   **Incident Response:** FIs must have a formal incident response plan to isolate threats and resume services. This plan must include a "lessons learned" process to improve future defenses.

### 5. Cybersecurity Assessment & Testing
*   **Vulnerability Assessment (VA) vs. Penetration Testing (PT):**
    *   **VA:** Regular, frequency-based checks for known vulnerabilities.
    *   **PT:** In-depth evaluations using **blackbox** and **greybox** methods. For Internet-facing systems, PT must be conducted at least **annually**.
*   **Advanced Testing:** FIs are encouraged to use **Bug Bounty programs** and conduct **Adversarial Attack Simulations (Red Teaming)** to test defenses against real-world attacker tactics.
*   **Cyber Exercises:** FIs should conduct regular scenario-based exercises, such as **Table-top exercises**, **Social Engineering simulations**, and **Cyber Range** exercises, to validate response and communication plans.
*   **Remediation:** A formal process must exist to track and resolve findings from assessments, including severity classification and remediation timelines.

### 6. Online Financial Services
*   **Attack Vector Mitigation:** FIs must implement controls against common web attacks, including **SQL injection, Cross-Site Scripting (XSS), Man-in-the-Middle (MITM), and DNS hijacking.**
*   **Mobile Security:** FIs must address risks unique to mobile applications and ensure software is only distributed through **official app stores** or secure channels.