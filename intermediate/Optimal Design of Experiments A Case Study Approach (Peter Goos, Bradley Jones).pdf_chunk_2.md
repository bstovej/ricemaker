This document appears to be a draft or excerpt from a textbook titled *Optimal Design of Experiments*. It features a dialogue between two characters, Brad and Peter, who use a practical example (comparing the thickness of cables from two different machines) to demonstrate the principles of experimental design.

Here are the key insights and facts extracted from the text:

### 1. Core Statistical Principle: Optimal Sample Allocation
The central theme of the document is determining how to divide a fixed total number of observations ($n$) between two groups to minimize the variance of the difference between their means ($\bar{X}_1 - \bar{X}_2$). 

*   **The Impact of Variance:** The optimal way to split a sample depends entirely on whether the variances ($\sigma^2$) of the two groups are equal or unequal.
*   **The Rule of Compensation:** When variances are unequal, the optimal design requires allocating **more** observations to the group with the **higher** variance to "compensate" and prevent the total variance of the difference from becoming too large.

### 2. Key Experimental Findings (Case Studies)

The document presents three specific scenarios using a total sample size of $n=12$:

**Scenario A: Equal Variances ($\sigma_1^2 = \sigma_2^2 = 1$)**
*   **Optimal Design:** A perfectly balanced design ($n_1=6, n_2=6$).
*   **Insight:** This confirms "traditional wisdom" that when group variances are identical, a 50/50 split is the most efficient.

**Scenario B: High Variance Imbalance ($\sigma_1^2 = 1, \sigma_2^2 = 9$)**
*   **Optimal Design:** An unbalanced design ($n_1=3, n_2=9$).
*   **Efficiency Loss:** Using a balanced design ($6/6$) in this scenario is only **80% efficient** compared to the optimal design, because the variance of the balanced design is 25% higher than the optimal one.

**Scenario C: Low Variance Imbalance ($\sigma_1^2 = 1, \sigma_2^2 = 2$)**
*   **Optimal Design:** A slightly unbalanced design ($n_1=5, n_2=7$).
*   **Insight:** As the ratio of variances approaches 1:1, the optimal design moves back toward a balanced 50/50 split.

### 3. Mathematical Observations
*   **Invariance of Design Choice:** Peter notes a crucial mathematical fact: the absolute value of $\sigma^2$ does not change the optimal design or the relative efficiency of the options; it only scales the absolute values of the variances.
*   **Efficiency Calculation:** Efficiency is calculated by dividing the variance of the optimal design by the variance of the alternative design (e.g., $\text{Var}_{\text{optimal}} / \text{Var}_{\text{alternative}}$).
*   **Robustness of Unbalanced Designs:** The text notes that "you don’t lose much" if you use a design that is only slightly unbalanced; the efficiency remains high (e.g., 97.2% in the first scenario).

### Summary Table of Scenarios
| Variance Ratio ($\sigma_1^2 : \sigma_2^2$) | Optimal $n_1$ | Optimal $n_2$ | Design Type |
| :--- | :--- | :--- | :--- |
| **1 : 1** | 6 | 6 | Balanced |
| **1 : 2** | 5 | 7 | Slightly Unbalanced |
| **1 : 9** | 3 | 9 | Highly Unbalanced |