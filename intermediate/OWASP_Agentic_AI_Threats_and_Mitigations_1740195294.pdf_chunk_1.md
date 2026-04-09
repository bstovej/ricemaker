This document, produced by the **OWASP Agentic Security Initiative (ASI)**, serves as a foundational guide for identifying and mitigating security risks specific to **Agentic AI** (autonomous systems powered by LLMs).

Below are the key insights and facts categorized by theme.

### 1. Core Definition and Evolution
*   **The Shift in AI:** While "agentic AI" predates LLMs, the integration of Generative AI has expanded the scale, autonomy, and risk profiles of these systems.
*   **Definition of an Agent:** An intelligent system that perceives its environment, reasons, makes decisions, and takes autonomous actions to achieve specific goals.
*   **Core Capabilities:** Modern agentic systems rely on three pillars:
    *   **Planning & Reasoning:** Using patterns like **ReAct** (Reason + Act), **Reflection** (evaluating past actions), **Chain of Thought** (step-by-step logic), and **Subgoal Decomposition**.
    *   **Memory/Statefulness:** Maintaining context through session-based (short-term) or persistent (long-term) memory.
    *   **Action and Tool Use:** The ability to invoke external tools, browse the web, perform math, or execute code via **Function Calling**.
*   **Market Forecast:** Gartner predicts that by **2028, 33% of enterprise software applications** will utilize agentic AI, enabling 1s5% of daily work decisions to be made autonomously.

### 2. Architectural Frameworks
The document identifies two primary ways agents are deployed:
*   **Single-Agent Architecture:** A centralized system where an application uses an LLM as a reasoning engine to interact with tools, external APIs, and databases (e.g., Vector databases for RAG).
*   **Multi-Agent Architecture:** A complex ecosystem where multiple specialized agents collaborate, often overseen by a "Coordinating Agent" or "Supervisor Agent."
*   **Agentic Patterns:** The document identifies several emerging patterns, including **Reflective Agents** (self-critiquing), **Hierarchical Agents** (managing workflows), and **Human-in-the-Loop** (semi-autonomous with human oversight).

### 3. The Emerging Threat Landscape
The primary insight of the document is that agentic AI introduces **new attack vectors** that go beyond traditional LLM vulnerabilities (like prompt injection).

#### **Key Vulnerabilities:**
*   **The "Confused Deputy" Problem:** A critical risk where an agent possesses higher privileges than the user but is manipulated via adversarial instructions to perform unauthorized actions on the user's behalf.
*   **Tool Misuse & Excessive Agency:** Unlike standard LLM risks, agentic systems can "chain" tools in unexpected ways to bypass security controls (e.g., retrieving data from one tool and exfiltrating it via another).
*   **Non-Human Identity (NHI) Risks:** Agents often operate using machine accounts, service identities, or API keys. These lack the session-based oversight of human users, making them susceptible to token abuse and privilege misuse.
*   **Memory & Knowledge Poisoning:** Attackers can target the agent's long-term memory or the RAG (Retrieval-Augmented Generation) pipeline to inject malicious information that influences future autonomous decisions.
*   **Remote Code Execution (RCE):** The agent's ability to generate and execute code as a "tool" creates a direct path for much more severe traditional cyberattacks.

### 4. Security Recommendations & Mitigations
The document advocates for moving toward a **Zero-Trust** model for AI agents. Key strategies include:
*   **Privilege Down-scoping:** Reducing the permissions of an agent so it cannot perform actions beyond what is strictly necessary for the user's specific request.
*   **Strict RBAC (Role-Based Access Control):** Implementing rigorous identity and access management for both human users and Non-Human Identities (NHIs).
*   **Permission-Aware Infrastructure:** Utilizing vector databases and tools that are natively aware of user permissions to prevent unauthorized data retrieval.
*   **Identity Flow Validation:** Ensuring that as identity flows from a user to an agent to a third-party API, the original user's constraints are maintained.