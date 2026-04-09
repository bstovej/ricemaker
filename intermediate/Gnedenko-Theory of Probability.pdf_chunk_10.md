Based on the provided document, which appears to be a segment from a textbook on probability theory (specifically Chapter 4, "Random Variables and Distribution Functions"), here are the key insights and facts organized by topic.

### 1. Fundamental Concept: The Random Variable (RV)
*   **Definition:** A random variable is a quantity that describes a phenomenon subject to chance. To fully specify a random variable, one must know both the values it can assume and the probability with which it assumes those values.
*   **Real-World Examples:** The text provides several concrete examples of random variables:
    *   The number of cosmic particles hitting the Earth.
    *   The number of telephone calls arriving at an exchange.
    *   The deviation of a shell impact from a target center.
    *   The velocity of a gas molecule.
*   **Mathematical Definition:** Formally, a random variable $X$ is a measurable function $f(e)$ that maps an elementary event $e$ from a probability space $(\Omega, \mathcal{F}, P)$ to a real number.

### 2. The Distribution Function $F(x)$
The distribution function is the primary tool used to describe the behavior of a random variable.
*   **Mathematical Definition:** $F(x) = P(X < x)$.
*   **Core Properties of $F(x)$:**
    *   **Non-decreasing:** As $x$ increases, $F(x)$ never decreases.
    *   **Boundaries:** $F(-\infty) = 0$ and $F(+\infty) = 1$.
    *   **Continuity:** The text specifies that the distribution function is **continuous on the left** (a convention often found in specific mathematical traditions).
    *   **Jumps:** $F(x)$ can have jumps (discontinuities). The magnitude of the jump at a point represents the probability mass at that specific value.

### 3. Classification of Random Variables
The text distinguishes between different types of distributions:
*   **Discrete/Step Distributions:** Characterized by "jumps" in the distribution function (e.g., the Bernoulli or Binomial-style processes).
*   **Continuous Distributions:** Defined by a probability density function (PDF) where $F(x)$ is continuous.
*   **Specific Probability Models Mentioned:**
    *   **Bernoulli/Binomial context:** Mentioned via "success/failure" logic in the exercises.
    *   **Normal/Gaussian context:** Implicitly discussed via the discussion of the Normal distribution parameters ($\mu$ and $\sigma$).
*   **Special Cases:** The text mentions the **Cantor distribution** (via the Cantor function/curve) as a mathematical curiosity where the distribution is continuous but has a derivative of zero almost everywhere.

### 4. Types of Probability Distributions Discussed
*   **Poisson/Binomial logic:** Implied in the exercises regarding counts of events.
*   **Normal (Gaussian) Distribution:** Discussed in the context of $\mu$ (mean) and $\sigma$ (standard deviation).
*   **The Cantor Distribution:** A "singular" distribution that is continuous but its derivative is zero almost everywhere (related to the Cantor set).

### 5. Mathematical Advanced Concepts
*   **Probability Density Function (PDF):** For continuous variables, the density $f(x)$ is the derivative of the distribution function $F(x)$.
*   **Multivariate Distributions:** The text touches upon $n$-dimensional random variables (vectors) and joint distributions.
*   **The Cantor Set/Function:** The text references the concept of a distribution that is continuous but has no density in the traditional sense (the "Cantor staircase").

### 6. Summary of Mathematical Properties
| Feature | Property |
| :--- | :--- |
| **Function $F(x)$** | Non-decreasing, $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$ |
| **Probability Mass** | $P(X=x) = F(x) - \lim_{t \to x^-} F(t)$ |
| **Continuity** | If $F(x)$ is continuous, the variable is "continuous." |
| **Density $f(x)$** | $f(x) = \frac{d}{dx} F(x)$ (where the derivative exists). |