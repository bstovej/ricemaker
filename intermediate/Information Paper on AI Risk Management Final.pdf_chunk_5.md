This review covers the provided document regarding **Artificial Intelligence Model Risk Management (MRM)**, specifically focusing on third-party AI risks, mitigation strategies, and technical definitions within a banking context.

### **Key Insights**

*   **The Fallibility of RAG:** While Retrieval-Augmented Generation (RAG) is a primary method used to ground Large Language Models (LLMs) in factual data to reduce errors, it is **not a silver bullet**. The document notes that even with external context provided, the possibility of "hallucinations" remains.
*   **Systemic Concentration Risk:** A critical insight regarding third-party AI is the emergence of **concentration risk**. Because multiple financial institutions (FIs) may rely on the same underlying foundational models, a failure or bias in one single third-party model could create a ripple effect across the entire financial sector.
*   **The Transparency Paradox:** There is a fundamental tension in third-party AI management: banks need transparency to perform risk assessments, but AI providers are often reluctant to disclose proprietary information regarding training data and algorithms. This "black box" nature is a primary hurdle in effective risk management.
*   **Integrated Risk Management:** AI risk cannot be managed in a vacuum. Effective AI MRM requires the integration of non-AI-specific controls, including **cybersecurity, data governance, legal/compliance, and third-party risk management.**
*   **Evolutionary Governance:** The document emphasizes that AI MRM is not a "set and forget" process. As the technology evolves, frameworks must be regularly reviewed, and risk management efforts must scale alongside the complexity of AI use.

---

### **Key Facts**

#### **1. Third-Party AI Risks & Mitigations**
*   **Primary Risks:** Unknown biases in pre-training data, data protection concerns, and concentration risks due to interdependencies.
*   **Mitigation Strategies for Banks:**
    *   **Compensatory Testing:** Rigorous testing using various datasets to detect bias and ensure stability.
    *   **Contingency Planning:** Developing backup systems or manual processes to handle vendor failure or service discontinuation.
    *   **Legal Safeguards:** Updating contracts to include "right to audit" clauses, performance guarantees, and notifications regarding AI implementation.
    *   **Awareness/Literacy:** Investing in staff training and conducting surveys with vendors to understand their AI development practices.

#### **2. Technical Definitions**
*   **Discriminative vs. Generative AI:** Discriminative models are used for **predictions** (e.g., credit default), whereas Generative models are used to **create content** (e.g., text, images).
*   **Types of "Drift":**
    *   **Data Drift:** A change in the statistical properties of the input data over time (measured by Population Stability Index - PSI).
    *   **Concept Drift:** A change in the relationship between input features and the target prediction (measured by Characteristic Stability Index - CSI).
    *   **Model Drift:** A broad term encompassing both data and concept drift that leads to performance degradation.
*   **Learning Methods:**
    *   **Supervised Learning:** Training on labeled datasets (input paired with a known output).
    *   **Unsupervised Learning:** Finding patterns in unlabeled data (e.g., clustering).

#### **3. Regulatory Context (MAS)**
*   **Regulatory Outlook:** The Monetary Authority of Singapore (MAS) is considering the release of **supervisory guidance** for all Financial Institutions (FIs) next year.
*   **Collaborative Efforts:** MAS is actively participating in industry-wide initiatives like **Project MindForge** to promote best practices in AI governance.