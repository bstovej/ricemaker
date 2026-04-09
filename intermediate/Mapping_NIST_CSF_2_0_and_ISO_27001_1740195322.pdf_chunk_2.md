This document is a technical mapping between two major cybersecurity frameworks: **NIST CSF 2.0** (Cybersecurity Framework) and **ISO/IEC 27001:2022**. It is designed to help organizations align their strategic security objectives (NIST) with specific, actionable security controls (ISO).

### Key Insights

*   **Strategic Alignment Tool:** The primary value of this document is for "compliance cross-walking." It allows an organization that uses NIST CSF 2.0 for its high-level security strategy to identify exactly which ISO 27001:2022 controls must be implemented to satisfy NIST subcategories.
*   **Complexity of Implementation:** The mapping demonstrates a **many-to-many relationship**. A single NIST subcategory (e.g., PR.PS-02 regarding software maintenance) often requires multiple ISO controls (e.g., documented procedures, configuration management, and change management). This highlights that fulfilling a single NIST objective requires a multi-layered technical and administrative approach.
*   **Foundational Role of "Documented Procedures":** A recurring theme in the mapping is the frequent appearance of **ISO Control A.5.37 (Documented operating procedures)**. This indicates that regardless of the technical goal (backups, monitoring, or software installation), standardized documentation is a fundamental requirement across almost all NIST functions.
*   **Lifecycle Coverage:** The document covers the entire "Security Lifecycle," spanning the four main NIST functions:
    *   **Protect (PR):** Prevention and platform security.
    *   **Detect (DE):** Continuous monitoring and anomaly identification.
    *   **Respond (RS):** Incident management, analysis, and mitigation.
    *   **Recover (RC):** Restoration of services and communication.

### Key Facts

**1. Framework Versions**
*   **NIST CSF:** Version 2.0.
*   **ISO/IEC:** 27001:2022 (the most recent major update to the standard).

**2. Core NIST Functions Addressed**
*   **Platform Security (PR.PS):** Focuses on managing hardware, software, and services to protect CIA (Confidentiality, Integrity, Availability).
*   **Technology Infrastructure Resilience (PR.IR):** Focuses on protecting networks and environmental threats.
*   **Continuous Monitoring (DE.CM):** Focuses on finding anomalies and indicators of compromise in networks, physical environments, and personnel activity.
*   **Adverse Event Analysis (DE.AE):** Focuses on understanding the impact and scope of detected events.
*   **Incident Management (RS.MA/RS.AN/RS.CO/RS.MI):** Covers the entire lifecycle of an incident, from declaration and triage to investigation and communication.
*   **Incident Recovery (RC.RP/RC.CO):** Focuses on executing recovery plans and communicating progress to stakeholders.

**3. Notable Specific Mappings**
*   **Data Backup:** NIST subcategory **PR.DS-11** (Backups) maps specifically to ISO **A.8.13** (Information backup).
*   **Incident Response:** NIST subcategory **RS.MA-01** (Executing response plans) maps to ISO **A.5.26** (Response to information security incidents).
*   **Software Security:** NIST subcategory **PR.PS-06** (Secure software development) maps to a large cluster of ISO controls (A.8.25 through A.8.34), emphasizing the breadth of the SDLC (Software Development Life Cycle).

**4. Document Metadata**
*   **Author:** Andrey Prozorov (a certified professional with CISM, CIPP/E, CDPSE, and LA 27001 credentials).
*   **Classification:** **TLP:GREEN** (Traffic Light Protocol), meaning the information is suitable for widespread distribution within the cybersecurity community.
*   **Date of Document:** March 1, 2024.