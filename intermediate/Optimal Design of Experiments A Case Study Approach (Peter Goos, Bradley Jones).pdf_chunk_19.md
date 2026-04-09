Based on the provided document segments from *"Optimal Design of Experiments: A Case Study Approach"* by Peter Goos and Bradley Jones, here are the key insights and facts categorized by subject matter:

### 1. Statistical Methodology & Design of Experiments (DoE)
*   **Causation vs. Correlation:** A fundamental advantage of designed experiments over observational studies is that designed experiments can establish **causation**, whereas observational studies can only establish **correlation**.
*   **Coordinate-Exchange Algorithm:** This algorithm is used to construct designs by replacing one coordinate in a design matrix at a time. When constraints are present, the algorithm must be modified to ensure the new values stay within allowable intervals.
*   **Optimality Criteria:** The algorithm uses specific criteria to determine the "best" new value, specifically the **D-criterion** (to maximize) or the **I-criterion** (to minimize).
*   **Statistical Significance:** The text illustrates the use of the **F-distribution** to test hypotheses. It notes that a p-value (e.g., 0.2743) indicates that a result could easily occur by chance, meaning there is no evidence to reject the null hypothesis regarding systematic effects.

### 2. Mixture Experiments
*   **Defining Characteristic:** In mixture experiments, the ingredients/factors are not independent because their proportions must **sum to a constant** (usually 1).
*   **Modeling Challenges:** 
    *   Because the sum of ingredients is constant, models for mixture problems generally **do not have an intercept (constant) term**, as such a term would be linearly dependent on the sum of the ingredients.
    *   **Process Variables:** These experiments often involve "process variables" (factors that can vary independently of the mixture). These variables can impact standard models and create complex interactions with the mixture components.
*   **Constraints:** Unlike standard experiments that assume a spherical or cubic experimental region, mixture experiments often involve nonlinear or inequality constraints (e.g., $x_1 + x_2 \leq 1$).

### 3. Case Study: The Rolling Mill Experiment
*   **The Problem:** An aluminum plant is facing a high **scrap rate (50%)**. The goal is to produce aluminum sheets with a **reflectivity of 5.5 or higher**. Sheets that fail this metric are dull or smudged and must be re-melted, which is costly and inefficient.
*   **The "Lurking Variable" Trap:** 
    *   Initial observations showed a strong positive correlation between **melt temperature** and **reflectivity**.
    *   Based on this correlation, the team attempted to raise the melt temperature.
    *   **The Result:** The experiment failed; increasing the temperature actually **increased the scrap rate**.
*   **Key Insight:** This case study serves as a "cautionary tale" about the dangers of relying on observational data (correlation) and the presence of "lurking variables" that can invalidate seemingly obvious conclusions.
*   **Controlled Factors:** The experiment involves controlling the ratio of oil to water in a coolant and the volume of coolant applied during the milling process.