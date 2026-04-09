This report, issued by the U.S. House of Representatives Committee on Oversight and Government Reform, details the systemic failures that led to the 2017 Equifax data breach.

### **1. Scale and Impact of the Breach**
* **Scope of Data Loss:** The breach initially affected 143 million consumers, a figure that later rose to **148 million**—representing approximately 56% of the U.S. adult population.
* **Type of Data:** The stolen information included highly sensitive **Personally Identively Information (PII)**, which is a high-value target for cybercriminals due to its use in fraud and identity theft.

### **2. Technical Root Causes**
* **The Primary Vulnerability:** The breach was made possible by a failure to patch a known, critical vulnerability in **Apache Struts** software. 
* **Failure to Act on Alerts:** 
    * On March 7, 2017, the vulnerability was publicly disclosed.
    * On March 8, 2017, the Department of Homeland Security alerted Equifax.
    * On March 9, 2017, Equifax’s internal security team instructed staff to apply the patch within 48 hours.
    * **The Failure:** Equifax failed to patch the "Automated Consumer Interview System" (ACIS), leaving the door open for attackers.
* **The Attack Sequence:** Attackers entered the network on May 13, 2017, and remained undetected for **76 days**. They used "web shells" to gain remote control and discovered **unencrypted credentials** (usernames and passwords), which allowed them to access 48 unrelated databases.

### **3. Critical Systemic and Operational Failures**
* **Monitoring Blind Spot:** Equifax failed to detect the massive data exfiltration because the device used to monitor network traffic had an **expired security certificate that had been inactive for 19 months**. The breach was only discovered after the certificate was finally updated on July 29, 2017.
* **Growth vs. Security:** Under CEO Richard Smith, Equifax pursued an aggressive acquisition strategy. While this grew the company's value, it created an incredibly complex IT environment with "legacy" (outdated) systems that were difficult to secure.
* **Lack of Accountability:** The report identifies a lack of clear authority within Equifax’s IT management. This led to an "execution gap" where security policies were developed but not implemented. 
* **Certificate Negligence:** The company allowed over **300 security certificates to expire**, including 79 that were critical to monitoring business domains.

### **4. Leadership and Accountability**
The breach resulted in significant personnel changes and high-level accountability:
* **Richard Smith (CEO):** Left the company in September 2017.
* **David Webb (CIO) & Susan Mauldin (CSO):** Both took early retirements in September 2017.
* **Graeme Payne (SVP):** Terminated for failing to forward an internal email regarding the Apache Struts vulnerability.

### **Summary Fact Sheet**
| Feature | Detail |
| :--- | :--- |
| **Duration of Attack** | 76 Days (May 13 – July 30, 2017) |
| **Total Victims** | 148 Million |
| **Primary Software Flaw** | Apache Struts (CVE-2017-5638) |
| **Critical Oversight** | Security monitoring certificate expired for 19 months |
| **Core Internal Issue** | Excessive IT complexity due to aggressive acquisition strategy |