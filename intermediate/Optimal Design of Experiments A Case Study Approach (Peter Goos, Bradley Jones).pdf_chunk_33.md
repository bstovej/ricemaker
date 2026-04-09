Based on the provided document segment, here are the key insights and facts regarding the polypropylene experiment and its statistical analysis:

### **1. Core Experimental Objective**
The study aimed to determine the factors affecting the **surface tension** of polypropylene, which is a critical metric for ensuring proper adhesion.

### **2. Key Scientific Findings (Model Results)**
Based on the mathematical models presented by Peter, the following factors have a direct impact on increasing surface tension (and thus better adhesion):
*   **Positive Correlations:**
    *   **EPDM:** Increasing the proportion of EPDM increases surface tension (a change from low to high level results in an increase of 5.96 units).
    *   **Power:** Increasing power (from 500W to 2000W) has a large positive effect (10.05 units).
    *   **Reaction Time:** Increasing time (from 2 to 15 minutes) has a moderate positive effect (3.24 units).
    *   **EVA:** The presence of EVA increases surface tension.
*   **Negative Correlations:**
    *   **Ethylene:** Increasing ethylene concentration decreases surface tension (-3.27 units).
/
    *   **Flowrate:** Increasing the flowrate has a small negative effect (-1.37 units).
*   **Gas Type Hierarchy:** The effectiveness of gases for surface tension is ranked as: 
    **Etching Gas > Activation Gas 1 > Activation Gas 2.**

### **3. Statistical Methodology & Insights**
The discussion highlights several advanced experimental design concepts:
*   **Coding and Interpretation:** The analysis used **coded factor levels** (where -1 represents the low level and +1 represents the high level). This allows for a standardized comparison of effect magnitudes.
*   **Categorical Variable Analysis:** To analyze the three-level "Gastype" factor, the researchers used **effects-type coding** with two dummy variables. 
    *   The sum of the coefficients for the categorical factor is constrained to zero, which helps manage collinearity.
    *   The "implied" coefficient for the third gas (Activationgas2) was calculated to be -5.5936.
*   **Significance Testing:** 
    *   While individual dummy variable p-values were used, Peter notes that a global test (the omnibus test) is necessary to determine the significance of the categorical factor as a whole.
    *   All primary factors (EPDM, Ethylene, etc.) showed statistically significant impacts.

### **4. Operational Constraints and Conflicts**
A tension exists between the "optimal" scientific result and "optimal" industrial application:
*   **The "Optimal" Setting (per the model):** High EPDM, low Ethylene, use of Etching gas, high power, and long reaction times (15 minutes).
*   **The "Industrial" Reality:** Marc notes that **Etching gas is expensive** and the long reaction time (15 minutes) may not be cost-effective or practical, implying a need to balance surface quality with production cost and speed.