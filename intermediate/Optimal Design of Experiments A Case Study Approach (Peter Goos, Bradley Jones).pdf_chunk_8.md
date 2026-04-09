Based on the provided text, here is a summary of the key information regarding the **Coordinate Exchange Algorithm** used in optimal experimental design.

### **Core Concept**
The Coordinate Exchange Algorithm is a local search procedure used to improve an existing experimental design. The primary goal is to iteratively modify the coordinates of the design points to maximize a specific criterion, most commonly **D-optimality** (which involves maximizing the determinant of the information matrix, $X^T X$).

---

### **How the Algorithm Works**
The algorithm follows a systematic, iterative process to "search" for a better design:

1.  **Initialization:** Start with an initial design (this can be a random selection of points within the design space).
2.  **Iterative Improvement (The "Pass"):** The algorithm performs a "pass" through the design, examining each experimental point one by one.
3.  **Coordinate Modification:** For each individual point in the design:
    *   The algorithm examines each coordinate (dimension) of that point.
    *   It tests changing the value of that coordinate, typically by moving it to the boundaries (extremes) of the design space.
4.  **Evaluation:** After a potential change is made, the algorithm recalculates the design criterion (e.g., the determinant of the information matrix).
5.  **Decision Rule:** 
    *   **If the change improves the criterion:** The new coordinate value is accepted, and the design is updated.
    *   **If the change does not improve the criterion:** The original coordinate value is retained.
6.  **Convergence (Termination):** The algorithm repeats the entire pass (Steps 2–5) for all points in the design. The process stops only when an entire pass is completed without any changes being made to any points. This indicates that the algorithm has reached a local optimum.

---

### **Key Technical Elements**
*   **Optimization Criterion:** The text refers to maximizing the determinant of the information matrix, which is the hallmark of **D-optimality**.
*   **Design Space:** The algorithm operates within a defined space, and the search for new coordinates often involves testing the boundaries of that space.
*   **Nature of the Algorithm:** It is a **local search method**, meaning it finds an optimal configuration relative to the starting point, but it is not guaranteed to find the global optimum unless the design space and criteria are well-behaved.
*   **Application:** This technique is fundamental in the field of **Optimal Experimental Design**, used to create efficient experiments that provide the maximum amount of information with the minimum number of runs.