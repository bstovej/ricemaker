This document segment details the development and structure of a **Common Reporting Framework for AI Incidents**. The overarching goal is to standardize and enhance the collection of detailed, complementary data regarding AI incidents across different jurisdictions, thereby aiding global policymaking and regulatory oversight.

Here is a breakdown of the key insights and facts.

---

### 💡 Key Insights

#### 1. Focus on Standardization and Depth
The framework shifts the reporting focus beyond basic incident reporting. It is designed to capture highly specific, technical, and contextual details—such as the **AI model version**, **training data provenance**, **autonomy level**, and **specific harm quantification**—ensuring policymakers receive nuanced, actionable data.

#### 2. Efficiency through Design Principles
To balance comprehensive detail with practical usability, the framework employs three key design features:
*   **Optionality:** Only **7 criteria are mandatory**, streamlining the reporting process while still allowing for the inclusion of supplementary (optional) information.
*   **Data Consistency:** The format utilizes predefined inputs (binary, multi-selection) to ensure that the collected data is consistent and comparable globally.
*   **Structured Categorization:** The 29 criteria are systematically organized into **8 distinct dimensions**, mirroring established international standards (like the OECD Framework for AI).

#### 3. Policy and Regulatory Value
The primary value of this framework is in its ability to enable deep analysis. By collecting standardized data, it aims to:
*   Identify high-risk AI systems and patterns of failure.
*   Provide insights into effective preventative and mitigation measures.
*   Help policymakers understand incident perceptions across different national and legal contexts.

---

### 🗂️ Key Facts and Technical Structure

#### 1. Framework Scope and Scale
*   **Total Criteria:** The framework is built upon a comprehensive set of **29 criteria**.
*   **Mandatory Criteria:** **7 criteria** are deemed fundamental and mandatory for every report.
*   **Purpose of Criteria:** The 29 criteria include both *recurrent* (common) information and *complementary* information (e.g., technical details on data, models, and tasks).

#### 2. The 8 Organizational Dimensions
The 29 criteria are logically segmented into 8 dimensions, providing a systematic way to classify incidents:

| Dimension | Focus Area | Examples of Data Captured |
| :--- | :--- | :--- |
| **1. Metadata** | Administrative details of the incident. | Title, description, date of occurrence, supporting materials. |
| **2. Harm Details** | Impact assessment and severity. | Harm type (e.g., physical, economic, reputational), severity, quantification of loss. |
| **3. People & Planet** | Affected parties and ethical dimensions. | Affected stakeholders (consumers, workers, government), adverse impacts on human rights, associated AI principles. |
| **4. Economic Context** | Deployment context and industry impact. | Industry (via ISIC codes), business function, and impact on critical infrastructure. |
| **5. Data and Input** | Input data quality and source. | Specific incident link to the **training data** (and how). |
| **6. AI Model** | Technical model characteristics. | Specific incident link to the **AI model** (and how), and usage rights. |
| **7. Task and Output** | How the AI operates and interacts. | Specific **tasks** the AI performs (e.g., prediction, content generation), and **maximum autonomy level** (e.g., human-in-the-loop). |
| **8. Other Information** | Ancillary details and remediation. | Details on actions taken (prevention, mitigation), and additional contextual notes. |

#### 3. Comparison to Existing Systems
The framework is presented as an evolution and complement to several existing global mechanisms:
*   **AI Incidents Monitor (AIM):** AIM currently tracks incidents and will integrate with this framework to enhance risk pattern identification.
*   **OECD Framework for AI Systems:** The structure of the common framework aligns with the OECD's existing classification dimensions (People & Planet, Economic Context, Data & Input, etc.).
*   **AIID (AI Incidents Database):** The framework incorporates elements from various established harm taxonomies (CSETv1 and GMF) to categorize AI failures.

---

### ✅ Summary of Core Functionality

In essence, the common reporting framework is a **multi-faceted diagnostic tool** for AI risks. It moves beyond simple "was there an incident?" reporting to ask:
1. **What failed?** (Model, data, task, or human?)
2. **How bad was it?** (Severity and measurable harm?)
3. **Who was affected?** (Stakeholders, and rights violated?)
4. **Where/Why did it happen?** (Context, industry, and deployment breadth?)