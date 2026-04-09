Based on the technical text provided, here is a summary of the key concepts and findings regarding experimental design and statistical modeling.

### **1. Modeling Quadratic Effects**
To detect "curvature" in a dataset (non-linear relationships), the experimental design must include at least **three levels** for the factors being tested. A quadratic model (which includes squared terms like $x^2$) is used to model these effects. The text notes that a one-factor, two-level design is insufficient for detecting these patterns.

### **2. Handling Categorical Variables (Dummy Variables)**
When dealing with categorical factors (e.g., different suppliers or categories), researchers use "dummy variables" to represent them. However, this introduces a mathematical risk:
*   **The Collinearity Problem:** If you include a dummy variable for every single category, you create "perfect collinearity" (the variables become mathematically redundant), which prevents the model from being solved.
*   **The Solution:** To avoid this, one must use a "reference" method, such as:
    *   Dropping one category from the model (the reference category).
    *   Applying specific constraints to the parameters.

### **3. Measuring Design Quality (D-Efficiency)**
The text discusses how to compare different experimental designs using **D-efficiency**. 
*   **D-Optimality:** This is a criterion used to select a design that minimizes the volume of the confidence ellipsoid for the model parameters.
*   **Comparison:** The text suggests that "D-efficiency" is a primary metric for comparing the effectiveness of one experimental design against another.

### **4. FDS Plots (Fraction of Design Space)**
The document introduces **FDS plots** as a tool for visualizing the reliability of a model across the entire experimental region.
*   **Purpose:** These plots show the **variance of predictions** (how much the prediction might fluctuate) across the design space.
*   **Function:** An FDS plot allows a researcher to see if the model is equally reliable in all parts of the experimental area or if certain regions (e.g., the edges of the design space) have much higher uncertainty/variance than others.
*   **Metric:** The calculation involves looking at the "relative variance" of predictions compared to the variance at the center of the design.

### **Summary of Mathematical Concepts**
*   **Integration & Moments:** The calculation of average prediction variance can be simplified using the concept of "moments" of the design, which involves integrating the variance function over the experimental region.
*   **Relative Variance:** The primary goal of these techniques is to ensure that the prediction error is controlled and understood across the entire range of experimental conditions.