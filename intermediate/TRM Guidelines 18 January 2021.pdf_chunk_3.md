This document is an excerpt from the **Monetary Authority of Singapore (MAS) Technology Risk Management Guidelines (January 2021)**. It outlines the regulatory expectations for Financial Institutions (FIs) regarding IT operations, security, and resilience.

Below are the key insights and facts categorized by functional domain.

### 1. Change and Software Release Management
The primary goal is to maintain the stability and integrity of the production environment.
*   **Testing & Approval:** All changes must be tested in a dedicated environment. Test plans require approval from both Business and IT management, and results must be formally signed off before deployment.
*   **Governance:** A **Change Advisory Board (CAB)**, comprising key stakeholders, must be established to prioritize changes based on their security and stability implications.
*   **Risk Mitigation:** FIs must perform backups and establish **rollback plans** prior to any change implementation to revert to a previous state if errors occur.
*   **Emergency Procedures:** While "emergency changes" (e.g., high-priority security patches) may bypass standard processes, FIs must have clearly defined procedures for assessing, approving, and identifying authorizers for these urgent updates.
*   **Segregation of Duties:** In software releases, no single individual should have the authority to develop, compile, and move code between environments. Traceability and integrity of code must be maintained.

### 2. Incident and Problem Management
The focus is on rapid recovery and preventing the recurrence of failures.
*   **Incident Response:** The objective of the incident management framework is to restore services to a secure state as quickly as possible to minimize business and customer impact.
*   **Resource & Evidence Management:** FIs must have sufficient resources (potentially including external forensics) and must ensure that evidence is preserved for investigation.
*   **Communication:** FIs must maintain a communication plan to notify customers and the media, including identifying designated spokespersons.
*   **Problem Management (Root Cause):** Unlike incident management (which focuses on restoration), problem management focuses on identifying the **root cause** and performing **trend analysis** to prevent future incidents.

### 3. IT Resilience and Disaster Recovery (DR)
The guidelines emphasize continuous availability and the ability to recover from significant disruptions.
*   **System Availability:** High-availability systems require redundancy and fault-tolerant solutions. FIs must map internal and external dependencies to identify **single points of failure**.
*   **Recovery Objectives:** FIs must establish and align **Recovery Time Objectives (RTO)** and **Recovery Point Objectives (RPO)** with business requirements.
*   **DR Testing:** Disaster Recovery plans must be tested regularly using various scenarios (e.g., total site failure). These tests must include coordination with third-party service providers.
*   **Backup Strategy:** A complete lifecycle approach is required for backups, including frequency, retention, secure storage (offline/offsite), and the **secure destruction** of data.

### 4. Data Centre (DC) Resilience
Physical and environmental security is as critical as digital security.
*   **Risk Assessment:** FIs must conduct a **Threat and Vulnerability Risk Assessment (TVRA)** for data centers, considering physical threats (fire, flood) and even political/economic climates.
*   **Infrastructure Redundancy:** DCs must have redundant power (UPS, generators), cooling, and network paths to eliminate single points of failure.
*   **Physical Access:** Access to the DC must be on a "need-to-have" basis, with strict controls on visitors, equipment racks, and keys.

### 5. Access Control and Identity Management
The guidelines follow the principle of "Zero Trust" and restricted privilege.
*   **Core Principles:** Access management must adhere to **"Never Alone"** (dual control for sensitive tasks), **"Segregation of Duties,"** and **"Least Privilege"** (access based on job necessity).
*   **Authentication:** **Multi-factor authentication (MFA)** is mandatory for sensitive system functions and all remote access.
*   **Review and Revocation:** FIs must perform periodic access reviews to identify and remove dormant or inappropriate accounts. Access must be revoked immediately upon an employee's change in role or termination.
*   **Remote Access:** All remote connections must be encrypted and conducted only from secured, FI-standard devices.

### 6. Cryptography
Cryptography is viewed as a fundamental tool for confidentiality, integrity, and authenticity.
*   **Standards:** FIs must use well-established international algorithms and appropriate key lengths.
*   **Key Management:** A full lifecycle policy is required (generation, distribution, renewal, revocation, and expiry).
*   **Hardware Security:** Sensitive keys should be stored in **hardened, tamper-resistant systems**, such as Hardware Security Modules (HSMs).
*   **Key Segregation:** To limit impact, cryptographic keys should be used for a single purpose (e.g., do not use the same key for both encryption and digital signatures).