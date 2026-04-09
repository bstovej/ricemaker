This document segment from **ISO/IEC DIS 27090** provides a technical overview of two primary types of adversarial attacks on Machine Learning (ML) systems: **Data Poisoning Attacks** and **Evasion Attacks**.

Below are the key insights and facts categorized by attack type.

---

### 1. Data Poisoning Attacks
*Focus: Manipulating the training dataset to corrupt the model's learning process.*

#### **Nature and Risks**
* **Mechanism:** Attackers inject malicious data into training, validation, or testing sets to alter the model's behavior.
* **The "Trigger" Problem:** A major risk is the use of "triggers" (e.g., a ruler marker in a skin cancer image) that cause the model to misclassify specific inputs.
* **Targeted vs. Indiscriminate:** Targeted attacks are harder to detect because the "trigger" is not present in standard test datasets; the model behaves normally unless the specific trigger is present.
 **Data Ordering Attacks:** A specialized attack where the adversary manipulates the *order* in which data is analyzed by the training algorithm.

#### **Detection Techniques**
* **Integrity Checks:** Validating the accuracy, consistency, and provenance of datasets throughout their life cycle to detect unauthorized additions or deletions.
* **Anomaly Detection:** Using statistical methods to identify outliers or shifts in data distribution.
* **Micromodel Voting:** Training small models on disjoint datasets and using a "majority vote" to identify suspicious training instances.
* **Advanced Methods:** 
    * **Trigger Inversion:** Reconstructing injected backdoors to identify if a model is compromised.
    * **Activation Clustering:** Identifying data that is unrepresentative of the typical dataset by examining model activations.

#### **Mitigation Strategies**
* **Data Sanitization:** Pre-processing and cleaning datasets to remove identified outliers or malicious samples.
* **Model Ensemble & Robustness:** 
    * Using **Model Ensembles** (multiple models in protected environments) to identify when one model’s output deviates significantly from others.
    * Utilizing **Robust Loss Optimization** to penalize predictions made on adversarial examples.
* **Fine Pruning & Fine Tuning:** 
    * **Pruning:** Reducing model size to remove "non-essential" neurons that may have memorized malicious patterns.
    * **Fine Tuning:** Retraining the model on a clean dataset to overwrite poisoned patterns.
* **Zero Trust Principles:** Implementing "Assume Breach" (encryption, micro-segmentation) and "Least Privilege" (Just-in-Time/Just-Enough Access to training data).

---

### 2. Evasion Attacks (Adversarial Attacks)
*Focus: Manipulating input data during the inference/operation stage to cause misclassification.*

#### **Nature and Risks**
* **Mechanism:** Adding small, often imperceptible "perturbations" to an input (e.g., an image or malware code) that do not change the human-perceived meaning but force the AI to produce an incorrect output.
* **Attack Settings:**
    * **Perfect-Knowledge:** Attacker has access to the model's architecture and weights.
    * **Zero-Knowledge:** Attacker can only query the model and observe results (often using "surrogate models" to craft the attack).
* **Digital vs. Physical:** 
    * **Digital:** Altering bits in a file (e.g., changing malware code).
    * **Physical:** Altering the real world (e.g., putting stickers on a road sign to trick an autonomous vehicle).
* **Impact:** Can lead to compromised integrity (wrong classification) and degraded availability (system failure), potentially resulting in physical safety hazards (e.g., traffic accidents).

#### **Detection Techniques**
* **Supplemental Networks:** Building parallel networks specifically designed to analyze input distributions and identify deviations.
* **Explainable AI (XAI):** Using XAI to visualize how a model derives predictions; unexpected patterns in explanations can signal an evasion attack.

#### **Mitigation Strategies**
* **Adversarial Training:** Training the model on a mixture of clean and known adversarial examples (Note: This has high computational overhead and may lead to overfitting).
* **Randomized Smoothing:** Applying random perturbations to an input to "blur" the attacker's precision and certify the model's robustness.
* **Feature Denoising:** Using filters or "purifiers" to remove malicious perturbations from the input before it reaches the AI system.
* **Random Transformations (RT):** Implementing random input transformations to make it computationally too difficult for an attacker to calculate effective gradients.

---

### Summary Table of Key Concepts

| Feature | Data Poisoning | Evasion Attack |
| :--- | :--- | :--- |
| **Target Stage** | Training / Development | Deployment / Operation |
| **Primary Goal** | Corrupt the model's "knowledge" | Trick the model into a wrong decision |
| **Key Vulnerability** | Trust in training data/labels | Sensitivity to input perturbations |
| **Core Defense** | Data integrity & provenance | Robustness & input sanitization |