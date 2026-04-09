This document, **ISO/IEC DIS 27090**, serves as a guidance framework for addressing security threats specific to Artificial Intelligence (AI) systems. It outlines how organizations can protect AI models and data throughout their entire lifecycle.

Below are the key insights and facts extracted from the text, categorized by theme.

### 1. The Evolving Threat Landscape
The fundamental insight of the document is that AI security is not a replacement for traditional cybersecurity, but an expansion of it.
*   **Dual-Layer Threats:** AI systems are vulnerable to **traditional cybersecurity attacks** (e.g., DDoS, unauthorized access) **AND** **new, AI-specific attacks** (e.g., data poisoning, model theft).
*   **Increased Severity:** Because AI is increasingly used in "safety-critical contexts," security breaches can lead to much more severe consequences than traditional data breaches, including potential **physical or mental repercussions** for individuals.
*   **The Vulnerability of Training Data:** The heavy dependency on training data (which often includes unvetted or user-provided data) creates a unique attack surface that conventional information processing systems do not face to the same degree.

### 2. Specific AI-Based Attack Vectors
The document defines several specialized attack types that target the unique architecture of machine learning:
*   **Data Poisoning:** Injecting malicious or unwanted data into the training set to manipulate the AI’s behavior. This is particularly dangerous in systems utilizing **continuous learning**, where an attacker can corrupt the model during operation.
*   **Model Exfiltration (Model Theft):** An attacker copies the model (or parts of it) by making legitimate queries and observing the outputs. Notably, the document states that **conventional security (like rate limiting) may be insufficient** to stop this.
*   **Evasion Attacks:** Manipulating inputs to cause the AI to avoid correct behavior (e.g., making a system fail to recognize a specific object).
*   **Membership Inference:** An attack aimed at determining whether a specific piece of data was part of the model's original training set.
*   **Model Inversion:** An attack where the adversary attempts to reconstruct the original training data by analyzing the model's outputs.

### 3. Strategic Mitigation & Defense
The document advocates for a **"Defense in Depth"** strategy, combining established security frameworks with new, AI-specific controls.
*   **Zero Trust Principles:** The document emphasizes a "never trust, always verify" approach. Key tenets include:
    *   Assuming the system is already breached.
    *   Using end-to-end encryption for all requests.
    *   Applying **least privilege access control** even to those interacting with the model.
    *   Authenticating and authorizing every request as if it originated externally.
*   **Integration of Best Practices:** Organizations should leverage existing standards like **ISO/IEC 27001** (Information Security) and **ISO/IEC 42001** (AI Management) while adding specific controls like data integrity checks and anomaly detection for user behavior.

### 4. Engineering and Governance Best Practices
To secure AI, the document suggests a shift in how teams are structured and how software is developed.
*   **Cross-Functional Teams:** A key recommendation is to **mix Data Scientists with Software Engineers**. Data scientists must learn secure, maintainable coding, while engineers must understand data science-specific risks.
*   **AI-Specific Engineering:** Beyond standard software testing, AI development requires monitoring for **model drift, data lineage, and model's "robustness"** (e.g., preventing evasion attacks).
*   **Governance & Compliance:** Organizations should implement rigorous monitoring of data provenance (where data comes from) and the use of "provenance" to track the lifecycle of the model.

### 5. Supply Chain & Provenance (The AI Supply Chain)
The document highlights a new complexity in the software supply chain:
*   **The AI Bill of Materials (AI BOM):** Similar to traditional software, AI requires tracking the "provenance" of training data and the models themselves.
*   **Complexity of the AI Supply Chain:** Because models rely on third-party datasets and pre-trained models, the "attack surface" includes the entire pipeline—from the raw data collection to the final deployment.