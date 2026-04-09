This document is a draft of an upcoming international standard, **ISO/IEC DIS 27090**, titled *"Cybersecurity — Artificial Intelligence — Guidance for addressing security threats to artificial intelligence systems."*

Below are the key insights and facts extracted from the provided segment.

### **1. Document Status and Purpose**
*   **Current Stage:** Draft International Standard (**DIS**). It is currently in a review phase to confirm that previous comments from the 1st Committee Draft (CD) have been correctly implemented.
*   **Critical Deadline:** Experts must submit comments/replies by **November 29, 2024**. 
*   **Finality of Review:** After this specific review period, the document will be submitted for a DIS ballot, and **no new comments will be considered.**
*   **Authoring Body:** ISO/IEC JTC 1/SC 27/WG 4 (Security controls and services).

### **2. Core Objective**
The primary goal of the standard is to provide guidance on **mitigating security threats** to AI systems to improve the trustworthiness of organizations that develop or use them. It focuses on protecting the AI lifecycle, including data, models, and outputs.

### **3. Key Security Threats Identified**
The document categorizes a wide range of specific AI-centric attacks, including:
*   **Data-Level Attacks:** Data poisoning, direct training data leaks, and direct model poisoning.
*   **Model-Level Attacks:** Evasion attacks, model exfiltration, model inversion, model theft, and backdoor attacks.
*   **Inference & Privacy Attacks:** Membership inference, model input leaks, and sensitive model output leaks.
*   **Input/Output Attacks:** **Prompt injection** and attacks where the model's output contains malicious injection attacks.
*   **Infrastructure/System Attacks:** Denial-of-Service (DoS) or scaling attacks and supply chain attacks.

### **4. Key Mitigation Strategies & Frameworks**
The standard proposes a multi-layered approach to security:
*   **Foundational Principles:** Implementation of **Zero Trust** principles and robust AI governance programs.
*   **Data Management:** Data minimization, minimal retention, data obfuscation, and ensuring data integrity.
*   **Operational Controls:** 
    *   **Continuous Validation:** Monitoring model behavior and using **Red Teaming** and threat modeling.
    *   **Model Oversight:** Implementing "least model privilege," transparency, and explainability.
    *   **Input/Output Filtering:** Detecting adversarial or "odd" inputs and filtering malicious outputs.
    *   **Technical Guardrails:** Throttling model use, protecting the development environment, and obscuring confidence scores to prevent reverse-engineering.
*   **Software Engineering:** Applying established software engineering best practices specifically to the AI context.

### **5. Structural Components**
*   **Annex A:** Provides a framework for mapping specific attacks to the **AI system life cycle** and identifying specific **assets** that need protection.
*   **Annex B:** Details how conventional cyber attacks (like DoS and Supply Chain attacks) manifest in AI-specific contexts.