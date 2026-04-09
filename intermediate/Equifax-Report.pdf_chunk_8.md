Based on the provided document segment regarding the Equifax 2017 data breach, here are the key insights and facts categorized by theme.

### 1. The Failure of Remediation (2015 vs. 2017)
The most significant insight is that **the 2017 breach was preventable.** The document reveals a direct link between unaddressed findings from a 2015 audit and the eventual breach.
*   **Known Issues Left Unresolved:** Equifax failed to remediate many of the security deficiencies identified in a 2015 Patch Management Audit prior to the 2017 breach.
*   **Reactive vs. Proactive:** Patching was performed reactively (responding to alerts) rather than proactively.
*   **The "Honor System":** Patching relied on an "honor system" with no controls, no tracking for exceptions, and no mechanism to ensure accountability or compliance.

### 2. Critical Failures in Patch & Certificate Management
The document highlights specific technical management failures that directly allowed the attackers to operate undetected.
*   **Certificate Blindness:** At the time of the breach, Equifax had **324 expired SSL certificates**, 79 of which were for business-critical domains. 
    *   *Critical Impact:* An expired certificate on the device monitoring the ACIS platform prevented the company from seeing suspicious traffic, which could have mitigated or prevented the breach.
*   **Lack of Visibility (Asset Management):** Equifax lacked a comprehensive, up-to-date inventory of its IT assets. 
    *   Because they did not know exactly what software was running on their systems, they were "surprised" to discover the presence of the vulnerable Apache Struts software during the breach.
*   **Policy/Execution Disconnect:** While a Patch Management Policy existed and defined roles, Equifax failed to actually designate employees to fill those roles.

### 3. The Risks of Legacy Infrastructure (The ACIS System)
The breach centered on the **ACIS system**, an internet-facing platform for credit disputes, which suffered from the inherent risks of "legacy" technology.
*   **Complexity through Acquisition:** Rapid company growth via acquisitions created a highly complex, fragmented IT infrastructure that was difficult to secure and standardize.
*   **The "Knowledge Gap":** The ACIS system relied on aging technology (Sun Microsystems/Solaris) and a dwindling number of original developers. There was a significant operational risk that the specialized knowledge required to maintain these systems would disappear as the workforce aged.
*   **Custom-Built Complexity:** Many systems were custom-built, making it nearly impossible for standard automated scanning tools to identify all software components within the technology stack.

### 4. Specific Technical Vulnerabilities in the ACIS Environment
A security assessment identified several critical "security concerns" within the ACIS environment that facilitated the attackers' movement:
*   **Lack of Network Segmentation:** There was no segmentation between the application servers and the rest of the network. This allowed attackers to **"pivot" or move laterally** from the initial point of entry to any other device or database globally within the Equifax network.
*   **Absence of File Integrity Monitoring (FIM):** The lack of FIM meant the company could not detect unauthorized changes to files. The report notes that FIM could have detected the **30 web shells** created by the attackers.
*   **Insecure File Sharing:** A shared file system allowed access to administrator files from one system to another, violating the "principle of least privilege" and providing attackers with a path to sensitive configuration files.