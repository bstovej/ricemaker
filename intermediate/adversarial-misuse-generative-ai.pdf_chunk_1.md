This document is a report from the **Google Threat Intelligence Group (GTIG)**, published in **January 2025**. It analyzes how government-backed threat actors (Advanced Persistent Threats or APTs) and Information Operations (IO) actors have attempted to misuse Google’s **Gemini** AI.

The overarching theme of the report is that while generative AI is helping attackers **increase the speed and volume** of their operations, it is **not yet creating entirely new or "breakthrough" attack capabilities.**

### **Key Insights**

#### **1. AI as a Productivity Tool, Not a "Game-Charies"**
*   **Efficiency over Innovation:** Threat actors are using Gemini to automate common tasks (research, troubleshooting, and content creation) rather than developing novel, unprecedented attack techniques.
*   **The "IT Admin" Analogy:** For many groups (particularly Chinese actors), using AI is similar to how a system administrator uses tools to automate routine tasks. For skilled actors, it acts as a framework similar to established tools like Metasploit or Cobalt Strike.
*   **No Advanced Prompt Injection:** The report found **no evidence** of sophisticated, original, or persistent "prompt injection" attacks or machine-learning-focused threats.

#### **2. Effectiveness of AI Safety Measures**
*   **Failed Jailbreaks:** Attackers primarily relied on "low-effort" methods, such as copying and pasting publicly available jailbreak prompts from sites like GitHub. These attempts were largely **unsuccessful**.
*   **Successful Guardrails:** Gemini’s safety filters effectively blocked requests for explicitly malicious content, such as creating ransomware, coding infostealers, or bypassing Google account verification. When faced with malicious instructions, the AI provided neutral, helpful, or safety-filtered responses instead.

---

### **Threat Actor Profiles**

The report categorizes the activity of several major government-backed groups:

| Actor Group | Level of Use | Primary Use Cases & Tactics |
| :--- | :--- | :--- |
| **Iran** | **Highest Volume** | Used for broad research (defense orgs, US military), vulnerability research (CVEs), and creating phishing content. **APT42** specifically used it to tailor phishing emails and research weapons systems (UAVs, satellite tech). |
| **China (PRC)** | **High Volume** | Behavior resembles an "IT admin." Focused on reconnaissance (US military/IT orgs), scripting/development, and techniques for lateral movement and privilege escalation within networks. |
| **North Korea** | **Moderate** | Focused on reconnaissance (US/South Korean military), payload development, and strategic research (cryptocurrency). **Notably used Gemini to draft cover letters/job applications** to support clandestine IT worker placement. |
| **Russia** | **Limited** | Focused narrowly on coding tasks, such as converting malware from one language to another or adding encryption functions to existing code. |

---

### **The Attack Lifecycle: How Gemini is Used**
The document details how AI is integrated into various stages of a cyberattack:
*   **Reconnaissance:** Researching target organizations, finding IP ranges, and studying individuals (e.g., defense experts).
*   **Weaponization:** Converting code (e.g., Python to Node.js), adding encryption (AES), or developing malicious scripts.
*   **Delivery:** Generating localized, culturally relevant phishing content and translating text to improve deceptive reach.
*   **Exploitation & Installation:** Researching specific vulnerabilities (CVEs) and finding ways to deploy tools (like VSTO plug-ins) silently.
*   **Actions on Objectives:** Automating post-compromise workflows, such as using Selenium to log into compromised accounts or extracting emails.

### **Summary Fact Sheet**
*   **Primary Threat Type:** Information Operations (IO) and Advanced Persistent Threats (APT).
*   **Primary Vulnerability Targeted:** Not the AI itself, but using the AI to accelerate traditional attack phases.
*   **Key Risk:** The primary danger is the **scaling of existing threats** (higher volume, better localization, faster research) rather than the invention of new ones.