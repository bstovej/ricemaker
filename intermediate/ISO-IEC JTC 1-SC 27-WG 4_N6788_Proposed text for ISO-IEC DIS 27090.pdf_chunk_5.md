This document segment (part of the ISO/IEC DIS 27090 draft) provides a technical breakdown of various security threats to Artificial Intelligence (AI) and Machine Learning (ML) models. It details the mechanics of each attack, the potential consequences, and strategies for detection and mitigation.

Below are the key insights and facts categorized by the specific threat types discussed.

### 1. Membership Inference Attacks
*   **Description:** An attacker attempts to determine whether a specific data sample was part of the model's training dataset. This is done by using "shadow models" to train a meta-classifier that recognizes the difference in how a model behaves on training data versus unseen data.
*   **Variations:** **Property Inference Attacks** are a subset where the attacker aims to infer general properties of a group within the dataset rather than a specific individual.
*   **Impact:** High risk to privacy and confidentiality. For example, in healthcare, confirming a person's data was in a dataset could reveal a specific medical diagnosis (PII exposure).
*   **Mitigation:** 
    *   **Differential Privacy (DP):** Adding random noise to statistics to ensure outputs don't change significantly based on one individual's presence.
    *   **Techniques:** Data shuffling, minimizing training data, limiting query frequency, and obfuscating confidence scores.
    *   **Zero Trust:** Applying "least privilege" and "verify explicitly" to all inputs and outputs.

### 2. Model Exfiltration (Model Stealing)
*   **Description:** A reverse-engineering or "oracle" attack where an adversary recreates a functional replica of the original model. This is achieved either by stealing weights/code (partial knowledge) or by querying an API with numerous inputs and observing outputs (zero knowledge).
*   **Impact:** Theft of Intellectual Property (IP) and loss of competitive advantage. Crucially, an exfiltrated model can be used to "test" and develop **evasion attacks** against the original production model.
*   **Detection:** Using User Behavior Analytics (UBA) to identify unusual query distributions or high-frequency requests from a single caller.
*   **Mitigation:** Throttling queries, encrypting model parameters, and using **model watermarking** to protect IP.

### 3. Model Inversion Attacks
*   **Description:** An attack that exploits model outputs (specifically high confidence scores) to reconstruct or recover features of the original training data.
*   **Impact:** Can lead to a permanent compromise of training data confidentiality, such as reconstructing a human face from a facial recognition system or extracting sensitive attributes (e.g., social security numbers) from LLMs.
*   **Detection/Mitigation:** Similar to exfiltration; focus on monitoring the "prediction space" being explored by users and limiting the rate/number of queries.

### 4. Direct Model Poisoning
*   **Description:** Unlike "data poisoning" (which targets the dataset), this targets the **engineering pipeline**. It involves manipulating the code, the training pipeline, or the model structure itself during development or operation.
*   **Transfer Learning Attack:** A specific type of poisoning where a supplier provides a model that has been pre-manipulated with unwanted behaviors.
*   **Mitigation:** Securing the development environment, using **Trusted Execution Environments (TEEs)**, and rigorous supply chain management.

### 5. Direct Model Theft
*   **Description:** The physical or digital theft of model parameters, executables, or memory contents through unauthorized access or side-channel attacks.
*   **Impact:** Results in the same functional loss as model exfiltration (loss of IP and confidentiality).
*   **Mitigation:** Protecting the development/operational environment and using **model obfuscation** (making the model's internal structure confusing and difficult to interpret).

---

### Summary of Recurring Security Principles
The document emphasizes three core **Zero Trust** pillars across almost all attack vectors:
1.  **Least Privilege/Access Control:** Limiting access to the model and its parameters.
2.  **Verification:** Continuous auditing of inputs and outputs (e.g., checking for malicious patterns in queries).
3.  **Defense in Depth:** Using a layered approach involving encryption, obfuscation, monitoring, and strict input/output controls to protect the integrity of the AI lifecycle.