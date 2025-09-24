
# Fundamental Data Structures: A Comprehensive Review

## Graph Representations

### Adjacency Matrix

* A 2D array where element A[i,j] is 1 if there's an edge from vertex i to j, and 0 otherwise
* Efficient for dense graphs
* Requires n^2 space for n vertices, regardless of the number of edges
* Quick edge lookup: O(1) time
* Inefficient for sparse graphs due to wasted space

### Adjacency List

* A collection of linked lists, one for each vertex, containing its adjacent vertices
* More space-efficient for sparse graphs
* Space complexity: O(|V| + |E|) where |V| is the number of vertices and |E| is the number of edges
* Slower edge lookup compared to adjacency matrix: O(degree(v)) time
* Efficient for algorithms that explore the graph by following edges

### Weighted Graphs

* Graphs with numbers (weights or costs) assigned to edges
* Real-world applications: shortest path in transportation networks, traveling salesman problem
* Representations:
  1. Weight matrix: A[i,j] contains the weight of the edge from i to j, or ∞ if no edge exists
  2. Adjacency lists with weight information: each node includes both vertex and edge weight

## Graph Properties

### Paths

* A sequence of adjacent (connected by an edge) vertices
* Simple path: all vertices are distinct
* Path length: number of edges in the path (or vertices - 1)
* Example: a, c, b, f is a simple path of length 3

### Connectivity

* A graph is connected if there's a path between every pair of vertices
* Connected components: maximal connected subgraphs
* Disconnected graphs have multiple connected components
* Example: U.S. Interstate highway system (Why is it disconnected?)

### Cycles

* A path of positive length that starts and ends at the same vertex
* Does not traverse the same edge more than once
* Acyclic graph: a graph with no cycles
* Important for many applications to determine if a graph has cycles

### Trees

* Connected acyclic graphs
* Properties: |E| = |V| - 1, unique path between any two vertices
* Forest: a collection of trees (acyclic graph, not necessarily connected)

## Linear Data Structures

### Linked Lists

* Dynamic data structure, no need for contiguous memory allocation
* Efficient insertions and deletions
* Types:
  * Singly linked list: each node points to the next
  * Doubly linked list: each node points to both successor and predecessor
  * Lists with headers: special node containing list information (e.g., length)

### Stacks

* Last-In-First-Out (LIFO) principle
* Operations: push (add to top), pop (remove from top)
* Applications: implementing recursive algorithms, expression evaluation

### Queues

* First-In-First-Out (FIFO) principle
* Operations: enqueue (add to rear), dequeue (remove from front)
* Applications: breadth-first search, scheduling

### Priority Queues

* Collection of items from a totally ordered universe
* Operations: find max, delete max, add new element
* Implementations: arrays, sorted arrays, heaps (most efficient)
* Applications: event-driven simulations, data compression

## Tree Representations

* First child–next sibling representation: each node stores pointers to its first child and next sibling
* Binary tree representation: leftmost child becomes left child, next sibling becomes right child

## Sets and Dictionaries

### Set Implementations

1. Bit vector representation:
   * Uses a bit string where i-th bit is 1 if i-th element of universal set is in the subset
   * Fast set operations, but potentially large storage requirements
2. List representation:
   * Elements stored in a list structure
   * More flexible, but slower operations

### Multiset (Bag)

* Unordered collection of items that are not necessarily distinct
* Relaxes the set requirement of unique elements

### Dictionary

* Supports: search, add, delete operations
* Implementations:
  * Unsophisticated: arrays (sorted or unsorted)
  * Sophisticated: hashing, balanced search trees
* Challenge: balance efficiency of searching with efficiency of insertions/deletions

### Set Union Problem

* Dynamic partition of n-element set into disjoint subsets
* Initialize as n one-element subsets
* Perform sequence of union and search operations
* Applications: connected components in graphs

## Abstract Data Types (ADT)

* Set of abstract objects representing data items with associated operations
* Examples: priority queue, dictionary
* Implemented using classes in object-oriented languages (C++, Java)
* Encapsulates data and operations, promoting modularity and reusability