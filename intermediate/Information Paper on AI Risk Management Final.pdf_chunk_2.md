This document segment outlines the framework and best practices for **Artificial Intelligence Model Risk Management (MRM)** within the banking sector. It focuses on how banks inventory, assess, develop, and manage the risks associated with both AI and conventional quantitative models.

Below are the key insights and facts categorized by functional area:

### 1. AI Inventory and Asset Management
Banks use inventories to track the lifecycle, usage, and interdependencies of AI models.
*   **Inventory Methods:** Most banks use sophisticated software systems to track AI usage, automate approvals, and identify interdependencies. A small minority still use spreadsheets, which is noted as a risk due to potential for outdated records and lack of advanced features.
*   **Key Data Captured:** Inventories include purpose, scope, jurisdiction, model type, output, risk rating, approvals, use of Personally Identifiable Information (PII), and responsible personnel.
*   **Third-Party AI:** For external models, banks track additional attributes like the provider, model version, and "model cards" (transparency documents).
*   **Jurisdictional Risk:** A critical insight is that AI approved in one jurisdiction should **not** be automatically approved in another, as data, assumptions, and contexts vary.

### 2. Risk Materiality Assessment
Banks use "Risk Materiality" to determine the depth of validation and monitoring required for a specific AI tool.
*   **Three Dimensions of Risk:**
    1.  **Impact:** The potential financial, operational, regulatory, or reputational damage to the bank and its stakeholders.
    2.  **Complexity:** The intricacy of the model or the novelty of the use case.
    3.  **Reliance:** The level of autonomy granted to the AI versus the level of "human-in-the-loop" oversight.
*   **Dynamic Review:** Risk materiality is not static; banks must periodically review and update these assessments as business environments and AI capabilities evolve.

### 3. Development and Deployment Standards
Banks apply rigorous standards to ensure AI is reliable, fair, and auditable.
*   **Core Focus Areas:** Key priorities during development include data management, model selection, robustness, stability, explainability, fairness, reproducibility, and auditability.
*   **Validation Strategies:** 
    *   **High-risk models:** Require independent validation/review prior to deployment.
            *   **Lower-risk models:** May undergo peer reviews.
*   **Post-Deployment:** Banks implement continuous monitoring to detect "model drift" (performance degradation) and "data drift" (changes in input data patterns) and maintain strict change management processes.

### 4. Data Management
Robust data management is identified as the essential foundation for AI.
*   **AI-Specific Data Requirements:** Beyond standard governance, banks focus on:
    *   **Representativeness:** Ensuring training data reflects real-world and "stressed" conditions.
    *   **Bias Mitigation:** Ensuring data engineering (processing, augmentation, labeling) is free of bias.
    *   **Data Pipelines:** Implementing controls to monitor the quality of data flowing into deployed models.
*   **Advanced Data Practices:**
    *   **Feature Marts:** Some banks use centralized repositories for "features" (attributes) to improve consistency and reduce engineering time.
    *   **Unstructured Data:** There is an increasing focus on managing unstructured data (text, images, audio) due to the rise of Generative AI.

### 5. Model Selection and Robustness
The document highlights the technical trade-offs inherent in AI development.
*   **The Complexity Trade-off:** Developers are often required to justify using complex models (like neural networks) over simpler ones (like logistic regression) by balancing performance gains against the loss of **explainability**. Some banks require "challenger models" to prove the complex model is actually superior.
*   **Robustness and Stability:** 
    *   **Overfitting Risk:** Banks focus heavily on preventing "overfitting" (where a model performs well on training data but fails in the real world).
    *   **Training-Testing Skew:** Banks strive to ensure the distribution of data used for testing is similar to the data used for training to avoid discrepancies in performance prediction.