This document segment outlines the regulatory boundaries of the **EU AI Act** regarding two specific types of biometric technologies: **Biometric Categorization** and **Real-Time Remote Biometric Identification (RBI)**.

Below are the key insights and facts categorized by regulatory theme.

---

### 1. Prohibited Biometric Categorization (Article 5(1)(g))
The AI Act prohibits AI systems that categorize individuals based on sensitive biometric data to infer specific protected characteristics.

*   **The Prohibited Scope:** The prohibition applies when the system's objective is to deduce or infer:
    *   Race or ethnicity.
    *   Political opinions.
    *   Trade union membership.
    *   Religious or philosophical beliefs.
    *   Sex life or sexual orientation.
*   **The "Individual" Requirement:** For the prohibition to apply, the system must categorize persons **individually**. Categorizing a whole group without looking at the individual is not prohibited.
*   **The "Strict Necessity" Rule:** Even if a system is "ancillary" to another service (like targeted advertising), it is prohibited if it is not "strictly necessary for objective technical reasons."
*   **Key Examples:**
    *   **Prohibited:** Using facial photos on social media to infer sexual orientation for targeted ads; using voice to deduce race; using tattoos to infer religious beliefs.

    *   **Permitted (Out of Scope):** Using biometric data for medical diagnosis (e.g., analyzing skin/eye color for cancer); labeling datasets to ensure diversity and prevent algorithmic bias; using biometric data for law enforcement to identify victims or suspects (within specific legal bounds).

### 2. Real-Time Remote Biometric Identification (RBI) (Article 5(1)(h))
The document outlines a strict prohibition on the use of "real-time" RBI by law enforcement in publicly accessible spaces, subject to very narrow exceptions.

*   **The Three Specific Exceptions:** Law enforcement may only use real-time RBI if it is strictly necessary for:
    1.  **Searching for victims:** Specifically for abduction, human trafficking, or sexual exploitation, or for finding missing persons.
    2.  **Preventing threats:** Addressing a specific, substantial, and imminent threat to life/physical safety or a foreseeable terrorist attack.
    3.  **Criminal investigations:** Identifying/localizing suspects for serious crimes (offenses punishable by a maximum of at least four years of imprisonment).
*   **Conditions for Use:** Any use of these exceptions must be authorized by **national legislation** and meet strict EU safeguards.

### 3. Key Technical Definitions & Distinctions
The document clarifies the legal boundaries between different biometric processes:

*   **Identification vs. Verification:**
    *   **Identification (Prohibited in real-time):** Comparing a person's data against a database to establish who they are (e.g., scanning a crowd to find a suspect).
    *   **Verification/Authentication (Not Prohibited):** Comparing data presented at a sensor to a specific record to confirm identity (e.g., using a fingerprint to unlock a phone or an e-gate at an airport).
*   **"Remote" vs. "Active Involvement":**
    *   **Remote:** Identifying people at a distance without their active participation (e.g., CCTV surveillance).
    *   **Active Involvement (Excluded from RBI prohibition):** Systems where the user consciously interacts with the sensor (e.g., using a biometric metro ticket or face scanning for building access).
*   **"Real-Time" vs. "Post-Event" (Retrospective):**
    *   **Real-Time:** Processing data instantaneously or without significant delay (before the person has left the area).
    *   **Post-Event (Post-RBI):** Analyzing video footage after an incident has occurred to identify an offender. This is **not** prohibited under Article 5(1)(h), but it is subject to "high-risk" AI regulations.

### 4. Summary of Legal Interplay
*   **High-Risk Classification:** AI systems used for biometric categorization (that are not prohibited) are classified as **high-risk** under the AI Act.
*   **Data Protection Alignment:** The AI Act works alongside the **GDPR** and the **Law Enforcement Directive (LED)**. It reinforces existing prohibitions against profiling that leads to discrimination based on sensitive personal data.