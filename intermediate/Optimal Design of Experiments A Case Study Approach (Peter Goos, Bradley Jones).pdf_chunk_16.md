Based on the provided document segment (which appears to be from the book *Optimal Design of Experiments: A Case Study Approach*), here are the key insights and facts categorized by topic.

### 1. Experimental Design Optimality Criteria
The text compares different mathematical approaches to selecting the "best" experimental design:
*   **I-optimal Design:** This design minimizes the **average relative variance of prediction** across the experimental region. It is specifically noted as being more appropriate for **response surface experiments** because its focus is on prediction accuracy.
*   **G-optimal Design:** This design seeks to minimize the **maximum prediction variance** over the experimental region. However, the text notes a significant drawback: minimizing the maximum variance often leads to increased prediction variance in more than 90% of the rest of the experimental region.
*   **D-optimal Design:** While not detailed extensively in this specific snippet, the summary indicates that D-optimal designs focus on **factor-effect estimation** and are most appropriate for **screening experiments**.
*   **Composite/Compound Criteria:** In complex scenarios with multiple goals, researchers use weighted averages of different criteria (e.g., combining D-, I-, and G-optimality).

### 2. Statistical Validity and Error Independence
A major portion of the text focuses on the requirements for **Ordinary Least Squares (OLS)** estimation to be valid:
*   **The Independence Assumption:** For OLS to be the "best possible estimator," random errors ($\epsilon$) must be statistically independent.
*   **The Danger of "Hard-to-Change" Factors:** If certain factors are difficult or expensive to change, experimenters often change them in a systematic order rather than a random one. This creates "clusters" of correlated errors, making OLS inference inappropriate.
*   **Solutions for Dependencies:**
    *   When factor levels are hard to change, **split-plot** or **two-way-plot** designs should be used instead of standard designs.
    *   To ensure independence, all factor levels should be set independently for every run.
*   **Heterogeneity:** Variations in batches or time (e.g., day-to-day changes) can introduce errors. Use of blocking or recognizing these variations is necessary.

### 3  **Experimental Regions and Geometry**
*   **Cuboid/Box Designs:** The text discusses "cuboid" regions (where factors are bounded by independent limits) and "spherical" regions.
*   **Design Regions:**
    *   **Cuboid:** Defined by $x$ values within a specific range (e._g., $-1$ to $+1$).
    *   **Spherical:** Defined by a radius where the sum of the squares of the factors is less than or equal to a constant.
*   **Moments/Matrices:** The text references the use of moment matrices and the calculation of variance/covariance in the context of experimental design.

### 4. Experimental Modeling and Tools
*   **Polynomial Models:** The text discusses using quadratic (second-order) models to capture curvature in experimental data.
*   **Diagnostic Tools:** 
    *   **FDS (Functionally Distributed Statistics):** Used for analyzing results.
    *   **FDS Plots/Variance Plots:** Used to visualize the variance of predictions across the experimental space.
*   **Complexity:** The text notes that as models move from linear to quadratic, the complexity of the design increases.

### 5. Key Terminology/Glossary from the Text
*   **Efficiency:** A measure of how well a design uses the available experimental runs.
*   **Predictive Variance:** The error associated with the prediction at a specific point in the design space.
*   **Regression Coefficients:** The values being estimated in the mathematical model of the experiment.