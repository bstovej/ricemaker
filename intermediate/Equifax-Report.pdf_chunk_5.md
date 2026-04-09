This document segment details the technical causes, internal timeline, and the subsequent public response regarding the 2017 Equifax data breach.

### **1. Technical Cause of the Breach**
*   **Exploit Method:** Attackers used **JSP (JavaServer Pages) files** to create "web shells." These files allowed the attackers to execute commands on the web server and receive output, essentially giving them remote control.
*   **Vulnerability:** The breach was facilitated by a known **Apache Struts vulnerability**. Although a scan in January 2017 had identified this vulnerability as "remediated," a subsequent review of the application’s WAR file confirmed that a vulnerable version of Apache Struts was still running on the ACIS platform.
*   **Lack of Visibility:** A second server within the ACIS application also ran a vulnerable version of Apache Struts. Because Equifax had **not loaded an SSL certificate** on this server, the company had no visibility into the traffic moving to and from it.

### **2. Timeline of Internal Awareness vs. Public Disclosure**
There was a significant gap (approximately five weeks) between the internal discovery of the breach and the public announcement.
*   **July 31, 2017:** CIO David Webb informed CEO Richard Smith of the incident. On this same day, the Chief Security Officer (Mauldin) stated she believed Personally Identifiable Information (PII) had been involved, though she did not report this specific belief to the CIO.
*   **August 2, 2017:** Equifax contacted outside counsel and the FBI.
*   **August 3, 2017:** The cybersecurity firm **Mandiant** was hired to conduct a forensic review.
*   **August 11, 2017:** Mandiant identified potential access to consumer PII.
*   **August 15, 2017:** Equifax leadership was informed that consumer PII was likely stolen.
*   **August 24–25, 2017:** The CEO informed the Equifax Board of Directors.
*   **September 7, 2017:** **Public notification** was issued, initially stating 143 million consumers were affected (a number that later rose to 148 million).

### **3. Crisis Management: "Project Sparta"**
Equifax initiated "Project Sparta" to manage the fallout and prepare for public notification.
*   **Objectives:** To create a consumer-facing website (`equifaxsecurity2017.com`) and establish call center capabilities.
*   **Scale of Effort:** The company attempted to ramp up **1,500 call center agents** in roughly one week and deployed 50 to 60 IT employees to the website project.
*   **External Support:** Mandiant performed the forensic investigation from August 3 to October 2.

### **4. Operational Failures and Consequences**
The document highlights several critical failures in Equifax's public response:
*   **Communication Errors:** An error on the company's Twitter account directed users to a fraudulent site.
*   **Website Failures:** The newly created website suffered from coding errors and was difficult to use. An error in the Twitter handle caused users to land on a fake site.
*   **The "Phishing" Incident:** A significant error occurred where the company's official Twitter account directed users to a fake website, leading to potential security risks for consumers.
*   **Technical Bottlenecks:** The website provided inconsistent information; for example, the content displayed differently on mobile devices versus desktops.
*   **Systemic Errors:** The company’s Twitter account accidentally directed users to a fake website.
*   **Financial and Reputational Impact:** The breach led to a significant drop in stock value and a loss of consumer trust. The company's stock price dropped by 35% in the weeks following the announcement.
*   **Regulatory/Legal Consequences:** The breach prompted investigations by various regulatory bodies and lawsuits from affected consumers.

### **Summary of Key Findings**
| Category | Key Detail |
| :--- | :--- ability to exploit known vulnerabilities (Apache Struts). |
| **Root Cause** | Unpatched software (Apache Strors) and lack of visibility due to unencrypted traffic. |
| **Scale of Impact** | Over 147 million people potentially affected; massive loss of consumer trust. |
| **Operational Failure** | Inability to manage the scale of the crisis (broken links, incorrect Twitter info, overwhelmed servers). |
| **Corporate Fallout** | Significant decline in market capitalization and intense regulatory scrutiny. |