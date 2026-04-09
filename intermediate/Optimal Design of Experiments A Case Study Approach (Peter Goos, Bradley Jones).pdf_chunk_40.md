This document segment provides a technical explanation of **Split-Plot Designs** within the context of experimental design. It focuses on the mathematical modeling, statistical estimation, and the varying levels of precision associated with different types of experimental factors.

Below are the key insights and facts categorized by subject matter.

### 1. Core Structure of Split-Plot Designs
A split-plot design is defined by two distinct types of experimental factors:
*   **Hard-to-Change Factors (Whole-Plot Factors):** These factors are applied to "whole plots." Their levels are difficult or expensive to change, so they are held constant across multiple runs within a single whole plot.
*   **Easy-to-Change Factors (Sub-Plot Factors):** These factors are applied to "sub-plots" (individual runs). Their levels are reset for every run within a whole plot.
*   **The Hierarchy:** The design creates a nested structure where multiple sub-plots exist within each whole plot.

### 2. The Statistical Model and Error Structure
The document defines the model for the response $Y_{ij}$ as:
$$Y_{ij} = f(x_{ij})\beta + \gamma_i + \epsilon_{ij}$$

*   **Components:**
    *   $f(x_{ij})\beta$: The model expansion containing all factor effects and the intercept.
    *   $\mathbf{\gamma_i}$: The **whole-plot effect** (random effect).
    *   $\mathbf{\epsilon_{ij}}$: The **residual error** associated with the $j^{th}$ run in the $i^{th}$ whole plot.
*   **Error Assumptions:** The whole-plot effects ($\gamma_i$) and residual errors ($\epsilon_{ij}$) are assumed to be independent and normally distributed with zero mean. They have variances $\sigma^2_\gamma$ and $\sigma^2_\epsilon$, respectively.
*   **Correlation:** Because multiple runs share the same whole-plot factor, the responses within a whole plot are **correlated**. This correlation is represented by a specific covariance matrix ($V$), where the off-diagonal elements (covariances) only exist for pairs of responses within the same whole plot.

### 3. Estimation Methodology
Because the responses are correlated, standard Ordinary Least Squares (OLS) is insufficient. The document recommends:
*   **Generalized Least Squares (GLS):** Using the covariance structure to account for the correlation.
*   **Estimation Methods:** 
    *   Use **REML (Restricted Maximum Likelihood)** or similar methods to estimate variance components.
    *   Use **REML** to estimate the $\sigma^2$ values.
*   **Software/Approach:** The document suggests using **GLS** and specifically mentions the use of **REML** for error terms and **Kenward-Roger** (implied via the context of uncertainty/degrees of freedom) or similar approaches to handle the covariance.

### 4. Key Findings on Precision and Inference
The document highlights how the split-plot structure affects the "power" or precision of statistical tests:
*   **Precision of Hard-to-Change Factors:** Tests for the "hard-to-change" factors (whole-plot effects) are generally less powerful because they are subject to the variability of the whole-plot error.
*   **Precision of Easy-to-Change Factors:** Tests for "easy-to-change" factors (sub-plot effects) are typically more precise because they are subject to the smaller residual error.
*   **The "Quadratic" Exception:** The document notes that while interaction effects and easy-to-change factors are usually estimated with high precision, the precision of quadratic terms depends on the experimental design and the specific structure of the covariance.

### Summary Table of Effects
| Effect Type | Source of Error | Relative Precision |
| :--- | :--- | :--- |
| **Whole-Plot (Hard-to-change)** | Whole-plot error ($\gamma$) | Lower |
| **Sub-Plot (Easy-to-change)** | Residual error ($\epsilon$) | Higher |
| **Interactions** | Residual error ($\epsilon$) | Higher |