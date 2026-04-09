This document is an excerpt from the **Monetary Authority of Singapore (MAS) Technology Risk Management Guidelines (January 2021)**. It outlines the regulatory expectations for Financial Institutions (FIs) regarding technology risk, software development, and IT service management.

Below are the key insights and facts extracted from the document.

### Key Insights

*   **Security-by-Design is Mandatory:** Security is not a final "check-box" at the end of a project; it must be integrated into every phase of the System Development Life Cycle (SDLC), including requirements, design, testing, and even in modern methodologies like Agile and DevSecOps.
*   **Holistic Risk Ownership:** Risk management is not just about identifying threats (like malware or sabotage) but also about managing the *residual risk* (the risk remaining after controls are applied) and determining the authority levels for risk acceptance.
*   **Third-Party & Ecosystem Governance:** A significant portion of the guidelines focuses on the risks introduced by external entities. This includes vendor selection, the security of third-party service providers, the use of open-source code, the management of APIs, and the oversight of "Shadow IT" (unmanaged end-user computing).
*   **Proactive Lifecycle Management:** The guidelines emphasize the importance of preventing "technical debt" and security gaps by proactively managing the end-of-support (EOS) dates for hardware and software through technology refresh plans.
*   **Integration of Automation (DevSecOps):** The document recognizes modern development trends, stating that while DevSecOps introduces automation and speed, it must still adhere to traditional IT service management (ITSM) and security principles, particularly regarding the segregation of duties.

---

### Key Facts

#### 1. Technology Risk Management Framework
*   **Risk Owner:** Can be an individual, a function, or a group of functions within the FI.
*   **Core Components:** Must include risk identification, assessment, treatment, and monitoring/reporting.
*   **Assessment Criteria:** Risk assessments must consider financial, operational, legal, reputational, and regulatory impacts.
*   **Reporting:** Significant risks must be reported to the Board of Directors and Senior Management.
*   **Risk Treatment:** FIs should consider insurance as a method to reduce the financial impact of technology risks.

#### 2. IT Project Management & SDLC
*   **Project Steering Committee:** Required for large and complex projects to provide oversight and handle escalations.
*   **System Acquisition:** FIs should use source code escrow agreements for critical software to ensure access if a vendor fails.
*   **Testing Requirements:** Testing must cover business logic, security, and performance (stress/load). FIs must maintain separate environments for unit, integration, and user acceptance testing (UAT).
*   **Quality Assurance:** An independent function should perform quality assurance to ensure compliance with internal policies.

#### 3. Software Development & APIs
*   **Secure Coding:** Standards must cover input validation, cryptography, authentication, and error handling.
*   **API Security:** FIs must implement a vetting process for third parties connecting via APIs, use encryption for sensitive data, and implement mechanisms to revoke API keys/tokens in the event of a breach.
*   **Shadow IT:** Business users developing their own applications (end-user computing) must be monitored and assessed for risk.

#### 4. IT Service Management (ITSM)
*   **Configuration Management:** FIs must maintain accurate, up-to-date information on all hardware and software components.
*   **Patch Management:** Patches must be tested before being applied to production environments to prevent system instability.
*   **Technology Refresh:** Using outdated/unsupported hardware or software is discouraged; if used, it requires formal management dispensation and a risk assessment.
*   **Change Management:** All changes to information assets must undergo risk/impact analysis, testing, and formal approval.