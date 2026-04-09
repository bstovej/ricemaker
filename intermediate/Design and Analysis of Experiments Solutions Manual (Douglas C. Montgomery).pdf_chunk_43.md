The provided text contains a series of solutions and explanations for various experimental design problems, likely from a textbook or course manual based on **Douglas Montgomery's "Design and Analysis of Experiments."**

The content covers advanced topics in **ANOVA (Analysis of Variance)**, specifically focusing on **Mixed Models**, **Split-Plot Designs**, and **Multi-Factorial Experiments**. Below is a summary of the key engineering and statistical concepts addressed in each section:

### 1. Mixed Models & Restricted Random Effects (Problems 14.2 - 14.3)
These sections deal with the complexities of models where some factors are **fixed** (levels are specifically chosen) and others are **random** (levels are a random sample from a larger population).
*   **Key Concept:** The "Univariate" vs. "Multivariate" approach to error terms. When a factor is random, it introduces a new error term into the model.
*   **Expected Value of Variance Components:** The solutions demonstrate how to calculate the variance components ($\sigma^2$) and identify which error term (e.g., $E(a)$ or $E(e)$) should be used as the denominator in the F-test.

### 2. Split-Plot Designs (Problems 14.13 - 14.15)
The text addresses scenarios where experimental units are not homogeneous, necessitating a split-plot structure (e.g., one factor is applied to a large plot, and another is applied to sub-plots).
*   **Key Concept:** The **Split-Plot ANOVA table**. The analysis identifies two distinct error terms:
    1.  **Whole-plot error:** Associated with the harder-to-change factor.
    2.  **Sub-plot error:** Associated with the easier-to-change factor.
*   **Practical Application:** The text uses examples involving manufacturing (e.g., thickness, temperature) to show how the F-test for the whole-plot factor must use the whole-plot error, while the sub-plot factor uses the residual error.

### 3. Complex ANOVA with Interaction (Problems 14.20 - 14.22)
These sections tackle advanced ANOVA problems involving multiple levels and interactions.
*   **Key Concept:** Determining the correct denominator for F-tests when dealing with multi-level interactions and varying error structures.
*   **Complexity:** The solutions demonstrate the use of the **Expected Mean Squares (EMS)** method to systematically derive which variance component should be used for testing each effect.

### Summary of Mathematical Procedures Used:
1.  **EMS (Expected Mean Squares) Calculation:** The primary tool used to determine the correct denominator for every F-ratio in the ANOVA table.
2.  **Variance Component Estimation:** Determining how much of the total variability is attributable to specific random factors.
3.  **Degrees of Freedom Adjustment:** Adjusting the error terms in split-plot designs to account for the hierarchical structure of the observations.

**Target Audience:** This material is intended for graduate-level students or professionals in Industrial Engineering, Statistics, or Quality Engineering studying experimental design.