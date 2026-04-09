Based on the provided document segments from the **Singapore Cyber Landscape 2022** report, here are the key insights and facts categorized by threat type:

### 1. Ransomware Trends
* **Stable Incident Rates:** The number of reported ransomware cases in Singapore remained relatively stable, with **132 cases in 2022**, compared to 137 in 2021.
* **Evolution of Tactics:** Ransomware has become more complex through:
    * **Ransomware-as-a-Service (RaaS):** Groups like LockBit 3.0 adopt models where they reuse or steal capabilities from other criminals.
    * **Cross-Operability:** New strains are designed to work across multiple operating systems (Windows, Linux, and Mac).
    * **Self-Propagation:** Some strains can spread through a network without human intervention.
* **Primary Targets:** Small and Medium Enterprises (**SMEs**) in the **Manufacturing and Retail** sectors are the most frequent victims.
* **Key Strains to Watch:** LockBit, DeadBolt (targets unpatched NAS systems), and MedusaLocker (exploits RDP vulnerabilities).

### 2. Phishing and Spoofing
* **Shortening URLs:** Threat actors are increasingly using URL shorteners to mask malicious links. The average length of reported phishing links decreased significantly from **44 characters in 2021 to 26 characters in 2022**.
* **Anomalous Targeting:** There was a notable trend of spoofing **China-based banks** (e.g., Agricultural Bank of China, Zhongyuan Bank) in the Singapore market, despite these banks having little to no presence in Singapore's retail banking scene.
* **Methods:** Attackers use bulk emails and SMS messages that impersonate delivery notifications (e.g., shipment issues, missing packages) to exploit user trust.

### 3. Infected Infrastructure (C&C Servers and Botnets)
* **Decrease in C&C Servers:** The number of infected Command and Control (C&C) servers dropped by **13%** (from 94,000 in 2021 to 81,500 in 2022). This may indicate improved cyber hygiene, though Singapore remains a hub for such infrastructure.
* **Dominant Malware:** 
    * **C&C Servers:** **Cobalt Strike** remains the top malware, followed by Emotet and Guloader.
    * **Botnet Drones:** **Gamarue, Nymaim, and Mirai** are the most prevalent.
* **The Rise of Mirai:** There was a significant uptick in **Mirai** infections in 2022, driven by global campaigns targeting vulnerabilities in Linux-based servers and IoT devices.
* **High Concentration:** Two malware families, Emotet and Nymaim, accounted for approximately **60% of all infected Singapore IP addresses**.

### 4. Website Defacements
* **Downward Trend:** The number of '.sg' website defacements decreased by nearly **20%** in 2022 (340 websites) compared to 2021.
* **Vulnerability Source:** A major weakness identified was the use of **outdated WordPress versions** (pre-6.0), which accounted for roughly 60% of defaced sites.
* **Attacker Profile:** The attacks were largely opportunistic and carried out by groups such as "Hunter Bajwa" and "B3g0k[Kurdish Hacker]," often using automated scripts.
* **Target Demographic:** **SMEs** were the primary victims; notably, **no government websites** were impacted by defacement in 2022.
* **Persistence:** "Re-defacements" (attacking a site that had already been defaced) accounted for almost **40%** of all observed incidents.

### Summary of Core Vulnerabilities
The document highlights a recurring theme: **unpatched software and negligence** are the primary drivers of cyber attacks. Whether it is outdated WordPress plugins, unpatched NAS systems, or unpatched RDP vulnerabilities, threat actors are successfully exploiting known weaknesses in both SME and consumer infrastructure.