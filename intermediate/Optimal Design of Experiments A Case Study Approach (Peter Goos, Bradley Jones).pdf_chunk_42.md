This document segment is an excerpt from a textbook titled *Optimal Design of Experiments: A Case Study Approach* by Peter Goos and Bradley Jones. It details a technical discussion regarding the implementation of a **two-way split-plot design** in an industrial manufacturing context.

Below are the key insights and facts extracted from the text.

### **1. Key Technical Insights**

*   **The Danger of Incorrect Randomization:** The text warns against the common practice of "completely randomizing" every design without accounting for logistical constraints. Analyzing a split-plot experiment as if it were a completely randomized design (CRD) leads to two critical errors:
    *   **False Positives:** Main effects and interactions of "hard-to-change" factors appear more statistically significant than they actually are (underestimated standard errors).
    *   **False Negatives:** Effects involving "easy-to-change" factors appear less statistically significant than they actually are.
*   **Complexity of Two-Way Split-Plot Designs:** Also known as **strip-plot**, **strip-block**, or **criss-cross** designs, these involve two layers of correlation. In this specific case, responses are correlated both within the same "lot" (assembly stage) and within the same "curing cycle" (curing stage).
*   **The Statistical Bottleneck (Degrees of Freedom):** A major insight provided is that a design with too few levels (e.g., only 4 curing cycles) makes it impossible to perform significance tests. With only 4 columns, there are only 3 degrees of freedom, which is insufficient to simultaneously estimate the column-to-column variation and the effects of the column factors.
*   **The GLS Approach:** The document recommends using **Generalized Least Squares (GLS)** to handle the complex variance-covariance matrix ($V$) inherent in two-way designs. The estimator used is $\hat{\beta} = (X'V^{-1}X)^{-1}X'V^{-1}Y$.

### **2. Case Study Facts: Battery Cell Production**

*   **The Problem:** A manufacturer (Rayovac) is experiencing issues with **Open Circuit Voltage (OCV)** in battery cells. High OCV causes cells to self-discharge, leading to poor performance.
*   **The Experimental Factors:**
    *   **Total Factors:** 6 factors (all at 2 levels).
    *   **Stage 1 (Assembly):** 4 factors. These are "harder" to change because they involve the production of the cells themselves.
    *   **Stage 2 (Curing):** 2 factors. These are "easier" to change but happen after the assembly stage.
*   **The Constraints:**
    *   **Batching:** The assembly process produces cells in batches (lots).
    *   **Time/Cost:** The goal is to find an optimal setup without excessive experimentation.
*   **The Proposed Plan:**
    *   The initial plan was a 4-level assembly/4-level curing setup (4x4).
    *   The researchers suggested increasing the complexity (e.g., a 6-level curing setup) to ensure enough degrees of freedom for statistical validity, despite the increased experimental cost.

### 3. Summary of Technical Concepts
| Concept | Description in Text |
| :------ | :--- |
| **Primary Goal** | To optimize the battery production process (preventing OCV issues). |
| **Statistical Risk** | Underestimating the error variance due to "hidden" correlations in batches. |
| **Statistical Solution** | Using a Split-Plot or Strip-Plot design approach to account for restricted randomization. |
| **Key Methodology** | Using the GLS (Generalized Least Squares) framework to estimate parameters when error structures are non-independent. |