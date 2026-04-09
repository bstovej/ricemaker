This document segment appears to be a draft of an international standard (**ISO/IEC 27090**) regarding the security of Artificial Intelligence (AI) systems. It outlines strategies for reducing the attack surface, controlling unwanted model behavior, and categorizing specific AI-centric threats.

Below are the key insights and facts extracted from the text.

### 1. Key Strategic Insights

*   **The Security-Transparency Paradox:** A recurring theme in the document is the tension between **transparency** (needed for user trust and explainability) and **security** (where too much technical detail provides a roadmap for attackers). Effective security requires minimizing technical "leakage" while maintaining enough information for users to understand the model's limitations.
*   **The "Human-in-the-Loop" Risk:** While human oversight is a primary control for managing unwanted behavior, the document highlights the **"out-of-the-loop" phenomenon**. High levels of automation can lead to human disengagement, causing a loss of situational awareness and slower, less effective responses to system failures.
*   **Principle of Least Privilege applied to AI:** The document extends traditional cybersecurity principles to AI, suggesting that **"Least Model Privilege"** should be implemented—restricting an AI's autonomy and access to external systems (e.g., preventing an LLM from having direct access to email facilities) to mitigate the impact of potential hijacks.
*   **Data Minimization as a Security Control:** Reducing the attack surface is not just about access control, but about **data limitation**. By reducing the amount, variety, and retention duration of data, an organization inherently reduces the potential impact of a data breach.

### 2. Core Security Controls & Methodologies

The document outlines several specific technical and procedural controls:

*   **Data Management Controls:**
    *   **Data Minimization:** Using statistical analysis, dimensionality reduction, and feature selection to remove unnecessary data.
    *   **Obfuscation:** Utilizing **Differential Privacy** (adding controlled noise to datasets) to protect individual identities while allowing for aggregate statistical analysis.
    *   **Data Provenance:** Ensuring the origin and history of data are known (referencing ISO/IEC 5181).
*   **Operational Controls:**
    *   **Continuous Validation:** Frequent testing against datasets to detect "model drift" or permanent attacks like poisoning.
    *   **Explainability (XAI):** Using explainable AI to build trust and allow users to identify when a model's "reasoning" is flawed, which prevents **overreliance**.
    *   **Guardrails:** Implementing automated business logic to halt or correct improper model decisions.
*   **Proactive Testing:**
    *   **Threat Modeling:** Using structured techniques to identify potential AI-specific security issues during the lifecycle.
    *   **Red Teaming:** Emulating real-world adversaries to test for both security vulnerabilities and safety risks (e.g., the production of harmful content).

### 3. Fact Sheet: AI-Specific Threats

The document provides a taxonomy of attacks targeting AI systems:

| Attack Type | Mechanism | Primary Impact |
| :--- | :--- | :--- |
| **Data Poisoning** | Injecting malicious data into training sets. | Compromised model integrity/accuracy. |
| **Model Inversion/Extraction** | Reverse-engineering the model or its training data. | Privacy breach/Loss of intellectual property. |
| **Adversarial Attacks** | Crafting specific inputs to trigger errors. | Model failure/Incorrect outputs. |
| **Prompt Injection** | Manipulating LLM inputs to bypass constraints. | Bypassing safety guardrails. |

**Specific Attack Classifications Mentioned:**
*   **Targeted Attacks:** Using "adversarial" inputs to cause specific misclassifications.
*   **Data Poisoning (Two types):** 
    1.  **Targeted:** Aimed at causing a specific error.
    2.  **Untargeted:** Aimed at degrading the overall performance of the model.
*   **Prompt Injection:** Specifically relevant to LLMs, where an attacker manipulates the input to override the system's original instructions.

### 4. Key Technical Terminology
*   **Overfitting:** When a model learns the noise in the training data rather than the signal, making it fail on new data.
*   **Underfitting:** When a model is too simple to capture the underlying structure of the data.
*   **Model Robustness:** The ability of a model to maintain performance despite noisy or adversarial input.
*   **Model Interpretability/Explainability:** The degree to which a human can understand the cause of a decision made by an AI.