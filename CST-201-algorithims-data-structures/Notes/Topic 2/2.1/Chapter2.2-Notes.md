# 2.2 Asymptotic Notations and Basic Efficiency Classes

As pointed out in the previous section, the efficiency analysis framework concentrates on the order of growth of an algorithm’s basic operation count as the principal indicator of the algorithm’s efficiency. To compare and rank such orders of growth, computer scientists use three notations: **O** (big oh), **Ω** (big omega), and **Θ** (big theta). 

First, we introduce these notations informally, and then, after several examples, formal definitions are given. In the following discussion, **t(n)** and **g(n)** can be any nonnegative functions defined on the set of natural numbers. In the context we are interested in, **t(n)** will be an algorithm’s running time (usually indicated by its basic operation count **C(n)**), and **g(n)** will be some simple function to compare the count with.

### Informal Introduction

Informally, **O(g(n))** is the set of all functions with a lower or same order of growth as **g(n)** (to within a constant multiple, as **n** goes to infinity). The following assertions are all true:

- **n ∈ O(n²)**, 
- **100n + 5 ∈ O(n²)**, 
- **12n(n - 1) ∈ O(n²)**.

The first two functions are linear and hence have a lower order of growth than **g(n) = n²**, while the last one is quadratic and hence has the same order of growth as **n²**. 

On the other hand, the following assertions are false:

- **n³ ∉ O(n²)**, 
- **0.00001n³ ∉ O(n²)**, 
- **n⁴ + n + 1 ∉ O(n²)**.

Indeed, the functions **n³** and **0.00001n³** are both cubic and hence have a higher order of growth than **n²**, as does the fourth-degree polynomial **n⁴ + n + 1**.

The second notation, **Ω(g(n))**, stands for the set of all functions with a higher or same order of growth as **g(n)** (to within a constant multiple, as **n** goes to infinity). For example:

- **n³ ∈ Ω(n²)**, 
- **12n(n - 1) ∈ Ω(n²)**, 
- but **100n + 5 ∉ Ω(n²)**.

Finally, **Θ(g(n))** is the set of all functions that have the same order of growth as **g(n)** (to within a constant multiple, as **n** goes to infinity). Thus, every quadratic function **an² + bn + c** with **a > 0** is in **Θ(n²)**, but so are, among infinitely many others, **n² + sin(n)** and **n² + log(n)**. (Can you explain why?)

Hopefully, this informal introduction has made you comfortable with the idea behind the three asymptotic notations. Now come the formal definitions.

### O-notation

#### Definition:

A function **t(n)** is said to be in **O(g(n))**, denoted **t(n) ∈ O(g(n))**, if **t(n)** is bounded above by some constant multiple of **g(n)** for all large **n**, i.e., if there exist some positive constant **c** and some nonnegative integer **n₀** such that:

**t(n) ≤ c * g(n)** for all **n ≥ n₀**.

The definition is illustrated in Figure 2.1 where, for the sake of visual clarity, **n** is extended to be a real number.

#### Example:

Let us formally prove one of the assertions made in the introduction: **100n + 5 ∈ O(n²)**. 

Indeed,

**100n + 5 ≤ 100n + n** (for all **n ≥ 5**)  
= **101n ≤ 101n²**.

Thus, as values of the constants **c** and **n₀** required by the definition, we can take **101** and **5**, respectively.

Note that the definition gives us a lot of freedom in choosing specific values for constants **c** and **n₀**. For example, we could also reason that:

**100n + 5 ≤ 100n + 5n** (for all **n ≥ 1**)  
= **105n** to complete the proof with **c = 105** and **n₀ = 1**.

### Ω-notation

#### Definition:

A function **t(n)** is said to be in **Ω(g(n))**, denoted **t(n) ∈ Ω(g(n))**, if **t(n)** is bounded below by some positive constant multiple of **g(n)** for all large **n**, i.e., if there exist some positive constant **c** and some nonnegative integer **n₀** such that:

**t(n) ≥ c * g(n)** for all **n ≥ n₀**.

#### Example:

Here is an example of the formal proof that **n³ ∈ Ω(n²)**:

**n³ ≥ n²** for all **n ≥ 0**, i.e., we can select **c = 1** and **n₀ = 0**.

### Θ-notation

#### Definition:

A function **t(n)** is said to be in **Θ(g(n))**, denoted **t(n) ∈ Θ(g(n))**, if **t(n)** is bounded both above and below by some positive constant multiples of **g(n)** for all large **n**, i.e., if there exist some positive constants **c₁** and **c₂** and some nonnegative integer **n₀** such that:

**c₂ * g(n) ≤ t(n) ≤ c₁ * g(n)** for all **n ≥ n₀**.

#### Example:

Let us prove that **12n(n - 1) ∈ Θ(n²)**. 

First, we prove the right inequality (the upper bound):

**12n(n - 1) = 12n² - 12n ≤ 12n²** for all **n ≥ 0**.

Second, we prove the left inequality (the lower bound):

**12n(n - 1) = 12n² - 12n ≥ 12n² - 12n**  
= **12n** (for all **n ≥ 2**)  
= **14n²**.

Hence, we can select **c₂ = 1/4**, **c₁ = 1/2**, and **n₀ = 2**.

### Useful Property Involving the Asymptotic Notations

Using the formal definitions of the asymptotic notations, we can prove their general properties (see Problem 7 in this section’s exercises for a few simple examples). The following property, in particular, is useful in analyzing algorithms that comprise two consecutively executed parts.

## Fundamentals of the Analysis of Algorithm Efficiency

### Theorem:
If \( t_1(n) \in O(g_1(n)) \) and \( t_2(n) \in O(g_2(n)) \), then:

\[
t_1(n) + t_2(n) \in O(\max\{g_1(n), g_2(n)\})
\]

(The analogous assertions are true for the \( \Theta \) and \( \Omega \) notations as well.)

#### Proof:
The proof extends to orders of growth the following simple fact about four arbitrary real numbers \( a_1 \), \( b_1 \), \( a_2 \), and \( b_2 \): if \( a_1 \leq b_1 \) and \( a_2 \leq b_2 \), then:

\[
a_1 + a_2 \leq 2 \max\{b_1, b_2\}
\]

Since \( t_1(n) \in O(g_1(n)) \), there exists some positive constant \( c_1 \) and some non-negative integer \( n_1 \) such that:

\[
t_1(n) \leq c_1g_1(n) \text{ for all } n \geq n_1
\]

Similarly, since \( t_2(n) \in O(g_2(n)) \), 

\[
t_2(n) \leq c_2g_2(n) \text{ for all } n \geq n_2
\]

Let us denote \( c_3 = \max\{c_1, c_2\} \) and consider \( n \geq \max\{n_1, n_2\} \), so that we can use both inequalities. Adding them yields the following:

\[
t_1(n) + t_2(n) \leq c_1g_1(n) + c_2g_2(n) \leq c_3g_1(n) + c_3g_2(n) = c_3[g_1(n) + g_2(n)] \leq 2c_3 \max\{g_1(n), g_2(n)\}
\]

Hence, \( t_1(n) + t_2(n) \in O(\max\{g_1(n), g_2(n)\}) \), with the constants \( c \) and \( n_0 \) required by the \( O \)-definition being \( 2c_3 = 2 \max\{c_1, c_2\} \) and \( \max\{n_1, n_2\} \), respectively.

### Implications for Algorithm Efficiency:
This property implies that if an algorithm consists of two consecutive parts, its overall efficiency is determined by the part with a higher order of growth, i.e., its least efficient part.

For example, consider an algorithm that checks whether an array has equal elements by first sorting the array (which takes \( O(n^2) \)) and then scanning it (which takes \( O(n) \)). The overall efficiency will be:

\[
O(\max\{n^2, n\}) = O(n^2)
\]

### Using Limits for Comparing Orders of Growth:
To compare the growth rates of two functions, we can compute the limit of the ratio of the two functions as \( n \to \infty \). Three principal cases arise:

1. If 

\[
\lim_{n \to \infty} \frac{t(n)}{g(n)} = 0
\]

then \( t(n) \) has a smaller order of growth than \( g(n) \).

2. If 

\[
\lim_{n \to \infty} \frac{t(n)}{g(n)} = c
\]

where \( c \) is a constant, then \( t(n) \) has the same order of growth as \( g(n) \).

3. If 

\[
\lim_{n \to \infty} \frac{t(n)}{g(n)} = \infty
\]

then \( t(n) \) has a larger order of growth than \( g(n) \).

> **Note:** The first two cases mean \( t(n) \in O(g(n)) \), the last two mean \( t(n) \in \Omega(g(n)) \), and the second case means \( t(n) \in \Theta(g(n)) \).

The limit-based approach is often more convenient than the formal definitions because it can use calculus techniques like L'Hôpital's rule:

\[
\lim_{n \to \infty} \frac{t(n)}{g(n)} = \lim_{n \to \infty} \frac{t'(n)}{g'(n)}
\]

and Stirling's formula for large \( n \):

\[
n! \approx \sqrt{2 \pi n} \left(\frac{n}{e}\right)^n
\]

### Examples of Comparing Orders of Growth:

1. **Compare \( \frac{1}{2}n(n - 1) \) and \( n^2 \):**

\[
\lim_{n \to \infty} \frac{\frac{1}{2}n(n - 1)}{n^2} = \frac{1}{2} \lim_{n \to \infty} \left(1 - \frac{1}{n}\right) = \frac{1}{2}
\]

Since the limit is a positive constant, the functions have the same order of growth:

\[
\frac{1}{2}n(n - 1) \in \Theta(n^2)
\]

2. **Compare \( \log_2 n \) and \( \sqrt{n} \):**

\[
\lim_{n \to \infty} \frac{\log_2 n}{\sqrt{n}} = \lim_{n \to \infty} \frac{1 / n}{1 / (2\sqrt{n})} = 0
\]

Since the limit is 0, \( \log_2 n \) has a smaller order of growth than \( \sqrt{n} \):

\[
\log_2 n \in o(\sqrt{n})
\]

3. **Compare \( n! \) and \( 2^n \):**

Using Stirling's formula:

\[
\lim_{n \to \infty} \frac{n!}{2^n} = \lim_{n \to \infty} \frac{\sqrt{2 \pi n} \left(\frac{n}{e}\right)^n}{2^n} = \infty
\]

Thus, \( n! \) grows faster than \( 2^n \):

\[
n! \in \Omega(2^n)
\]

### Basic Efficiency Classes:
Even though there are infinitely many possible growth functions, many algorithms fall into a few basic efficiency classes. These include:

- **Constant** \( O(1) \)
- **Logarithmic** \( O(\log n) \)
- **Linear** \( O(n) \)
- **Quadratic** \( O(n^2) \)
- **Exponential** \( O(2^n) \)

While multiplicative constants can affect performance for small input sizes, algorithms with better asymptotic efficiency usually outperform algorithms with worse efficiency for larger inputs.

