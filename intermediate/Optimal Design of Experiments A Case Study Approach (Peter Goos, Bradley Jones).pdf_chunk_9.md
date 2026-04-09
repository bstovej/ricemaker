This document is an excerpt from the textbook *Optimal Design of Experiments: A Case Study Approach* by Peter Goos and Bradley Jones. It discusses the principles, methodologies, and practical applications of screening experiments and model augmentation.

Below are the key insights and facts categorized by theme:

### 1. Core Principles of Model Selection
*   **Principle of Hierarchy:** In regression modeling, first-order (main) effects are typically the largest source of variability. Second-order effects (two-factor interactions and quadratic effects) are the next largest. Consequently, model selection should prioritize adding main effects before including second-order effects.
*   **Principle of Heredity:** This relates to how interactions are included in a model:
    *   **Strong Heredity:** If a two-factor interaction ($x_i \times x_j$) is included, the main effects of both $x_i$ and $x_j$ must also be present. This provides a technical advantage: predictions remain stable even if factors are rescaled.
    *   **Weak Heredity:** If an interaction is included, only one of the two constituent main effects must be present in the model.
*   **Sparsity and Synergy:** While hierarchy and heredity are standard, empirical evidence (Li et al., 2006) shows that violations of these principles occur more frequently than previously thought. Notably, **80% of active two-factor interactions are synergistic** (positive), meaning that maximizing main effects will likely lead to increased responses via unidentified interactions.

### 2. Experimental Design Methodologies
*   **Design Types:**
    *   **Fractional Factorial Designs:** Include both regular (power of 2) and non-regular orthogonal designs (e.g., Plackett–Burman, Hadamard). Non-regular designs offer more flexibility because they can be used whenever the number of runs is a multiple of 4.
    *   **Supersaturated Designs:** These are highly efficient because they involve fewer experimental runs than there are experimental factors.
    *   **Three-Level Designs:** Proposed by Jones and Nachtsheim, these designs allow for the assessment of curvature and ensure main-effect estimates are not biased by two-factor interactions or quadratic effects.
*   **Algorithmic Approaches for Finding Optimal Designs:**
    *   **Coordinate-Exchange Algorithm:** Highly efficient as it runs in polynomial time, meaning its computational demand does not explode as the number of factors increases.
    *   **Point-Exchange Algorithms:** Less efficient for large designs because they require a massive "candidate set" of possible design points.
    *   **Metaheuristics (Genetic/Simulated Annealing):** While complex, these have not gained widespread popularity because they do not significantly outperform simpler algorithms in practical applications.

### 3. Sequential Experimentation and Augmentation
*   **The Goal of Augmentation:** The document highlights that experimentation is a sequential process. When a screening experiment leaves questions unanswered, "augmenting" the experiment (adding new runs) allows researchers to include more complex terms (like interactions) without drastically increasing the total run size.
*   **Handling Time-Based Variables (Blocking):** When adding runs to an old experiment, the process/environment may have changed. To prevent this from contaminating the results, researchers use a **blocking factor**. This factor distinguishes between the original and the new runs, capturing any "shift" in the process (e.g., changes in yield) caused by time.
*   **Trade-offs in Model Complexity:** Adding interaction effects to a model generally makes the model matrix non-orthogonal (increasing variance), but the reduction in the root mean square error (RMSE) typically outweighs the loss of precision.

### 4. Case Study Context: GeneBe
*   **The Scenario:** A biotech firm (GeneBe) successfully doubled their extraction yield using recommendations from a previous screening experiment.
*   **The Objective:** The researchers are performing a follow-up experiment to differentiate between several "competing models" (different sets of variables) and specifically to investigate the interaction between ethanol and other components.