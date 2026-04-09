Based on the document segment provided (which appears to be an excerpt from the **ISO/IEC DIS 27090** standard regarding AI security), here are the key insights and facts:

### **Core Theme**
The document distinguishes between **conventional cybersecurity attacks** and **AI-specific attacks**. While some attacks are traditional (like DoS or Supply Chain), AI-specific variations are harder to detect using generic security tools and require specialized, "built-in" architectural defenses.

---

### **1. Denial-of-Service (DoS) / Scaling Attacks**
*   **The AI-Specific Threat ("Sponge Attacks"):** Unlike traditional DoS attacks that focus on overwhelming network traffic, "Sponge attacks" target the computational resources of the AI model itself.
*   **Impact Fact:** A sponge attack can cause an AI system to consume up to **30 times more energy** and take up to **30 times longer** to process a single example compared to a typical query.
*   **Detection Challenge:** Detection cannot be an afterthought; it requires **per-query monitoring** of energy and time, which must be designed into the system's architecture from the beginning.
*   **Mitigation Strategies:** 
    *   Implementing "budgets" for time and energy (aborting queries that exceed them).
    *   Sizing the system capacity for **worst-case** resource consumption rather than average-case.

### **2. Supply Chain Attacks**
*   **The Vulnerability:** While data poisoning is a known supply chain risk in AI, this section highlights a more subtle hardware/software component risk: **Random Number Generators (RNGs).**
*   **Detection Challenge:** Attacks on RNGs are exceptionally difficult to identify because "hostile" generators can still pass standard statistical tests.
*   **Mitigation Strategy:** The primary defense is **provenance**—ensuring that all components (specifically RNGs) come from trusted sources and verifying their integrity.

### **3. Backdoor Attacks (Neural Network Backdoors)**
*   **The Threat:** Attackers can introduce architectural flaws or "backdoors" directly into the neural network structure.
*   **Vector of Attack:** These backdoors are often introduced via third-party models, such as downloading pre-trained models or using services like Machine Learning as a Service (MLaaS).
*   **Mitigation Difficulty:** Because these are embedded in the model architecture, they are harder to detect than traditional external threats.

### **Summary Table of Findings**

| Attack Type | Specific Threat Identified | Primary Vulnerability/Vector | Key Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **DoS (Denial of Service)** | "Sponge" attacks | High computational/energy consumption per query | Per-query monitoring & energy budgeting |
| **Supply Chain** | Compromised RNGs | Use of untrusted/third-party components | Use of trusted, verified sources |
| **Backdoor** | Architectural backdoors | Use of pre-trained models or MLaaS | Rigorous vetting of model origins |