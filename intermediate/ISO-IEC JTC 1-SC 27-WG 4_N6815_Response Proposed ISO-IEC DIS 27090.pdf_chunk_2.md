Based on the provided document segments, which consist of expert technical reviews and commentary on the draft international standard **ISO/IEC DIS 27090** (concerning the security of AI systems), here are the key insights and facts.

### Key Insights

* **Focus on Technical Precision in AI Security:** The reviews go beyond simple grammatical corrections; experts are actively challenging the technical accuracy of the draft. For example, they contest the generalization that Federated Machine Learning always improves bandwidth and suggest more nuanced language regarding model poisoning detection.
* **The Need for LLM-Specific Frameworks:** A significant insight from the reviewers is that modern AI security cannot be treated as a monolith. There is a specific recommendation to create a dedicated subsection for **Large Language Model (LLM)** threats, covering unique attack vectors like prompt injection, fine-tuning, and Retrieval-Augmented Generation (RAG).
* **Blurring Lines Between Security and Privacy:** The reviewers identify a recurring issue in the draft where "security risks" and "privacy risks" are conflated. A core theme of the critique is the need to clearly distinguish between threats to **integrity/availability** (security) and threats to **confidentiality/data leakage** (privacy).
* **Complexity of XAI (Explainable AI) Evaluation:** The comments suggest that XAI should not just be a feature but a tool for evaluating how input changes affect output and quantifying feature contributions, indicating that XAI is being positioned as a security/audit mechanism.
* **Standardization of Terminology:** The document highlights a high level of scrutiny regarding technical nomenclature (e.g., "back door" vs. "backdoor," "train data" vs. "training data," and "synthesis" vs. "synthesise"). This underscores the importance of linguistic precision in international ISO standards to avoid ambiguity in global implementation.

### Key Facts

* **Document Subject:** The document is a collection of expert comments (by individuals such as Dr. Betina Tagle) on the draft standard **ISO/IEC DIS 27090**.
* **Scope of Attacks Mentioned:** The document references several specific AI-related attack vectors, including:
    * **Prompt Injection** (specific to LLMs).
    * **Data/Model Poisoning** (targeted and indiscriminate).
    * **Membership Inference Attacks.**
    * **Evasion Attacks** (perturbations invisible to the human eye).
    * **Backdoor Attacks.**
* **Identified Technical Terms/Acronyms:** The review involves several specialized AI/ML concepts, including **RAG** (Retrieval-Augmented Generation), **XAI** (Explainable AI), **OOD** (Out-of-Distribution), **Federated Machine Learning**, and **AIS** (AI Systems).
* **Specific Error Corrections:**
    * **Typos:** Corrections include "out data" $\rightarrow$ "output data" and "zero knowledge" $\rightarrow$ "zero-knowledge."
    * **Structural Suggestions:** Requests to clarify the "General" clause to focus specifically on Machine Learning and Deep Learning models.
    * **Inconsistencies:** The reviewers noted inconsistent use of periods in headers and inconsistent alignment in tables and bulleted lists.
* **Date of Review:** The documents are dated around **October/November 2024**.