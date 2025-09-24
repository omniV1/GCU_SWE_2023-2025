# Topic 1: Introduction to Data and Algorithms

## Week 1, Class 1

### Ethics vs. Morals

**Note:** These terms are not interchangeable.

- **Morals:** Based on situational diagnosis
- **Ethics:** Based on grand instruction

### What is an Algorithm?

- Algorithms are always the same: a set of unambiguous steps of instructions
- Algorithms allow developers to manipulate data more effectively
- Example: Recursive algorithm
  - GCD (Greatest Common Divisor) is an example
  - To find GCD, we use: `gcd(m, n) = gcd(n, m mod n)`
    - `mod n` is the integer remainder
    - This is known as Euclid's algorithm

#### Example: GCD(60, 24) = GCD(24, 12) → GCD(12, 0)

1. If n = 0, return m and stop
2. Divide m by n and assign the value of the remainder to r
3. Assign the value of n to m and the value of r to n

#### Pseudo-code example:

```pseudo
while n != 0 do
    r = m mod n
    m = n
    n = r
return m
```

### Key Concepts

- What is an input to an algorithm called? **An instance**
- How often should an algorithm work correctly? (Answer not provided)

### Random Access Memory (RAM)

1. Allocates temporary storage / built as an array
2. A sequential algorithm will run in RAM
3. Newer computers have multiple processors running concurrently (concurrency is very important)
4. Algorithms that run concurrently are called parallel algorithms and are implemented with threading

### Factors Affecting Algorithms

1. **Exact:** More accurate
2. **Generality:** May have a rounding error

### Algorithm Design Techniques

1. Get it working, then optimize
2. Document algorithms with pseudo-code, flowcharts, and conversation
3. Natural language is the most problematic of the three
4. Ensure your models are clearly communicated and show failure cases

    
