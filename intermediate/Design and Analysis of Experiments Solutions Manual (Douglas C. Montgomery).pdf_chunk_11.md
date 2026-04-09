Based on the provided technical documents, here is a summary of the key information regarding the statistical experiments and solutions described:

### **1. Experimental Analysis & Findings**
The documents detail several experimental scenarios, focusing on ANOVA (Analysis of Variance) and the handling of missing data in randomized block designs.

*   **Potency/Process Optimization (Problem 4-12):** 
    *   An experiment was conducted to determine the effect of stirring speed and temperature on potency. 
    *   The results indicated that the **stirring speed was significant**, while the **temperature was not significant**.
    *   The analysis utilized the $F$-test (ANOVA) to evaluate the significance of these factors.

*   **Grain Processing (Problem 4-13):**
    *   The study examined the effect of two factors (stirring and temperature) on the potency of a product.
    *   Key result: The stirring speed had a statistically significant effect, whereas temperature did not.

*   **Aluminum/Material Strength (Problem 4-14):**
    *   An experiment evaluated the impact of different chemical concentrations on the strength of an aluminum alloy.
    *   The results showed that the **concentration was significant**, but the **temperature was not significant**.

### **2. Statistical Methodologies**
The text outlines advanced techniques for managing experimental errors and incomplete datasets:

*   **Handling Missing Data in Randomized Block Designs:** 
    *   The documents provide mathematical solutions for estimating missing values in cases where one or more observations are lost.
    *   **Iterative Approach:** A method is described where initial estimates for missing values are made and then refined using the residuals of the model.
    *   **Simultaneous Equations:** For two missing values, a system of simultaneous equations is derived from the Sum of Squares (SS) equations. This involves differentiating the $SS$ with respect to the missing values to find the minimum.
    *   **Complexity Differentiation:** The documents provide specific formulas for estimating missing values when they are in the same row/column versus different rows/columns of a design matrix.

*   **Error Estimation:** 
    *   The text demonstrates how to calculate the **Expected Mean Square (EMS)** and use it to determine the significance of treatment effects.
    *   The use of **Residual Analysis** (Normal Probability Plots) is mentioned as a method to check the assumption of normality in experimental data.

### **3. Mathematical Formula Summary**
The text provides the basis for calculating estimates for missing values ($\hat{y}_{ij}$) by setting:
$$\frac{\partial (SS_{Error})}{\partial y_{missing}} = 0$$
This approach allows the researcher to treat the missing values as parameters to be estimated, effectively "plugging" the gaps in the data matrix to maintain the balance of the design.