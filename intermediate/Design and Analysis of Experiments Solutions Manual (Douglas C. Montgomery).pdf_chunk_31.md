Based on the provided technical text and data, here is a structured summary of the key findings and mathematical proofs.

### 1. Optimization and Design of Experiments (DOE)
The document outlines a process for optimizing manufacturing variables (specifically regarding thickness/density) using a response surface methodology.

*   **Objective:** To find the optimal settings for factors $x_1$ and $x_2$ to minimize/maximize a response (e.g., thickness) while maintaining stability.
*   **Key Parameters:**
    *   **Factors:** $x_1$ and $x_2$ (e.g., pressure and temperature).
    *   **Response:** $y$ (Thickness or weight).
*   **Model Type:** The use of a second-order polynomial model is evidenced by the presence of quadratic terms ($x_1^2, x_2^2$) and interaction terms ($x_1x_2$).
*   **Optimization Criterion:** The text suggests an approach where the goal is to keep the response within a specific target range (e.g., $45 \pm 2$ units) by adjusting the center point of the design.

### 2. Statistical Analysis of Variance (ANOVA) and Regression
The text provides evidence of standard regression analysis used in Design of Experiments:
*   **Model Equation:** $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12} x_1 x_2 + \beta_{11} x_1^2 + \beta_{22} x_2^2 + \epsilon$.
*   **Model Adequacy:** The "Lack of Fit" test is used to ensure the model adequately describes the relationship. A non-significant Lack of Fit ($p > 0.05$) is desired.
*   **Significance of Terms:** Terms are evaluated using $p$-values to determine which factors ($x_1, x_2$) and interactions are statistically significant.
*   **Residual Analysis:** Standard diagnostic plots (Normal Plot of Residuals, Residuals vs. Predicted, and Residuals vs. Scale) are used to verify the assumptions of normality, constant variance, and independence.

### 3. Mathematical Proofs (Block Design and Rotation)
The document contains mathematical derivations related to experimental design efficiency:

#### **A. Rotatability in Design**
A design is **rotatable** if the variance of the predicted response $\hat{y}$ depends only on the distance from the design center, not on the direction. 
*   **Condition:** For a second-order design, rotatability is achieved when the ratio of the $x_1^2$ coefficient to the $x_1x_2$ coefficient follows a specific constant related to the number of factors.
*   **Property:** $\text{Var}(\hat{y}(x)) = \sigma^2 [1 + \text{constant} \cdot (x^T(X^T X)^{-1}x)]$.

#### **B. Orthogonality in Block Designs**
The text discusses the properties of **Orthogonal Arrays (OA)**.
*   **Definition:** An array is orthogonal if, for any two columns, all possible combinations of levels occur an equal number of times.
*   **Application:** This ensures that the effect of one factor can be estimated independently of the effects of other factors, reducing the variance of the parameter estimates.

### 4. Summary of Experimental Results (Sample)
*   **Process Stability:** The use of "Control Charts" and "Control Limits" (as seen in the $45 \pm 2$ example) indicates a focus on Six Sigma/Quality Control methodologies.
*   **Experimental Design:** The use of **Central Composite Design (CCD)** or **Box-Behnken Design (BBD)** is implied by the structure of the quadratic model and the mention of center points to estimate pure error.