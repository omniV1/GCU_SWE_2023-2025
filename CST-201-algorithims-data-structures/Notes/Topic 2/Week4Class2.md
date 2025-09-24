# Week 4 class 2 Notes

### three efficiency types: 

- Worst: worst runtime
    
     - Means the algorithim is running for a long time.

     - affected by the size of the input. 

- Avg: avg runtime
    - What we should expect everytime. 
    - typical

- Best: fastest runtime
     - Fastest possible runtime of the alogrithim. 

### which efficiencies should be most important? 

- the one that works!

    - get it to work then implement futher

### what is amortized efficiency? 

- Running multiple algos over a dataset. 

### Notations for efficiencies
- Big O
    - Worst case: 
    - stands for order of
- Big theta
    - avg case: 
- Big Omega
    - best case: 

### What are these case efficiencies not good at?

- at calculating order of growth. 

- Saas: Software as a service helps, because we can control the system. 

### What types of alogrithims are these case efficiencies straight forward at? 

- non-recursive: recursion is approximate in theory. 

- when code is called outside your control then it becomes not straight forward. 

### What are all the order of growth classifications? 

- O(n) - linear

- O(log n) - logrithmic

- O(1) - constant 

- O(n2) - quadratic

### What is a possible issue with efficiency when looking at a recursive algorithim? 

- tend to be small! may hide inefficiencies. 

### What is tail recursion? 

- Make the recursive call at the tail or the end. 

- * IT IS THE LAST CALL. 

### How can that affect the efficiency calculation? 

- It prevents blowing the stack

- It runs faster. 

### What is the fundamental difference in efficiency between recursive algorithim and the iterative algorithim for comupting Fibonacci numbers? 

- 