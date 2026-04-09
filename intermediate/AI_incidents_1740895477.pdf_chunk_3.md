This document segment outlines components of a **Common Reporting Framework for AI Incidents**, developed by the OECD. Its primary purpose is to provide a comprehensive, standardized taxonomy for categorizing not only the *types* of incidents that occur involving AI systems but also the *specific nature* of the link (causality) between the AI system and the incident.

Here are the key insights and facts, grouped by topic:

---

### 💡 Key Insights and Facts

#### 1. Framework Scope and Goal
*   **Objective:** To establish a structured system for reporting and analyzing AI incidents to create a common global understanding of how AI fails and causes harm.
*   **Nature of Links:** The categories of involvement are not exhaustive, and the links between an AI system and an incident are **not mutually exclusive** (meaning multiple links may apply to a single incident).

#### 2. Taxonomies for System Definition (The "What" and "How")
The report requires classifying AI systems based on several technical and ethical parameters:

*   **Licensing/Usage:** Classification along lines of commercial use (e.g., non-commercial), usage model (open source/permissive, copyleft/share alike), and cost (free of charge).
*   **Core Functionality (AI Capabilities):** Systems are categorized by their task capability, such as:
    *   Recognition/object detection
    *   Forecasting/prediction
    *   Goal-driven organization
    *   Content generation
    *   Reasoning with knowledge structures/planning
*   **Autonomy Level:** Measures the level of human involvement required during operation (e.g., Low-action autonomy/human-in-the-loop; High-action autonomy/human-out-of-the-loop).
*   **Incident Response Stages:** Incidents can be classified by the phase of response required: Prevention, mitigation, ceasing, or remediation.

#### 3. Incident Causation: The Link to Failure (Table C.1)
This section provides the most detailed insight, categorizing *how* an AI system relates to an incident:

**A. Direct Involvement (The AI is the primary culprit):**
*   **Direct Cause:** The AI system is the primary reason for the incident due to a malfunction or erroneous output.
*   **Contributing Factor:** The AI system played a secondary or supportive role in causing the incident.

**B. Indirect Involvement (Failure in oversight or human processes):**
*   **Human Error:** Mistake made by the user, operator, or human supervisor.
*   **Overreliance:** The incident occurs because the user overdepends on the AI or intentionally misuses it, disregarding proper oversight.
*   **Developer Error:** The AI functions as intended, but human errors in its development lead to unintended outcomes (e.g., training on flawed data).
*   **Operator Error:** Unintended outcomes arise from the operator's lack of skills, incorrect system configuration, or improper application of the tool.
*   **Failure to comply with legal frameworks:** The AI operates correctly but violates existing laws (e.g., data protection laws).

#### 4. Summary of Failure Responsibility
The framework shifts the focus from simply blaming the machine to a nuanced analysis of responsibility across the lifecycle:

| Failure Category | Root Cause | Example (Conceptual) |
| :--- | :--- | :--- |
| **Malfunction** | The AI system's core programming or operation fails. | A self-driving car misinterpreting road signals. |
| **User/Operator Error** | Misunderstanding, misuse, or inadequate training of the human user. | An operator misinterpreting AI recommendations. |
| **Systemic/Developer Error** | Flaws in the design, data, or architecture of the AI itself. | Training an AI model on flawed data. |
| **Governance Failure** | Lack of legal compliance or ethical oversight. | Using facial recognition without consent (violating privacy laws). |

***

### Summary Table

| Element | Purpose | Key Categories |
| :--- | :--- | :--- |
| **Reporting Goal** | Standardize the definition and classification of AI-related harms. | Common Reporting Framework for AI Incidents. |
| **Direct Link** | AI is the primary cause. | Direct Cause, Contributing Factor. |
| **Indirect Link** | Cause involves human or external factors. | Overreliance, Human Error, Developer Error, Operator Error, Legal Non-Compliance. |
| **System Scope** | Defining the AI's capability and legal context. | Object Detection, Forecasting, Reasoning, Open Source, Copyleft. |
| **Autonomy** | Defining human involvement. | Human-in-the-loop (Low), Human-on-the-loop (Medium), Human-out-of-the-loop (High). |