# Important Problem Types

### Motiviating forces for particular attention
1. Problems practical performance.
2. Interesting problem / research subject.

### Sorting
- **Definition**: Rearranging items of a given list in nondecreasing order
- **Requirements**: Items must allow total ordering
- **Common applications**: Numbers, characters, strings, and records
- **Key**: Chosen piece of information to guide sorting (e.g., student name, number, or GPA)

#### Importance of sorting:
- Required output for ranking (e.g., search results, student GPAs)
- Facilitates searching and other list operations
- Auxiliary step in various algorithms (e.g., geometric, data compression)
- Essential for greedy algorithms

#### Characteristics of sorting algorithms:
- Numerous algorithms exist (dozens)
- Efficient algorithms use about n log₂n comparisons
- No single algorithm is best for all situations

#### Key properties:
1. **Stability**: Preserves relative order of equal elements
   - Example: Sorting students by GPA while maintaining alphabetical order for equal GPAs
   - Trade-off: Algorithms that exchange distant keys are usually faster but not stable
2. **Memory usage**: 
   - In-place algorithms require minimal extra memory
   - Both in-place and non-in-place algorithms are important

### Searching
- **Definition**: Finding a given value (search key) in a set or multiset
- **Range of algorithms**: Sequential search, binary search, advanced data representations

#### Characteristics:
- No single best algorithm for all situations
- Trade-offs between speed and memory usage
- Some algorithms work only on sorted arrays

#### Considerations:
- Frequency of data changes vs. number of searches
- Balance between searching, addition, and deletion operations
- Special challenges for organizing large data sets

### String Processing
- **Definition**: Algorithms dealing with sequences of characters
- **Types**: Text strings, bit strings, gene sequences
- **Importance**: Increased interest due to non-numerical data applications
- Long-standing significance in computer languages and compiling

### Combinatorial Problems
- **Characteristics**:
  - Number of objects grows extremely fast with problem size
  - Most lack efficient algorithms for exact solutions
  - Believed to have no efficient algorithms (unproven conjecture)
- **Exceptions**: Some have efficient algorithms (e.g., shortest-path problem)

### Geometric Problems
- **Definition**: Algorithms dealing with geometric objects (points, lines, polygons)
- **Historical context**: Ancient Greek interest, modern resurgence with computer age
- **Applications**: Computer graphics, robotics, tomography
- **Examples**: Closest-pair problem, convex-hull problem

### Numerical Problems
- **Definition**: Problems involving continuous mathematical objects
- **Challenges**:
  1. Most can only be solved approximately
  2. Computer representation of real numbers is approximate
  3. Round-off errors can accumulate and distort results

#### Historical Significance and Current State:
- Critical in scientific and engineering applications
- Decreased focus due to shift towards business applications
- No longer dominating in industry or computer science programs
- Still important for general computer literacy

#### Coverage in the Book:
- Classical numerical algorithms discussed in Sections 6.2, 11.4, and 12.4




