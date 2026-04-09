This document review focuses on the **Artificial Intelligence Model Risk Management** segment provided, which outlines the frameworks, risks, and controls used by banks when deploying and managing AI, with a specific emphasis on the emerging challenges of Generative AI (GenAI).

### 1. AI Management in Production (General AI)
The document outlines a rigorous lifecycle for AI models once they are deployed into production environments.

*   **Automated Deployment (CI/CD):** Banks utilize Continuous Integration/Continuous Deployment pipelines to automate building, testing, and deploying. This reduces manual error and integrates essential checks for cybersecurity and compliance.
*   **Continuous Monitoring & "Drift":** Monitoring is critical to prevent "model staleness." Banks monitor for three specific types of drift:
    *   **Data Drift:** Changes in data distributions.
    *   **Concept Drift:** Changes in the relationship between input and output.
    *   **Model Drift:** General changes in the environment.
*   **Threshold-Based Management:** Banks use predefined and "tiered" thresholds. Early warning thresholds trigger alerts before significant deterioration occurs, while higher thresholds trigger retraining, redevelopment, or decommissioning.
*   **Change Management & Version Control:** Significant changes (e.g., altering model architecture) require formal approval. Version control must extend beyond code to include **data, hyperparameters, and model weights** to ensure reproducibility and the ability to "roll back" if necessary.
*   **Contingency & "Kill Switches":** For high-risk/mission-critical applications (like trading), banks maintain contingency plans (manual processes or alternative systems) and may employ "kill switches" to instantly deactivate AI that exceeds risk tolerances.

### 2. The Generative AI (GenAI) Landscape
The document notes that GenAI is in its early stages in banking, characterized by a shift from "specific-purpose" models to "general-purpose" models.

*   **Unique Risk Factors:**
    *   **Hallucinations & Uncertainty:** Higher complexity leads to unexpected behaviors and less stable performance.
    *   **Evaluation Difficulties:** Unlike conventional AI (which uses structured data and "ground truths"), GenAI uses unstructured data (text/images), making it harder to predict all possible permutations or verify accuracy.
    *   **Third-Party Dependency:** Banks rely heavily on external providers (e.g., OpenAI, Google), leading to a lack of transparency regarding the underlying training data and evaluation standards.
    *   **Explainability & Fairness:** There is currently a lack of established methods to explain GenAI outputs or rigorously assess fairness in a general-purpose context.

### 3. Risk Mitigation & Control Strategies
Banks are adopting specific technical and procedural "guardrails" to balance innovation with safety.

*   **Operational Strategies:**
    *   **Human-in-the-loop:** To manage hallucinations, banks currently limit GenAI to "assisting/augmenting" humans rather than fully autonomous customer-facing roles.
    *   **Pilot Frameworks:** Use of time-bound and user-limited experimentation to test real-world behavior.
    *   **Modular Architecture:** Investing in reusable modules like **Vector Databases** and **Retrieval Systems** to scale GenAI safely.
*   **Technical Controls (Guardrails):**
    *   **Input/Output Filters:** Using AI or rules to intercept toxic language, detect bias, or redact Personally Identifiable Information (PII) before it reaches the user or the model.
    *   **Grounding (RAG):** Implementing **Retrieval-Augmented Generation (RAG)** to anchor model outputs to a bank’s internal, verifiable knowledge base, thereby reducing hallucinations.
    *   **Security:** Mitigating data leakage through private cloud solutions, on-premise servers, and Data Loss Prevention (DLP) tools.
*   **Assessment Levels:** Advanced banks conduct three levels of evaluation:
    1.  **Standalone:** Evaluating the model itself via benchmarks.
    2.  **Functional:** Evaluating the model on specific bank tasks (e.g., retrieving info from a specific repository).
    3.  **End-to-End:** Evaluating the entire integrated system.

### Summary Fact Sheet
| Feature | Conventional AI Focus | Generative AI Focus |
| :--- | :--- | :--- |
| **Primary Risk** | Model/Data Drift | Hallucinations & Uncertainty |
| **Data Type** | Structured | Unstructured (Text, Images) |
| **Control Method** | Threshold-based monitoring | Input/Output Guardrails & RAG |
| **Governance** | Version control of code/weights | Human-in-the-loop & Pilot frameworks |
| **Deployment** | Specific use-case automation | Augmenting human capability |