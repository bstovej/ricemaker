Based on the provided document segments from the **Singapore Cyber Landscape 2022**, here are the key insights and facts categorized by the three main themes presented:

### 1. Anti-Scam Initiatives and Ecosystem in Singapore
The document highlights a highly collaborative approach to combating financial fraud and scams through **ASCom** and various institutional partnerships.

*   **Large-Scale Recoveries:**
    *   **Record Recovery:** In May 202, a partnership between ASCom and DBS Bank led to the recovery of **US$11.5 million**, the largest single amount recovered from one scam arrangement to date.
    *   **Major BEC Scam:** A Business Email Compromise (BEC) scam involving spoofed emails resulted in losses of over **US$15.5 million** to accounts held with DBS.
*   **Collaborative Infrastructure:**
    *   **Institutional Network:** ASCom partners with over **80 institutions**, including local/foreign banks, fintechs (e.g., Grab, Singtel DASH), and cryptocurrency houses (e.g., Wise, Coinhako).
    *   **Operational Co-location:** Six major banks (**DBS, OCBC, UOB, SCB, HSBC, and CIMB**) have co-located staff within ASCom premises to enhance real-time coordination and fund tracing with the police.
*   **Proactive Enforcement:**
    *   In 2022, ASCom froze more than **16,700 bank accounts** based on reports.
    *   ASCom works with the Singapore Police Force (SPF) and telcos to terminate scam-related phone numbers and WhatsApp lines.
    *   Technological integration includes using **AI** to identify and block suspicious financial transactions.

### 2. Technical Threat Intelligence: SocGholish Malware
The document provides a technical deep dive into the **SocGholish** malware, analyzed by Ensign InfoSecurity.

*   **Attack Mechanism:**
    *   **Evolution of Tactics:** Traditionally known for "drive-by" infections, SocGholish has evolved to use **malicious scripts embedded in legitimate web pages** that masquerade as software updates (e.g., fake browser or Windows updates).
    *   **The Process:** A user clicks a malicious link $\rightarrow$ a ZIP archive is downloaded $\rightarrow$ a malicious payload executes $\rightarrow$ the malware establishes a backdoor $\rightarrow$ it performs credential dumping and moves laterally across the network.
*   **Impact and Response:**
    *   **Capabilities:** The malware can exfiltrate user credentials, provide lateral access to networks, and create unauthorized administrator accounts.
    *   **Successful Containment:** In a studied incident, Ensign’s response teams successfully contained the breach within **48 hours**.
*   **Key Preventative Measures:**
    *   Use only **official tools** for system and software updates.
    *   Implement the **Principle of Least Privilege** to limit the impact of an infection.
    *   Maintain regular backups and educate employees on recognizing phishing/social engineering.

### 3. Case Study: Ransomware Lessons Learnt
An interview with the CEO and CIO of a Singapore-based precision engineering company reveals the high-stakes reality of ransomware attacks.

*   **The Incident:**
    *   The company faced a ransomware attack in 2022 with a demand of **200 Bitcoins (approx. S$7 million)**.
    *   The attackers threatened to leak stolen blueprints and client schematics, creating a massive competitive and reputational risk.
*   **The "Pay vs. No-Pay" Dilemma:**
    *   The decision to pay was driven by the fear of data leakage rather than a desire to comply with criminals. 
    *   **The consequence of paying:** The company opted to pay part of the ransom, but **80% of the demand was still incurred later**, and there remains no guarantee that the hackers will actually destroy the stolen data.
*   **Critical Recovery Factor:**
    *   **The Importance of Backups:** The company was able to resume operations because they followed a strict policy of **backing up data every weekend** to offline storage. This prevented permanent data loss despite the encryption of their primary systems.