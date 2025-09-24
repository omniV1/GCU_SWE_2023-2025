### Brute Force and Exhaustive Search 

#### Introduction: 

**Brute Force** is a straight forward stragey to solving a problem. The force impled is that of a computer and not based on individual intelect. 

- Typically the easiest to apply. 

**Identifying bruteforce strategy**

- The Consecutive integer search 

- the definition-based algorithim for matrix multiplication 

### Selection Sort & Bubble Sort

**Consider the application of the brute-force approach to problem solving**: 

Given a list of n orderable items (e.g, numbers, characters, or character strings), rearrange them in nondecreasing order. 

**Selection Sort**: 

Start by scanning the entire given list to find its smallest element and exchange it with the first element, putting the smallest element in its final position in the sorted list. Then we scan the list, starting with the second to find the smallest among the last n - 1 elements and exchange it with the second element, putting the second smallest element in its final position. Generally, on the ith pass through the list, which we number from 0 to n-1, the algorithim searches for the smallest item among the last n - i elements and swaps it with Ai:

After n-1 passes, the list is sorted. 


**Bubble Sort**

Another brute-force application to the sorting problem is to compare adjacentelements of the list and exchange them if they are out of order. By doing itrepeatedly, we end up “bubbling up” the largest element to the last position onthe list. The next pass bubbles up the second largest element, and so on, untilafter n − 1 passes the list is sorted. Pass i(0 ≤ i ≤ n − 2) of bubble sort can berepresented by the following diagram: