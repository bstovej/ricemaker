Based on the provided document, which appears to be a foundational text on probability theory, here are the key insights and facts organized by thematic category.

### 1. Philosophical Insights: The Nature of Probability
The text argues against a purely subjective view of probability, positioning it instead as an objective science.

*   **Objectivity vs. Subjectivity:** The author rejects the idea that probability is merely a measure of an investigator's "degree of confidence" or psychological state (subjective idealism). Instead, the author asserts that a probabilistic judgment expresses an **objective property** of a phenomenon that exists independently of the observer.
*   **The Role of Conditions ($\theta$):** Probability is not a universal constant but is tied to a specific set of conditions ($\theta$). To assert a probability $p$ for event $A$ is to claim a definite, objective relationship between the conditions $\text\theta$ and the event $A$.
*   **Beyond "Randomness":** The text notes that simply defining an event as "random" (meaning it is neither necessary nor impossible) is insufficient. To assign a specific numerical probability to a random event requires scientific substantiation or verification.
*   **Example of Physical Application:** In physics, the decay of a radioactive element is used to illustrate objective probability. The rate of decay ($\alpha$) is an objective property of the element under specific conditions, not just a guess by the physicist.

### 2. Categorization of Probability Definitions
The author identifies three historical approaches to defining mathematical probability:
1.  **Subjective:** Probability as a measure of the observer's "degree of certainty" (dismissed by the author as reducing probability to psychology).
2.  **Classical:** Probability based on the concept of "equal possibility" or symmetry (e.g., a fair die).
3.  **Statistical:** Probability based on the "frequency" of an event occurring over a large number of trials.
*   **The Author’s Thesis:** A complete understanding of probability requires a **synthesis** of the Classical and Statistical definitions.

### '3. Mathematical Framework: Set Theory and "Fields of Events"
The text establishes the formal language used to manipulate events using set theory:

*   **Fundamental Operations:**
    *   **Implication ($A \implies B$):** If event $A$ occurs, event $B$ must also occur.
    *   **Equivalence ($A = B$):** $A$ and $B$ are functionally identical if they always occur or fail to occur together.
    *   **Product ($AB$ or $A \cap B$):** The occurrence of both events $A$ and $B$.
    *   **Sum ($A+B$ or $A \cup B$):** The occurrence of at least one of the events $A$ or $B$.
    *   **Difference ($A - B$):** Event $A$ occurs, but event $B$ does not.
*   **Special Event Types:**
    *   **Certain Event ($U$):** An event that must occur by necessity.
    *   **Impossible Event ($\emptyset$ or $V$):** An event that cannot occur.
    *   **Mutually Exclusive:** Two events that cannot happen at the same time ($AB = \emptyset$).
    *   **Complementary (Contrary):** An event and its opposite ($A$ and $\bar{A}$) that together constitute certainty.
*   **The "Field of Events":** A collection of events is considered a "field" if it contains the certain and impossible events and is closed under the operations of sum, difference, and product.
*   **Sample Space:** The starting point of modern probability is a "space of simple (elementary) events" that encompasses all possible outcomes.

### 4. The Classical Definition of Probability
The text provides the formal logic for the "Classical" approach:

*   **The Formula:** If an event $A$ is composed of $m$ outcomes from a total group of $n$ mutually exclusive and equally probable outcomes, then:
    $$P(A) = \frac{m}{n}$$
*   **Requirement of Symmetry:** This definition relies on the assumption of **equal likelihood**, which is derived from the physical symmetry of the objects involved (e.g., a perfectly balanced, homogeneous cube for a die).
*   **Practical Application (The Die Example):** 
    *   In a single roll of a die, there are 6 possible outcomes.
    *   The probability of rolling an even number (2, 4, or 6) is $3/6 = 0.5$.
    *   In a roll of two dice, there are 36 possible combinations. The probability of rolling a sum of 11 is $2/36$ because there are only two favorable outcomes: $(5,6)$ and $(6,5)$.