# Analysis of Algorithms: A Comprehensive Framework

## Introduction
The analysis of algorithms primarily focuses on efficiency in two key areas:
- **Running time** (time complexity)
- **Memory space usage** (space complexity)

### This emphasis on efficiency stems from:
- The ability to study it in precise quantitative terms
- Its critical importance in practical applications

## General Framework for Analyzing Algorithm Efficiency

### Measuring Input Size (n)
The choice of size metric depends on the problem and algorithm operations:
- **For lists**: typically the number of elements
- **For matrices**: matrix order or total number of elements
- **For polynomials**: degree or number of coefficients

For problems with a single numeric input (e.g., primality testing):
- Size is often measured by the number of bits in binary representation
  - Formula: `b = log₂n + 1`, where `n` is the input number

### Units for Measuring Running Time
Count the number of executions of the algorithm's basic operation:
- **Basic operation**: usually the most time-consuming operation in the innermost loop
  - Example: key comparisons in sorting algorithms
- Estimate running time: `T(n) ≈ c_op * C(n)`
  - `c_op`: execution time of basic operation
  - `C(n)`: number of times the basic operation is executed

### Orders of Growth
Focus on the order of growth for large input sizes, ignoring multiplicative constants and lower-order terms. Common growth rates (from slowest to fastest):
- **Logarithmic**: log n
- **Linear**: n
- **Linearithmic**: n log n
- **Quadratic**: n²
- **Cubic**: n³
- **Exponential**: 2ⁿ, 3ⁿ, etc.

## Types of Efficiency Analysis

### Worst-Case Efficiency
- Measures efficiency for the input of size `n` with the longest running time
- Provides an upper bound on running time
- Generally the most important and widely used efficiency measure
- Notation: `C_worst(n)`

### Best-Case Efficiency
- Measures efficiency for the input of size `n` with the shortest running time
- Less important but useful for certain algorithms and input types
- Can indicate performance on nearly-ideal inputs
- Notation: `C_best(n)`

### Average-Case Efficiency
- Measures efficiency for a "typical" or "random" input of size `n`
- Requires assumptions about input probability distribution
- Often more difficult to determine than worst-case or best-case efficiency
- Provides insight into expected performance in practice
- Notation: `C_avg(n)`

### Amortized Efficiency
- Applies to a sequence of operations on a data structure
- Accounts for cases where occasional expensive operations are offset by many inexpensive ones
- Important for data structures with fluctuating operation costs

## Analytical Techniques

### Mathematical Analysis
- For non-recursive algorithms (Section 2.3)
- For recursive algorithms (Section 2.4)

### Empirical Analysis
- Measuring actual running time on various inputs

### Algorithm Visualization
- Graphical representation of algorithm behavior

## Key Points to Remember
- Efficiency is measured as a function of input size
- Time efficiency focuses on counting basic operation executions
- Space efficiency measures extra memory units consumed
- Distinguish between worst-case, average-case, and best-case for algorithms with variable performance
- The primary focus is on the order of growth as input size approaches infinity

This comprehensive framework provides a systematic approach to analyzing and comparing algorithm efficiency, which is crucial for designing and selecting appropriate algorithms for various computational problems.
