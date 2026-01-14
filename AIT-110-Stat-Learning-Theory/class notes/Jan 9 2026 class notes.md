[Notes from lecture](https://colab.research.google.com/drive/15Lq4kiSe4JkdOJifvjS4Ac2_jMODrdoI)

### Minutes

**Introductions**
1pm - 1:04pm 

**Terms and examples**
1:30 - 2pm

**Google Colab notes**
2:12 - 3pm

### Terms

**Population**: The data not dependent on size. Its just the data as a whole.(Parameter)

**Sample**: A (random) quantity of items from the population.
Sometimes has an issue of reference, statistical samples do not hold to relevance unless random. (statistic)

**Mean:** average is a type of parameter

**Variance:** Standard deviation - a length of distance from the mean always positive also a type of (parameter)

**Parameters:** Any characteristic of the population.

**Covariance:** is the measure between each parameter and compare how they interact with one another. 

**Correlation:** is the outcome of the covariance divided by the square root of the variance of x and y. is always between -1 and 1. If it is 0 there is no correlation between the covariance.  

**Bias:** is the difference between the actual and predicted outcome.

**High bias (underfitting):** not exactly what we want. It is too simple and will have large errors on both the training and the actual. 

**Low bias:** A model with low bias can capture complex pattern in data. may be prone to overfitting. 

**Irreducible Error:** Represents the noise in the data that cannot be reduced 
by any model. 

![[Pasted image 20260109141902.png]]
### Probability Concept review

Ex. Tossing 1 coin          

![[Pasted image 20260109142003.png]]

i) S is finite


ii) S is Infinite discreet {1,2,3,4,5,6,7.....}


ii) S is Continuous {- infinite, infinite} 

X is a random variable. 

This will imply X has values associated with probability. 

ex. X = # of T's in 1 Toss = {1, 0}

{ T, H }

P(T) = p, O <= p <= |

P(S(sample)) = P(T) + P(H) = 1

P(H) = 1 - P = outcome

---

EX. 2 

Roll 1 six-sided die

X = # of dots on the top face. 

X = {1, 2, 3, 4, 5, 6}

P(X=k) = 1/6

---

Toss 1 coin 3 times

S = { HHH HHT HTH THH  }
     THT TTH HTT TTT
     
 X = {3, 2, 1, 0 } = {0, 1 , 2, 3}
P(X=0) = 1/8
P(X=1) = 3/8
P(X=2) = 3/8
P(X=3) = 1/8

We know these distributions are correct because 1/8 + 3/8 + 3/8 + 1/8 = 8/8 OR 1


**Binomial Prob Distribution:**

Has a Probability Mass Functions or PMF 

Defined by
1. P(X=k) = (n / k)(p)^k(1-p)n-k


**Continuous Prob Distribution:** 

Requires integral for probability distributions. 




### Matrix 
See notes at [Fundamentals of Deep Learning](/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-204-Deep-Learning/class notes/Fundamentals of Deep Learning.md)


### Google Colab notes

[Lecture 2 notes](https://colab.research.google.com/drive/15Lq4kiSe4JkdOJifvjS4Ac2_jMODrdoI#scrollTo=8YvvCW7Q2ata)
