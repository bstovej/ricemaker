Based on the provided document, here is a summary of the key information regarding the **ISO/IEC Draft Standard for AI Security (ISO/IEC 27000 series/related)**, specifically focusing on the expert comments and technical feedback provided by the working group.

### **1. Document Overview**
The document is a collection of expert feedback (comments) on a draft international standard related to **AI Security**. The feedback is organized by "Expert Comments" from members of a technical committee (likely ISO/IEC JTC 1/SC 42).

### **2. Core Technical Themes in the Feedback**
The expert comments focus on several critical areas of AI security:

*   **Attack Surface & Impact:**
    *   There is a focus on the physical and societal impact of AI attacks. Experts suggest that the standard should address how attacks on AI can impact critical infrastructure (e.g., power grids, healthcare) and lead to "human-centric" consequences (e.g., physical harm or psychological impact).
    *   The scope should include the "consequences" of successful attacks, not just the methods.

*   **Adversarial Machine Learning (AML):**
    *   **Evasion Attacks:** Concerns regarding input manipulation (perturbations) to cause misclassification.
    *   **Poisoning Attacks:** The risks associated with corrupted training data or malicious fine-tuning.
    *   **Inference/Extraction Attacks:** The risk of attackers extracting sensitive training data or model parameters/intellectual property from the model's outputs.

*   **AI Lifecycle Security:**
    *   Security requirements must be integrated throughout the entire lifecycle: **Data Acquisition $\rightarrow$ Pre-processing $\rightarrow$ Training $\rightarrow$ Model Evaluation $\rightarrow$ Deployment $\rightarrow$ Monitoring/Retraining.**
    *   A major point of emphasis is **Data Integrity** and **Provenance** (verifying the origin and quality of training data).

*   **Robustness and Explainability (XAI):**
    *   Experts highlight the link between **Explainable AI (XAI)** and security. If a model is "black-box," it is harder to detect adversarial manipulations.
    *   The need for "Robustness Testing" (testing the model against adversarial examples) is a recurring theme.

### **3. Key Recommendations from Experts**
The following specific recommendations were extracted from the document:

*   **Standardization of Terminals/Metrics:** There is a call to standardize how "robustness" and "adversarial robustness" are measured and reported.
*   **Integration with Existing Standards:** The document emphasizes that this AI security standard should not exist in a vacuum but must align with existing ISO/IEC standards (like **ISO/IEC 27001** for Information Security Management and **ISO/IEC 22989/23053** for AI concepts and frameworks).
*   **Focus on "AI-Specific" Vulnerabilities:** Experts warn against treating AI security merely as a subset of traditional cybersecurity. They argue that AI introduces unique risks (e.g., stochastic behavior, data-driven logic) that traditional software security controls (like buffer overflow protection) do not cover.
*   **Human-Centricity:** A strong recommendation to include the impact of AI failures on human safety and fundamental rights.

### **4. Notable Technical Terminology Used**
*   **Adversarial Perturbations:** Small, often imperceptible changes to input data.
*   **Model Inversion:** An attack aimed at reconstructing training data.
*   **Data Poisoning:** Injecting malicious data into the training set.
*   **Robustness Quantification:** The mathematical measurement of a model's resistance to noise or attack.

### **Summary Conclusion**
The consensus among the experts is that while traditional cybersecurity principles (Confidentiality, Integrity, Availability) apply, the **AI-specific security layer** must focus heavily on **data integrity, model robustness, and the mitigation of risks arising from the black-box nature of deep learning.**