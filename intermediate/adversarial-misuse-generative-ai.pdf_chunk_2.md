This document is a threat intelligence report (likely from Google Threat Intelligence Group) detailing how various nation-state actors and financially motivated criminals are leveraging Large Language Models (LLMs), specifically **Gemini**, to advance cyberattacks, information operations, and espionage.

The following are the key insights and facts categorized by actor type:

### 1. North Korean (DPRK) Actors: The "Clandestine IT Worker" Threat
This section contains the most significant strategic findings, moving beyond traditional hacking into economic espionage.
*   **The Clandestine IT Worker Scheme:** North Korean actors are using Gemini to support a massive scheme involving thousands of workers using fake identities to secure freelance and full-time roles at Western companies. They use the AI to:
    *   Draft professional cover letters and job proposals.
    *   Research average salaries and find jobs on LinkedIn.
    *   Research "best Discord servers for freelancers."
*   **Cyberattack Lifecycle Support:** They use Gemini for reconnaissance (target organizations, US/South Korean military), payload development (C++ code for webcam recording), and defense evasion (writing code to detect Virtual Machines/Hyper-V).
*   **Strategic Research:** They use the tool to research sensitive topics like South Korean nuclear technology, cryptocurrency, and the impact of the Russia-Ukraine conflict.
*   **AI Tool Diversification:** Beyond Gemini, they use tools like *Monica* and *Ahells* for writing and employ AI-driven image manipulation to create realistic profile photos for their fake personas.

### 2. PRC (China) Actors: Technical Exploitation & Information Operations
PRC-backed actors demonstrate a dual use of Gemini: advanced technical assistance and large-scale influence campaigns.
*   **Technical Post-Exploitation:** APT actors use Gemini to assist in the "hands-on-keyboard" phase of an attack. Specific queries included:
    *   How to sign plugins for Microsoft Outlook for silent deployment.
    *   Generating code to access Windows Event Logs and identifying admin IPs.
    *   Troubleshooting tools like `impacket` and `smbclient`.
    *   Reverse engineering the EDR tool *Carbon Black*.
*   **Information Operations (IO):** The group **DRAGONBRIDGE** is identified as the most prolific pro-China IO actor, responsible for roughly 75% of PRC-linked activity.
    *   Their use focuses on general research (US/Taiwan politics) and content generation.
    *   They have experimented with AI-generated news presenters in YouTube videos.

### 3. Iranian-Linked Actors: Content Manipulation & Localization
Iranian actors represent the highest volume of Information Operations (IO) activity in the report.
*   **High-Volume Influence:** Iranian-linked groups accounted for **75% of all prompts** from all monitored IO actors.
*   **Sophisticated Localization:** Instead of just translating, they use Gemini to "localize" content—asking the AI to make Farsi-to-English translations sound like a "native English speaker" to increase credibility.
*   **Content Manipulation:** They use the AI to rewrite text to adopt specific biases, tones, or political slants (e.g., rewriting text about Sharia law or diplomacy to suit a specific narrative).
*   **SEO and Reach:** They use Gemini to generate SEO-optimized content and titles to ensure their propaganda reaches a wider audience.

### 4. Russian Actors: Limited but Strategic Use
The report notes a surprisingly low level of Gemini usage by Russian actors.
*   **Low Engagement/OPSEC:** The report suggests Russian actors may be avoiding Western-controlled platforms like Gemini to avoid monitoring, potentially favoring locally hosted LLMs or Russian-made AI.
*   **Technical Use Cases:** When they do use it, the focus is on rewriting existing malware into different languages and adding encryption functionality.
*   **AI Development Research:** Russian IO actors have been observed researching the generative AI landscape itself, specifically looking for tools to build their own online chatbots and textual analysis tools.

### 5. Financially Motivated Actors: The Rise of "Jailbroken" LLMs
The report highlights an emerging underground market for "unfiltered" AI.
*   **Malicious LLMs:** There is a burgeoning market for "jailbroken" models like **FraudGPT** and **WormGPT**. These are customized versions of LLMs designed specifically to bypass security guardrails, allowing users to generate malware and phishing content without restriction.
*   **Advanced Phishing:** These actors are using manipulated video and voice content (Deepfakes) and tools like WormGPT to create highly persuasive Business Email Compromise (BEC) scams.

### Summary Table of Key Findings

| Actor Category | Primary Gemini Use Case | Notable Characteristic |
| :--- | :--- | :--- |
| **North Korea** | Job hunting (fake identities) & Malware development | Focus on the "Clandestine IT Worker" scheme. |
| **PRC** | Post-exploitation & Info Ops | Highly technical; usage of DRAGONBRIDGE group. |
| **Iran** | Content localization & Manipulation | Highest volume of IO-related prompts. |
| **Russia** | Malware rewriting & AI research | Low engagement; focus on building native AI. |
| **Financial** | Malware & Phishing generation | Use of "Jailbroken" models (WormGPT/FraudGPT). |