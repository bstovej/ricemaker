This document segment, excerpted from *Optimal Design of Experiments: A Case Study Approach* by Peter Goos and Bradley Jones, discusses advanced experimental design strategies for handling **covariates**, **time-trend effects**, and **hard-to-change factors**.

The following are the key insights and facts categorized by topic:

### 1. Experimental Design and Covariates
*   **Definition of Covariates:** Covariate factors are characteristics of experimental units (e.g., the specific properties of a raw material) that are measurable but cannot be directly controlled by the experimenter. They can be continuous or categorical.
*   **The Benefit of Covariates:** Incorporating known covariate information into the experimental design reduces the standard error of factor-effect estimates compared to designs that ignore them.
*   **Time as a Covariate:** Time should be treated as a covariate if the researcher expects the response to "drift" or change over the duration of the experiment.
*   **Requirement for Independence:** To ensure experimental observations are independent, factor levels must be reset for every run, even if the level is the same as the previous run. Failing to do so results in **correlated observations**, which makes proper data analysis much more difficult or even impossible.

### 2. Split-Plot and Strip-Plot Designs
*   **Purpose:** These designs are recommended when it is difficult or costly to reset certain factor levels for every run (i.e., when "hard-to-change" factors are present). 
*   **Structural Mechanics:** 
    *   In a **split-plot design**, runs are grouped. The levels of "hard-to-change" factors only vary between groups, while "easy-to-change" factors vary within the groups.
    *   These designs involve **two levels of randomization**: one for the order of the groups (the master design) and a second for the order of runs within each group.
*   **Statistical Analysis:** 
    *   Because runs within a group are not independent (they are correlated), the model used is a **mixed model** (incorporating both fixed and random effects).
    *   Data must be analyzed using **Generalized Least Squares (GLS)** rather than Ordinary Least Squares (OLS), as OLS assumes independence that does not exist in split-plot structures.

### 3. Challenges of Time-Trends and Serial Correlation
*   **Trend-Robust Designs:** The text notes the difficulty in creating designs that are robust against time trends while remaining cost-efficient (minimizing the frequency of factor changes).
*   **Serial Correlation:** In experiments where runs occur in rapid succession, responses often exhibit serial correlation. The order of runs significantly impacts the precision of factor-effect estimates.
*   **Optimization:** Research has focused on finding run orders that are efficient for both main effects/interactions and second-order response surface models, even in the presence of serial correlation.

### 4. Case Study: NASA Langley Full-Scale Tunnel (LFST)
*   **The Scenario:** A study of a NASCAR Chevrolet Monte Carlo in a wind tunnel.
*   **The Factor Types:**
    *   **Hard-to-Change:** Front ride height and Rear ride height (requiring the tunnel to be shut down, wheel loads to be checked, and the car to be re-balanced).
    *   **Easy-to-Change:** Yaw angle (electronically automated) and Grille tape coverage (simple application of tape).
*   **Economic Efficiency:** The text highlights that a 50-run split-plot design can be more efficient/cost-effective than a standard 28-run design because it reduces the need to frequently stop and restart the wind tunnel to change the vehicle setup.
*   **Design Feature:** The use of **center points** (center points in the design) was included to check for non-linearity and to assist in detecting curvature.