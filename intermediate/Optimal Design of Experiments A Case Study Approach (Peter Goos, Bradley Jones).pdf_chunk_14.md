This document segment describes a case study in the field of **Optimal Design of Experiments (DOE)**, specifically comparing different experimental design types (D-optimal vs. I-optimal) and applying the results to a manufacturing problem regarding "Peel Strength."

Below are the key insights and facts categorized by subject matter.

### 1. Comparison of Experimental Designs (D-optimal vs. I-optimal)
The text provides a technical comparison between two types of optimal designs used to estimate model coefficients and predict responses.

*   **D-optimal Design Characteristics:**
    *   **Strength:** It is more precise at estimating specific factor effects (the individual impact of temperature, pressure, etc.).
    *   **Weakness:** It has a higher average prediction variance (0.66) and lower I-efficiency (73%).
    *   **Efficiency:** Its median relative prediction variance is 0.65.
*   **I-optimal Design Characteristics:**
    *   **Strength:** It is superior for estimating the **intercept** and **quadratic effects** (Temperature $\times$ Temperature, etc.). It is much better for making predictions across the experimental region.
    *   **Performance:** It achieves lower prediction variances (0.48) and covers 98% of the space with better precision. Its efficiency is higher in terms of prediction accuracy.
    *   **Structure:** It utilizes more points at the center/mid-range, as evidenced by the lower variance in its predictions.
*   **Key Metric:** The **relative efficiency (D/I)** of the designs is a central theme, specifically looking at how well one design predicts compared to the other.

### 2. Statistical Analysis of "Peel Strength" (The Case Study)
The document presents a practical application involving the control of "Peel Strength" in a manufacturing context, involving different suppliers.

*   **The Problem:** The goal is to find settings (Temperature, Pressure, Speed) that maintain a consistent "Peel Strength" across different suppliers (Supplier 1, 2, and 3) to ensure product quality.
*   **Key Variables:**
    *   **Factors:** Temperature, Pressure, and Speed.
    *   **Supplier Variability:** The interaction between "Speed" and "Supplier" is a critical finding.
*   **Primary Finding:** The interaction between **Speed** and **Supplier** is significant. Changing the speed of the machinery affects the peel strength differently depending on which supplier's material is being used.
*   **Regression Results:**
    *   At a pressure of 3.2 bar and a specific temperature, the peel strength can be adjusted by changing the speed.
    *   A significant "Speed $\times$ Supplier" interaction exists, meaning a speed that works for Supplier 1 might result in failed quality for Supplier 2.

### 3. Operational Decision-Making
The text moves from statistical analysis to industrial application:

*   **Strategy 1 (Adjustment):** One approach is to change the machine speed (e.g., to 26 cpm) depending on which supplier's material is currently loaded in the machine to maintain the target peel strength.
*   **Strategy 2 (Process Control):** The ultimate goal is to minimize the "Percent Out of Specification" (the amount of product that fails the peel strength test).
*   **Economic/Logistical Constraints:** The text implies a need for a robust process that is either easy to adjust (low cost of change) or insensitive to the supplier (low cost of error).

### Summary of Key Data Points
| Feature | D-Optimal Design | I-Optimal Design |
| :---					| :---					| :---					|
| **Primary Strength** | Estimating factor effects | Predicting responses/mean |
| **Prediction Variance** | Higher | Lower |
| **Key Interaction Found** | N/A | Speed $\times$ Supplier |
| **Target Metric** | Factor significance | Peel Strength consistency |