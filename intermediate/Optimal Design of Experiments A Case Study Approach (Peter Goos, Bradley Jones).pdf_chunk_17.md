This document describes a case study in **Design of Experiments (DOE)**, specifically focusing on optimizing a chemical yield within a constrained, irregular experimental region.

### **Key Facts**

**1. The Chemical Process**
* **Reaction Mechanism:** The process follows a sequential reaction: $A \rightarrow B \rightarrow C$.
* **Goal:** To maximize the yield of product **B**.
* **The Challenge:** 
    * **Low Temperature/Time:** Insufficient conversion of reactant $A$ to product $B$.
    * **High Temperature/Time:** Excessive reaction time causes product $B$ to convert into unwanted byproduct $C$.

**2. The Experimental Parameters**
* **Factors:** Time (seconds) and Temperature (Kelvin).
* **Initial Design (Failed):** A 3x3 full factorial design (central composite design). It failed because it included "impractical" settings (e.g., 500K was too low; 650s at 550K was too high).
* **New Design Parameters:**
    * **Time Range:** 360 to 720 seconds.
    * **Temperature Range:** 520 to 550 K.
* **Constraints:** The feasible region is irregular and bounded by two linear inequality constraints:
    * **Lower Bound:** $0.03 \times \text{Time} + \text{Temperature} \geq 539.8$
    * **Upper Bound:** $0.09 \times \text{Time} + \text{Temperature} \leq 587.8$

**3. The Optimization Methodology**
* **Model Type:** A full **third-order model** (including cubic terms and interaction terms like $x_i x_j^2$) was used instead of a standard quadratic model.
* **Design Type:** A **D-optimal design** was implemented using 15 experimental runs (including replicates) to account for the irregular constraints.

**4. Results and Success**
* **Yield Improvement:** The new experimental approach successfully identified a setting (360s, 545K range) that achieved a **62.1% yield**, representing a significant increase over previous attempts.

---

### **Key Insights**

* **The Limitation of Standard Designs:** The document highlights that "standard" experimental designs (like a 3x3 factorial) can fail when the "design space" is restricted by physical or chemical constraints (i.e., you cannot use all possible combinations of factors because some lead to undesirable side reactions or impossible conditions).
* **Importance of Model Complexity:** Moving from a quadratic model to a higher-order (third-order) model allowed the researchers to better capture the behavior of the reaction, particularly at the edges of the operating window.
* **Constraint-Based Optimization:** The success of the project relied heavily on defining the "feasible region" mathematically. By treating the temperature and time constraints as boundaries, the researchers could use D-optimal design to focus resources on the area most likely to yield high results.
* **Efficiency in Resource Allocation:** Using a D-optimal design allowed the team to select a specific number of runs (15) that provided maximum information about the complex landscape, rather than wasting runs on "unproductive" parts of the design space.