This document segment details the organizational and procedural failures at Equifax that contributed to the 2017 data breach. The text highlights a breakdown in communication, accountability, and execution between the Information Technology (IT) and Security departments.

### **Key Insights**

#### **1. Flawed Organizational Structure and Governance**
*   **Siloed Operations:** The IT and Security organizations functioned in "silos," with minimal information flow between them. Collaboration typically only occurred when required for specific network changes.
*   **Atypical Reporting Lines:** At the time of the breach, the Chief Security Officer (CSO) reported to the Legal department. This was identified as being outside industry norms; most CSOs report to the CIO, CEO, or Board of Directors. 
*   **Lack of Executive Prioritization:** The CEO did not prioritize cybersecurity; it was merely one topic in quarterly meetings. Furthermore, security information was presented to the CEO by the Chief Legal Officer, who lacked a technical background in IT or security.
*   **Ineffective Coordination:** The separation of responsibilities meant the Security team defined the "what" (policies), while the IT team handled the "how" (implementation). This division created gaps in accountability.

#### **2. Failure of the Patch Management Process**
*   **The Apache Struts Catalyst:** The 2017 breach was caused by the exploitation of a known vulnerability in Apache Struts. Although the patch was classified as "critical" and should have been applied within 48 hours of the March 8, 2017, alert, Equifax did not patch the affected ACIS system until the breach was discovered in late July 2017.
*   **Lack of Accountability:** While a Patch Management Policy existed, the company failed to officially designate "system owners" and "application owners" for many assets. This meant there was no clear individual responsible for ensuring the ACIS system was patched.
*   **Communication Breakdown:** The primary method for notifying staff of vulnerabilities was a single email sent to a large listserv (400 individuals). There were no redundant systems or follow-up processes to ensure the correct personnel had received and acted upon the alert.
*   **Inconsistent Inventories:** Both IT and Security maintained separate, incomplete software inventory lists, making it difficult to track which systems were vulnerable and in need of patching.

#### **3. Prior Warning and Negligence**
*   **Ignored Audit Findings:** Equifax was aware of significant deficiencies in its patching and asset management processes long before the breach. A **2015 audit** specifically identified that vulnerabilities were not being remediated in a timely manner and that the company lacked adequate IT asset management procedures.

### **Key Facts**
*   **The Breach Source:** The initial intrusion was confirmed to be the exploitation of the Apache Struts vulnerability.
*   **Policy Requirement:** Equifax’s 2016 Patch Management Policy mandated that critical vulnerabilities be patched within **48 hours**.
*   **Post-Breach Structural Changes:** Following the breach, Equifax restructured its leadership:
    *   The CSO role was renamed **CISO** (Chief Information Security Officer).
    *   The CISO was elevated to report **directly to the CEO**.
    *   The CIO role was renamed **CTO** (Chief Technology Officer), who also reports directly to the CEO.
*   **The "GTVM" Alert:** The Global Threat and Vulnerability Management (GTVM) team was the entity responsible for distributing the initial email alerts regarding vulnerabilities.