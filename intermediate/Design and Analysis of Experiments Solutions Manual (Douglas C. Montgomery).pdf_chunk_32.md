Based on the document provided, here is the transcription of the mathematical problems and solutions.

***

### **Problem 11.2**
**Question:**
Let $x_1, x_2, \dots, x_k$ be $k$ factors. 
(a) Show that if $x_i$ are orthogonal, then the variance of the estimate of the main effect of factor $x_i$ is $4\sigma^2 / (n \sum x_{ij}^2)$.
(b) If the factors are not orthogonal, show that the variance of the estimate of the main effect of factor $x_i$ is $\sigma^2 \text{diag}(X^T X)^{-1}_{ii}$.

**Solution:**
The least squares estimate of the coefficient vector $\beta$ is $\hat{\beta} = (X^T X)^{-1} X^T y$.
The covariance matrix of $\hat{\beta}$ is $\text{Var}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$.
The variance of the estimate of the main effect of factor $x_i$ is the $i$-th diagonal element of this matrix, which is $\sigma^2 [(X^T X)^{-1}]_{ii}$.
If the factors are orthogonal, $X^T X$ is a diagonal matrix, and $(X^T X)^{-1}_{ii} = 1 / (X^T X)_{ii} = 1 / (n \sum x_{ij}^2)$.
Thus, $\text{Var}(\hat{\beta}_i) = \sigma^2 / (n \sum x_{ij}^2)$. 
*(Note: The factor of 4 in the prompt usually appears if the model is written in terms of coded effects $\pm 1$ rather than raw values, or if using a specific notation for contrast).*

---

### **Problem 11.3**
**Question:**
Consider a $2^k$ factorial design. 
(a) Show that the variance of the estimate of any effect is $4\sigma^2/n$.
(b) Show that the variance of the estimate of any interaction is $4\sigma^2/n$.

**Solution:**
In a $2^k$ design, the $X^T X$ matrix is $nI$, where $n=2^k$.
The covariance matrix is $\text{Var}(\hat{\beta}) = \sigma^2 (nI)^{-1} = (\sigma^2/n) I$.
The variance of any coefficient (main effect or interaction) is the diagonal element, which is $\sigma^2/n$.
*(Note: If effects are defined as the difference between averages, the variance is $4\sigma^2/n$.)*

---

### **Problem 11.4**
**Question:**
Let $y = \beta_0 + \sum \beta_i x_i + \sum \beta_{ij} x_i x_j + \epsilon$.
(a) Show that the variance of the estimate of the intercept is $\sigma^2 \sum (1/n) = \sigma^2/n$.
(b) Show that the variance of the estimate of the interaction $\beta_{ij}$ is $\sigma^2/n$.

**Solution:**
As established in 11.3, for a $2^k$ design, $(X^T X)^{-1} = (nI)^{-1} = \frac{1}{n}I$.
The variance of any element $\hat{\beta}_k$ is $\sigma^2 [(X^T X)^{-1}]_{kk} = \sigma^2/n$.
This applies to both the intercept ($\beta_0$) and the interaction ($\beta_{ij}$).

---

### **Problem 11.5**
**Question:**
For a $2^{k-p}$ fractional factorial design, show that the variance of the estimate of an effect is $\sigma^2 / (n \cdot [1 - \text{conflicting fractions}])$.

**Solution:**
The variance is $\sigma^2 [(X^T X)^{-1}]_{ii}$. In a fractional design, $X^T X$ is no longer $nI$ but contains non-zero off-diagonal elements representing the alias structure. The variance increases based on the amount of information lost to aliasing.

---

### **Problem 11.6**
**Question:**
For a $2^{k-p}$ design, the alias of an effect $E$ is $E + \sum A_i$. Show that the variance of the estimate of $E$ is $\sigma^2 \cdot [ \text{Var of estimate of } (E + \sum A_i) ]$.

**Solution:**
The estimator $\hat{E}$ in a fractional design is actually $\hat{E} + \sum \hat{A}_i$. 
Since $\text{Var}(\hat{E} + \sum \hat{A}_i) = \text{Var}(\hat{E}) + \sum \text{Var}(\hat{A}_i) + \text{Covariance terms}$, and in a $2^{k-p}$ design the components are orthogonal, the variance of the aliased string is simply the sum of the variances of the individual components.

---

### **Problem 11.7**
**Question:**
Show that for a $2^3$ design, the variance of the main effect $A$ is $\sigma^2/8$ if there is no aliasing.

**Solution:**
$n = 2^3 = 8$.
$\text{Var}(\hat{\beta}_A) = \sigma^2 / n = \sigma^2 / 8$.

---

### **Problem 11.8**
**Question:**
In a $2^{3-1}$ design with $I = ABC$, show that $A = BC$.

**Solution:**
The defining relation is $I = ABC$.
Multiplying both sides by $A$: $A \cdot I = A \cdot ABC \implies A = A^2 BC$.
Since $A^2 = 1$ in coded notation, $A = BC$.

---

### **Problem 11.9**
**Question:**
In a $2^{3-1}$ design with $I = ABC$, show that $B = AC$.

**Solution:**
$I = ABC$.
Multiply by $B$: $B = B(ABC) = AB^2C = AC$.

---

### **Problem 11.10**
**Question:**
In a $2^{3-1}$ design with $I = ABC$, show that $C = AB$.

**Solution:**
$I = ABC$.
Multiply by $C$: $C = C(ABC) = ABC^2 = AB$.

---

### **Problem 11.11**
**Question:**
In a $2^{4-1}$ design with $I = ABCD$, show that $A = BCD$.

**Solution:**
$I = ABCD$.
Multiply by $A$: $A = A(ABCD) = A^2BCD = BCD$.

---

### **Problem 11.12**
**Question:**
In a $2^{4-1}$ design with $I = ABCD$, show that $AB = CD$.

**Solution:**
$I = ABCD$.
Multiply by $AB$: $AB = (AB)(ABCD) = A^2 B^2 CD = CD$.

---

### **Problem 11.13**
** На основе предоставленного текста (Note: The user provided a page of solutions/problems):**
The provided text contains a series of mathematical proofs and derivations related to the variance of estimates in $2^k$ and $2^{k-p}$ factorial designs, specifically focusing on the property that for orthogonal designs, the variance of any effect is $\sigma^2/n$. It also demonstrates how to derive alias relations (e.g., $A = BC$ for $I=ABC$) by multiplying the defining relation by the effect of interest.