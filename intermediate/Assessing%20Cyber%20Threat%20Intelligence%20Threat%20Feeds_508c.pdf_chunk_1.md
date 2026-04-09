This document, authored by Kimberly K. Watson in December 2020, provides a framework for organizations to evaluate the value of Cyber Threat Intelligence (CTI) feeds. The central thesis is that organizations often fail to assess CTI value properly because they focus solely on **Relevance** while neglecting **Usability**.

Below are the key insights and facts extracted from the text.

### The Core Framework for Assessment
To determine if a CTI feed is worth the investment, an organization must evaluate two primary dimensions: **Relevance** (does the data matter to us?) and **Usability** (can we actually use the data?).

#### 1. Dimension: Relevance
Relevance answers the question: *"Does this information help me make informed risk decisions regarding my specific assets and operations?"* It is broken down into three components:

*   **Applicability:** The data must directly relate to the organization’s specific mission, assets, and regulatory requirements. 
    *   *Pro-tip:* A key indicator of applicability is the provider's data source; feeds derived from organizations in the same sector are more likely to be applicable.
*   **Accuracy:** The information must have a documented level of confidence or correctness. Organizations must understand the "logic" (e.g., confidence scores or severity levels) used by the provider to ensure the data is reliable enough for their specific automated or manual processes.
*   **Timeliness:** The information must arrive in time to influence a decision. 
    *   *Note:* Timeliness is relative. A Security Operations Center (SOC) needs near-instant updates to block malware, whereas leadership needs slower, more contextual data for long-term strategic investments.

#### 2. Dimension: Usability
Usability answers the question: *"Can I access, process, and use this information to mitigate a threat in alignment with local policy?"* It is broken down into three components:

*   **Machine-Readability:** The data must be in a structured format (e.g., JSON, XML) that the organization's existing software can parse and process automatically.
*   **Consumability:** The data must be easily converted into operational information. For Indicators of Compromise (IOCs), this implies that the entire pipeline—from receipt to injection into security tools—should be automated to remain effective.
*   **Actionability:** The data must be capable of driving a decision within a useful timeframe. This requires the information to either have inherent characteristics (like confidence levels) or to be easily supplemented with context to support the decision-making process.

### Key Insights for Decision Makers
*   **The "Relevance Trap":** Most organizations focus only on whether the threat intelligence is "relevant" to their industry. However, a feed can be highly relevant but completely worthless if it is not machine-readable or arrives too late to be actionable.
*   **Automation is Essential:** For modern network defense (specifically regarding IOCs), usability is synonymous with automation. If the data cannot be automatically ingested and used to drive mitigation, its value is significantly diminished.
*   **Context is Critical:** To make CTI "actionable," an organization must be able to understand the "why" behind the data (the logic and confidence scores) or have the ability to quickly add context to it.
*   **Operational Tempo Matters:** When evaluating a feed, you must align the feed's delivery speed with your specific operational needs (e.g., tactical blocking vs. strategic planning).