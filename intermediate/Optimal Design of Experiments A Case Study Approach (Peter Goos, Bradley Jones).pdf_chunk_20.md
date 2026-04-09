This document describes a case study in **Design of Experiments (DOE)**, specifically focusing on a **mixture experiment** used to solve a manufacturing quality issue in a rolling mill process.

### **Key Insights**

#### **1. The Core Problem**
*   **Quality Defect:** A manufacturing process was experiencing a **50% defect rate**. The critical quality specification was a "reflectivity" value of at least **5.5**.
*   **The Challenge:** The plant needed to identify which of five potential process variables were causing the fluctuations in reflectivity and find a setting that ensured consistent quality.

#### **2. The Statistical Complexity (Mixture vs. Factorial)**
*   **The Constraint:** The experiment involved three rolling mills. Because the total thickness reduction is a fixed quantity, the settings for the three mills are **interdependent** (the sum of their proportions must equal 100%).
*   **The Method:** Because the mills are not independent, a standard factorial design was insufficient. The team used a **mixture design** approach.
*   **The Findings:** The team discovered that the "Spray Volume" and "Oil-water ratio" factors were negligible, while the distribution of work between the three mills was the critical driver of quality.

#### **3. The Solution and Results**
*   **Optimal Configuration:** The researchers identified that shifting the workload to the third mill was key. The optimized setting was:
    *   **Mill 1:** 10% of the reduction workload.
    *   **Mill 2:** 10% of the reduction workload.
    *   **Mill 3:** 80% of the reduction workload.
*   **Outcome:** Implementing this change reduced the defect rate significantly, bringing the reflectivity quality into compliance and dropping the defect rate from 50% to **less than 5%**.

---

### **Key Technical Details**
*   **Variables Tested:** 
    *   Three proportional components (Mill 1, Mill 2, and Mill 3 proportions).
    *   Two independent factors (Spray volume and Oil-water ratio).
*   **Experimental Design:** A **D-optimal design** (specifically a 12-run design) was used to navigate the dependency between the mill percentages.
*   **Mathematical Model:** The team used **pseudocomponents** (implied by the use of percentages that must sum to 1) to transform the dependent mixture components into independent variables for analysis.
*   **Observation of Side Effects:** A notable secondary observation was that the optimal setting (heavy load on Mill 3) resulted in higher temperatures, which the team identified as a potential "lurk" or side effect of the process change.

### **Summary Table of Results**
| Metric | Before Optimization | After Optimization |
| :--- | :--- | :--- |
| **Defect Rate** | ~50% | < 5% |
| **Reflectivity** | Unstable/Below 5.5 | Consistent/Above 5.5 |
| **Primary Driver** | Uncontrolled variable distribution | Precise workload split (10/10/80) |