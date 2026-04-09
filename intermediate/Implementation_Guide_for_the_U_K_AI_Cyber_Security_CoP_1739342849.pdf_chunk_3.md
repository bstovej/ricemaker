This document appears to be an excerpt from a **Code of Practice or a Security Framework for AI Systems**. It outlines structured principles, provisions, and specific controls designed to mitigate the unique risks associated with AI development and deployment.

The following are the key insights and facts extracted from the document.

### 1. Core Strategic Insights

*   **Shift from Traditional to AI-Specific Threat Modeling:** The document emphasizes that traditional cybersecurity models are insufficient. Organizations must adopt models (like MITRE ATLAS or OWASP AI Exchange) that specifically account for AI-centric attacks such as **data poisoning, model inversion, membership inference, and prompt injection.**
*   **The Danger of "Excessive Agency" and "Superfluous Functionality":** A recurring theme is the risk of over-provisioning. 
    *   **Excessive Agency:** AI "agents" that can act on other systems must be restricted by the principle of least privilege to prevent unauthorized data exfiltration.
    *   **Superfluous Functionality:** Keeping unused model capabilities (e.g., keeping image-processing capabilities active in a text-only chatbot) unnecessarily expands the attack surface.
*   **Proactive Governance via "Data Custodians":** Security is not just a technical task but a governance one. The document advocates for a multi-disciplinary approach involving **Data Custodians, legal experts, and privacy officers** to review usage, ensure compliance with Data Protection Impact Assessments (DPIA), and balance business needs against risk.
*   **Supply Chain Accountability:** Security is only as strong as the weakest third-party component. The framework mandates rigorous due diligence on external providers, requiring evidence of their adherence to the Code of Practice (CoP) and the use of trusted, verified repositories for models and datasets.

---

### 2. Key Facts & Technical Details

#### **Identified AI-Specific Threats**
*   **Inference/Extraction Attacks:** Model inversion and membership inference.
*   **Input Manipulation:** Prompt injection (direct and indirect), adversarial evasion, and serialization attacks.
*   **Data Integrity Risks:** Data poisoning and the use of biased or unverified external datasets.
*   **Systemic Risks:** "Agentic" system unpredictability, model drift, and the exploitation of "hallucinations" or incorrect outputs.

#### **Regulatory & Framework References**
The document relies on a heavy architecture of international and regional standards:
*   **Legal/Regulatory:** UK GDPR (specifically **Article 22** regarding automated decision-making), EU GDPR, and the DSIT AI Cybersecurity Code of Practice.
*   **Security Frameworks:** NIST AI Risk Management Framework (RMF), ISO/IEC 27001, and MITRE ATLAS.
*   **Industry Standards:** OWASP Top 10 for LLM Applications, OWASP AI Exchange, and NCSC (National Cyber Security Centre) guidance.

#### **Operational Controls & Methodologies**
*   **Threat Modeling Notations:** Recommends using standardized notations like **STRIDE** or **PASTA**.
*   **Access Control:** Mandates **Least-Privilege Access** and **Zero Trust** architecture principles for AI interacting with internal/external data sources.
*   **Continuous Monitoring:** Requires established processes for "Continuous AI Risk Monitoring," including the use of threat intelligence feeds to detect new attack vectors (e.g., new methods of bypassing safety guardrails via emoticons).
*   **Incident Reporting:** Suggests tailored templates for AI-specific risks (e.g., reporting sensitive data leakage or inappropriate model responses) and the use of centralized risk registries.

---

### 3. Summary of Application by Use Case
The document provides a "tiered" approach to security based on the complexity of the deployment:

| Use Case | Primary Security Focus |
| :--- | :--- |
| **Chatbot App** | Preventing prompt injection, data leakage, and restricting unused multimodal features. |
| **ML Fraud Detection** | Protecting against poisoning, evasion attacks, and ensuring compliance with GDPR Article 22. |
| **LLM Platform** | Managing complex ecosystems, including plugins, auxiliary models (RAG/RLHF), and third-party API security. |
| **Open-Access LLM** | Automating scans for trusted sources and implementing lightweight, checklist-based controls for smaller organizations. |