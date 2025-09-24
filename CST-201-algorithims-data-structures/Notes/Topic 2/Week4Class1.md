# Week 4 class one notes:

### Review questions

#### What does immutability mean

- once instantied it cannot be changed. 

- most languages have garbage collectors for memory upkeep

#### What does fail fast mean

- make the program fail when it fails!

- do not pass back up the stack

- either throw the error or clean it 

- ensure the error is easily identifiable 

#### What is a subgraph

- a graph within a graph

- also pieces of the graph that contains known edges

#### What is the issue with using real time efficency 

- The run time may not always be accurate, because there are enviornment variables running at the same time. 

- Only as good as the system its ran on 

- use it as a guide is fine not a good measurment. However you may need to run tests thousands of times before an error occurs. 

#### What are types of efficiency analysis

1. time

2. space / resources

- EC: lookups vs inserts

#### What is searching and what does it need to be done? 

- search key / search criteria 

# Algorithim Effciency Analysis

#### What is analysis

- OOP factoring: breaking a problem down. 

- You cannot implement the big picture, it must be broken into discernable parts. 

#### What are the types efficiency analysis?

- time 

- space / resources

#### What does data size affect these efficiencies 

- if data is extremely large it will adversly effect the time and space complexity. 

- can the data be broken down further? Can we use more space to handle the time issue? 

#### What are some examples calculations of run time efficiencies? 

- hours, minutes, milliseconds, etc. WE USE THE CLOCK

#### What is the issue with using real time? 

- efficiency is not always related to time.

- the issue is real time is only as good as the system it runs on. 

- - use the measurements to find trends, not as  legitimate form of data on its own. 

#### What is a "Basic Operation"? 

- The lowest operation in the algorithim we can handle. Base Case in recusion is an example

#### What is the risk of calculating "Basic Operation" 

- its an approximation, it may be correct but the performance will change sometimes. 

#### How does order of growth play into efficiency calculations? 

- order of growth is the scalability of an algorithim. 

- When data gets bigger, does your algorithim behave properly? 

- Big O
 1. worst case senario this is where the alogrithim will perform. Describes upper bounds of an alogrithim.

O(1) Constant array loop
O(n) b search
O(log n) unsorted array search 

- Big theta
1. ideal scenario 

- Big omega 
1. average!  