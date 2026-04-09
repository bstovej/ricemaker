This research memo, dated January 2025, explores the governance and structural challenges of determining which entities—government agencies, AI companies, or third-party organizations—are best suited to develop evaluations for AI model capabilities and safeguards.

Below are the key insights and facts extracted from the document.

### **1. Core Problem: The "Evaluation Dilemma"**
The memo identifies a fundamental tension in AI safety: the need for specialized expertise versus the need for impartial oversight.
*   **Conflicts of Interest:** AI companies face significant conflicts of interest when developing evaluations for their own products, potentially leading to favorable results or "sandbagging" (where models are trained to hide specific capabilities).
*   **Impartiality Risks:** Third-party evaluators may lack impartiality because they often depend financially on the very AI companies they are evaluating.
*   **The Expertise Gap:** Much of the technical expertise and data required to create high-quality evaluations resides in the private sector, making it difficult for governments to act alone.

### **2. Taxonomy of Development Approaches**
The authors propose four distinct models for how evaluations can be developed:

| Approach | Description | Primary Advantages | Primary Disadvantages |
| :---able | :--- | :--- | :--- |
| **AISI-Led** | AI Safety Institutes (AISIs) manage the process start-to-finish. | High security, independence, and access to classified data. | High cost; does not foster a broader ecosystem. |
| **Joint Development** | AISIs collaborate with contracted private experts. | Access to specialized expertise while maintaining oversight. | High coordination costs. |
| **Third-Party Grants** | Public or private funding for independent research/orgs. | Encourages innovation, flexibility, and experimental methods. | Difficult to maintain quality control and oversight. |
| **AI Company-Led** | AI companies develop their own evaluations. | Highly cost-effective; utilizes the highest level of model access. | Significant conflict of interest. |

### **3. Criteria for Selecting Developers**
The authors suggest a two-step sorting process based on two categories of criteria:

**Risk-Related Criteria:**
*   **Expertise Needs:** Does the evaluation require rare, highly specialized knowledge (e.g., virology for CBRN risks)?
*   **Information Sensitivity:** Does the development require access to classified or highly sensitive national security data?
*   **Urgency:** Does the risk require an immediate response (favoring the "quickest actor")?
*   **Incentive Alignment:** Does the developer have a genuine incentive to prevent risk, or are they driven by profit/impartiality?

**Method-Related Criteria:**
*   **Model Access:** Does the evaluation method require "model-neutral" tools, or does it require deep access to the model's architecture/weights (common in evaluating open-source models)?
*   **Deployment Stage:** Does the evaluation happen pre-deployment (protecting IP) or post-deployment?
*   **Cost:** The financial resources required to execute complex, resource-intensive testing.

### **4. Strategic Recommendations for a "Market-Based Ecosystem"**
To prevent a fragmented or biased landscape, the authors recommend that governments act as "market creators" through several measures:
*   **Accreditation:** Implementing accreditation for third-party evaluators to ensure quality.
*   **Mandates:** Requiring AI companies to develop certain specific evaluations.
*   **Brokering:** Acting as a bridge to facilitate relationships between third-party evaluators and AI companies.
*   **Standardization:** Establishing clear guidelines and providing public tools to lower the barrier to entry for new developers.

### **Key Terminology**
*   **AISIs:** AI Safety Institutes.
*   **CBRN:** Chemical, Biological, Radiological, and Nuclear risks.
*   **Model-Agnostic/Neutral:** Evaluations that can be applied to any AI model regardless of its specific architecture.
*   **Capability Elicitation:** The process of discovering and revealing "emergent" capabilities in a model that were not explicitly programmed.