This document is a technical report by the **Microsoft AI Red Team** detailing their experience conducting red teaming operations on over 100 generative AI (GenAI) products. It outlines their methodology, the evolving threat landscape, and practical lessons for securing AI systems.

Here are the key insights and facts extracted from the document:

### **1. Core Methodology: The AI Threat Model Ontology**
To standardize their testing, Microsoft uses a specific "ontology" to deconstruct attacks. Instead of just looking for bugs, they model the entire attack chain:
*   **System:** The end-to-end application or model being tested.
*   **Actor:** The person emulating the threat (can be **adversarial**, like a scammer, or **benign**, like a confused user).
*   **TTPs (Tactics, Techniques, and Procedures):** The specific methods used (e.g., prompt injection, reconnaissance).
*   **Weakness:** The underlying vulnerability (e.g., insufficient safety training).
*   **Impact:** The downstream result (e.g., data exfiltration for **Security** or hate speech for **Safety/RAI**).

### **2. Key Insights & Lessons Learned**
The report highlights eight main lessons, with the following being the most significant:

*   **Simple attacks often beat complex ones:** A major insight is that "real attackers don't compute gradients, they prompt engineer." While academic research focuses on complex, mathematically heavy gradient-based attacks, real-world attackers use simple, manually crafted "jailbreaks" (e.g., *Skeleton Key* or *Crescendo*) because they are cheaper, easier to scale, and do not require full access to the model's internal weights.
*   **Context is everything (Capabilities vs. Application):** Red teaming should not just look at what a model *can* do, but *where* it is used. 
    *   *Capability:* A larger model can decode Base64; a smaller one cannot.
 effectively testing a smaller model for Base64 attacks is a waste of resources.
    *   *Application:* An LLM used for creative writing is lower risk than the same LLM used to summarize medical records.
*   **Red Teaming $\neq$ Safety Benchmarking:** Benchmarks are useful for comparing model performance on known datasets, but they are static. Red teaming is dynamic and essential for discovering **novel harms** (new types of risks that don't exist in old datasets) and **contextual risks** (risks specific to a certain deployment).
*   **The "Agentic" shift increases risk:** As AI moves from simple models to "agents" and "copilots" that can access tools, databases, and external APIs, the attack surface expands significantly. This introduces traditional security risks (like SSRF—Server-Side Request Forgery) into the AI domain.
*   **Automation is necessary for scale:** Because the volume of AI products is increasing too fast for manual testing, Microsoft uses **PyRIT**, an open-source Python framework, to automate parts of the red teaming process.

### **3. Notable Case Study: Vision Language Model (VLM) Vulnerability**
The report provides a specific example of a successful "jailbreak" using a VLM:
*   **The Attack:** While the model would refuse a text-only prompt asking for illegal instructions (e.g., "How do I commit identity theft?"), it would comply if those same instructions were **overlaid as text onto an image**.
*   **The Finding:** This revealed that the model's safety guardrails were much weaker against visual inputs than text-only inputs.

### **4. Summary of Operational Facts**
*   **Scope:** Over 80 operations covering more than 100 products.
*   **Product Breakdown:** The tested products include Models (24%), Plugins (16%), Apps and Features (45%), and Copilots (15%).
*   **Shift in Focus:** Since 2021, there has been a documented increase in operations specifically probing for **Safety (RAI) impacts** alongside traditional security vulnerabilities.
*   **The "Never-Ending" Nature of AI Security:** The authors conclude that because AI capabilities and applications are constantly evolving, the work of securing these systems is a continuous process that will never be "complete."