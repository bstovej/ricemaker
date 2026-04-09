This document is an excerpt from the **Monetary Authority of Singapore (MAS) Technology Risk Management Guidelines (January 2021)**. It outlines the regulatory expectations and best practices for Financial Institutions (FIs) regarding cybersecurity, customer authentication, fraud prevention, and technical auditing.

Below are the key insights and facts categorized by functional area:

### 1. Customer Authentication and Transaction Integrity
The guidelines emphasize a multi-layered approach to securing user identities and sensitive actions:
*   **Multi-Factor Authentication (MFA):** FIs must deploy MFA for online services, utilizing at least two of three factors: *Knowledge* (password/PIN), *Possession* (OTP generator), and *Inherence* (biometrics).
*   **Transaction Signing:** For high-risk activities—such as changing contact details, registering new payees, or high-value fund transfers—FIs should implement digital signatures to ensure data integrity.
*   **Biometric Security:** Biometric data and credentials must be encrypted during both storage and transmission. The performance of these systems must be calibrated using the **False Acceptance Rate (FAR)** and **False Rejection Rate (FRR)** relative to the transaction risk.
*   **Session Management:** FIs must implement measures to detect and terminate hijacked sessions and must enforce automatic session timeouts after periods of inactivity.
*   **Soft Tokens:** When using software-based 2FA, FIs must implement "device binding" (linking a user to a specific device) and block access from rooted or jailbroken devices.

### 2. Fraud Monitoring and Phishing Prevention
FIs are expected to be proactive rather than reactive in the face of cyber threats:
*   **Real-Time Monitoring:** FIs must implement real-time systems to identify and block suspicious patterns (e.g., transactions deviating from usual behavior or logins from geographically impossible locations).
*   **Phishing Defense:** FIs should actively monitor for phishing campaigns, report malicious content to service providers for removal, and alert customers to ongoing threats.
*   **Customer Notification:** FIs must notify customers of suspicious activities above defined thresholds, providing clear instructions on how to report unauthorized transactions.

### 3. Application and Infrastructure Security
The document provides specific technical mandates for software development and device management:
*   **Mobile App Security:** To prevent malware and data leakage, mobile apps should:
    *   Avoid caching sensitive data on the device.
    *   Implement anti-tampering, anti-hooking, and code obfuscation.
    *   Use **Certificate/Public Key Pinning** to prevent Man-in-the-Middle (MITM) attacks.
    *   Use secure in-app keypads to mitigate keystroke logging.
*   **Application Security Testing (AST):** FIs should use various testing methods within the Software Development Life Cycle (SDLC):
    *   **SAST (Static):** Analyzing source code/binaries for flaws.
    *   **DAST (Dynamic):** Testing the application in its running state.
    *   **IAST (Interactive):** A hybrid of SAST and DAST.
    *   **Fuzzing:** Using random data input to discover bugs.
*   **BYOD (Bring Your Own Device) Security:** For personal devices accessing FI assets, FIs should use **MDM (Mobile Device Management)**, **MAM (Mobile Application Management)**, or **Virtualization** to prevent data leakage and enforce encryption and "remote wipe" capabilities.

### 4. Governance and IT Audit
The guidelines establish the "checks and balances" required for institutional oversight:
*   **Independent Oversight:** The IT Audit function must provide an independent and objective opinion to the Board of Directors and Senior Management regarding the effectiveness of risk management.
*   **Audit Scope and Frequency:** Audits must cover all IT operations and processes. The frequency of audits should be determined by the criticality and risk level of the specific IT asset or function.
*   **Competency:** FIs are responsible for ensuring that IT auditors possess the necessary skills and technical competency to evaluate complex technology risks.

### Summary of Key Definitions
*   **Rooted/Jailbroken Device:** A device with bypassed security restrictions, making it highly susceptible to malware.
*   **Device Binding:** A technique to link an authorized user to a specific registered device to ensure accountability.
*   **Maker-Checker:** A control process (often used in corporate banking) where one person initiates a transaction and another authorizes it.