This document is a technical excerpt from a solutions manual for **Montgomery’s *Design and Analysis of Experiments***. It focuses on the statistical application and mathematical derivation of **Analysis of Covariance (ANCOVA)**.

Below are the key insights and facts categorized by subject matter:

### 1. Experimental Case Study (Problem 15-17)
The document details an engineer's study on how cutting speed affects the rate of metal removal, while accounting for the "hardness" of the specimen as a covariate.
*   **Key Variables:** 
    *   **Dependent Variable ($y$):** Rate of metal removal.
    *   **Independent Variable (Factor):** Cutting Speed (1000, 1200, and 1400 rpm).
    *   **Covariate ($x$):** Hardness of the specimen.
*   **Statistical Findings:**
    *   **Hardness is significant:** The ANOVA table shows a $P$-value of **0.000** for Hardness, meaning hardness has a statistically significant impact on the rate of metal removal.
    *   **Speed is NOT significant:** The $P$-value for Speed is **0.872**, indicating that changing the cutting speed (within the tested range) does not significantly change the metal removal rate.
    *   **Outlier Detection:** Minitab identified **Observation 8** as an "unusual observation" due to a large standardized residual ($-2.20R$).

### 2. Mathematical Derivations for Adjusted Means (Problem 15-18)
The document provides the formulaic basis for calculating confidence intervals for **adjusted treatment means**.
*   **Concept of "Adjusted" Mean:** In ANCOVA, the mean is adjusted to account for the difference between the specific group's covariate mean ($\bar{x}_{i.}$) and the overall grand mean of the covariate ($\bar{x}_{..}$).
*   **Confidence Interval Formula:** The $100(1-\alpha)\%$ confidence interval is calculated using:
    $$\bar{y}_{i.adj} \pm t_{\alpha/2, a(n-1)-1} \cdot S(\bar{y}_{i.adj})$$
*   **Standard Error (SE) Calculation:** The standard error of the adjusted mean depends on the Error Mean Square ($MS_{Error}$), the sample size ($n$), and the distance of the group's covariate mean from the grand mean:
    $$S(\bar{y}_{i.adj}) = \sqrt{MS_{Error} \left[ \frac{1}{n_i} + \frac{(\bar{x}_{i.} - \bar{x}_{..})^2}{\sum (x - \bar{x}_{..})^2} \right]}$$

### 3. Comparison of Two Adjusted Means (Problem 15-19)
The text derives the formula for the **Standard Error of the difference** between any two adjusted treatment means ($\bar{y}_{adj.i} - \bar{y}_{adj.j}$). 
*   The formula expands the variance to account for the variance in both groups and the influence of the covariate's dispersion:
    $$S_{\bar{y}_{adj.i} - \bar{y}_{adj.j}} = \sqrt{MS_{Error} \left[ \frac{1}{n_i} + \frac{1}{n_j} + \frac{(\bar{x}_{i.} - \bar{x}_{..})^2 + (\bar{x}_{j.} - \bar{x}_{..})^2}{\sum (x - \bar{x}_{..})^2} \right]}$$

### 4. Operating Characteristic (OC) Curves (Problem 15-20)
The document touches upon the power of the test using **Operating Characteristic (OC) curves**.
*   **Parameter $\Phi^2$:** To use OC curves for the ANCOVA fixed-effects case, one must use the non-centrality parameter:
    $$\Phi^2 = \frac{\sum \tau_i^2}{n\sigma^2}$$
*   **Degrees of Freedom:** The test utilizes $a-1$ degrees of freedom in the numerator and $a(n-1)-1$ in the denominator.

### Summary Table of Key Minitab Stats (from the text)
| Source | DF | Adj SS | Adj MS | F | P-Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hardness** | 1 | 3019.3 | 3019.3 | 347.96 | 0.000 |
| **Speed** | 2 | 1.2 | 0.6 | 0.14 | 0.872 |
| **Error** | 11 | 8.7 | 8.7 | - | - |