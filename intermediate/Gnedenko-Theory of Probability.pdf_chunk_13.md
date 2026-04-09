Based on the provided mathematical text, here is a summary of the key concepts and definitions presented:

### 1. Probabilistic Moments and Central Moments
The text defines the **$k$-th moment** of a random variable $X$ as:
$$\mu'_k = \int x^k \, dF(x)$$
The **$k$-th central moment** (the moment about the mean $\mu$) is defined as:
$$\mu_k = E[(X - \mu)^k]$$
Specific cases mentioned include:
*   **$k=1$**: The expectation/mean ($E[X]$ or $\mu$).
*   **$k=2$**: The variance ($\sigma^2$).

### 2. Moments of a Distribution
The text provides formulas for calculating moments of specific distributions:
*   **Normal/General**: It discusses how $\mu_k$ can be expressed using $\mu'_k$ via the binomial expansion.
*   **Power-law/Specific relation**: It explores the relationship between moments $\mu_k$ and the $k$-th order.

### 3. Moments of the Uniform and Binomial-related distributions
The text describes the calculation of moments for various probability mass functions (PMF) and probability density functions (PDF). For example:
*   **Uniform Distribution**: The moments involve integrals of the form $\int x^k \, dx$.
*   **Sum of variables**: It discusses the moments of the sum of independent random variables, where the $k$-th moment of the sum depends on the moments of the individual components.

### 4. Key Statistical Measures
*   **Variance ($\sigma^2$)**: Defined as $\mu_2$, or $E[X^2] - (E[X])^2$.
*   **Standard Deviation ($\sigma$)**: The square root of the variance.
*   **Skewness and Kurtosis**: While not explicitly named, the text discusses the calculation of higher-order central moments ($\mu_3, \mu_4$), which are the basis for these measures.

### 5. Mathematical Relationships and Theorems
*   **Expectation of a Sum**: $E[\sum X_i] = \sum E[X_i]$.
*   **Variance of a Sum**: For independent variables, $Var(\sum X_i) = \sum Var(X_i)$.
*   **Relationship between Moments**: The text provides the expansion to relate central moments to raw moments:
    $$\mu_k = \sum_{j=0}^{k} \binom{k}{j} \mu'_j (-\mu)^{k-j}$$
*   **Moments of Products**: For independent $X$ and $Y$, $E[X^n Y^m] = E[X^n]E[Y^m]$.

### 6. Application Contexts
The text applies these statistical tools to:
*   **Probability Mass Functions (PMF)** for discrete variables.
*   **Probability Density Functions (PDF)** for continuous variables.
*   **Stochastic processes**: Mentioning the behavior of sums of random variables and the evolution of distributions.