This document segment is an excerpt from the **ISO/IEC DIS 27090** draft standard, focusing on the security threats, mitigations, and operational management of AI systems.

Below are the key insights and facts categorized by threat type, mitigation strategy, and systemic management.

### 1. Key AI Security Threats
The document identifies several critical vectors for data leakage and system manipulation:

*   **Training Data Leakage (6.9):** Unauthorized access to sensitive training or test data (e.g., PII, trade secrets). This occurs through development environments, live systems during the operational stage, or via third-party cloud providers during model fine-tuning.
*   **Model Input Leakage (6.10):** Sensitive data entering the model through user prompts or RAG (Retrieval-Augmented Generation) can be intercepted (e.g., Man-in-the-Middle attacks) or inadvertently reflected in the model's output.
*   **Sensitive Model Output (6.11):** The model may "memorize" and subsequently output sensitive information from its training set, such as personal data or copyrighted material, either through normal use or malicious provocation.

*   **Prompt Injection (6.12):** 
    *   **Direct:** Users provide instructions to bypass constraints (e.g., "Ignore previous instructions").
    *   **Indirect/Cross-domain:** Malicious instructions are hidden in external data sources (like a compromised website) that the AI subsequently processes as context.
*   **Output-based Injection (6.13):** Model-generated text may contain "traditional" malicious payloads, such as Cross-Site Scripting (XSS), which execute when the output is rendered by a web browser or another system.

### 2. Mitigation Strategies & Zero Trust Principles
The document heavily emphasizes **Zero Trust** architecture as the primary defense mechanism across all threat vectors.

*   **Core Zero Trust Principles for AI:**
    *   **Least Privilege Access:** Utilizing **Just-in-Time (JIT)** and **Just-Enough Access (JEA)** to limit model and dataset access.
    *   **Assume Breach:** Implementing encryption at rest, in transit, and **in use**, alongside automated detection and remediation plans.
    *   **Verify Explicitly:** Scrutinizing all inputs to ensure no information is leaked in outputs, and validating that model outputs do not contain malicious code.
    *   **Input Segregation:** Using specific prompt engineering (e.g., "meta-prompts") to clearly separate untrusted user input from the system's internal instructions.
*   **Data Protection:** Implementing monitoring and filtering to prevent the leakage of sensitive information during the training and inference phases.

### 3. Federated/Distributed Learning (Federated Learning Context)
The document highlights **Federated Learning** as a way to manage data privacy, though it acknowledges specific risks:
*   **Benefits:** It helps mitigate the risks of moving sensitive data by training locally.
*   **Risks:** It introduces vulnerabilities such as poisoning attacks (adversarial training) and the potential for information leakage through model updates.

### 4. Operational Management & Lifecycle Risks
*   **The "Performance vs. Security" Trade-off:** The document warns that mitigation strategies (like adversarial training) can negatively impact model performance, accuracy, or robustness.
*   **Model Decay and Drift:** AI models are subject to "deterioration" over time. Continuous monitoring is required to address model drift and ensure the integrity of the deployment.
*   **Complexity of the Lifecycle:** Security must be integrated throughout the entire lifecycle, from initial data collection and training to deployment, monitoring, and eventual decommissioning.
*   **Systemic Risks:** The document notes that vulnerabilities in the underlying infrastructure, data pipelines, or third-party dependencies can compromise the entire AI system.

### Summary Table of Key Concepts

| Category | Key Risks Identified | Primary Mitigation Strategies |
| :--- | :--- | :--- |
| **Data Privacy** | Leakage of training/test data; PII exposure. | Encryption; Federated Learning; Input/Output filtering. |
| **Integrity** | Poisoning attacks; Prompt injection; Model drift. | Adversarial training; Robustness testing; Continuous monitoring. |
| **Availability** | Denial of Service (DoS) via complex queries. | Rate limiting; Resource quotas; Input sanitization. |
| **Systemic** | Supply chain vulnerabilities; Infrastructure failure. | Secure software development (SDLC); Robust monitoring; Redundancy. |