


# Chapter 1

#### *Data Structures and Operations* 

The most common / important data structure is a matrix, a 2D array of numbers where each entry can be indexed via its row and column. Think of a Cartesian plane, or a CSV file. 

In linear algebra and even deep learning, operations such as multiplication and addition are done on the tabular data itself, but such operations can only be computed efficiently when the data is in solely numerical format.

### Matrix Operations

A Matrix can be added, subtracted, and multiplied—there is no division of matrices, but there exists a similar concept called inversion.

**Addition Operations** 

involve using Tuples. The first index represents the row number and the second index represents the column number. To add two matrices ( A + B), loop through each index(i,j) of the two matrices, sums the two entries at the current index, and places that result in the same index (i,j) of a new matrix C. 

![[screenshot-2026-01-08_13-38-07.png]]

This algorithm implies that we can’t add two matrices of different shapes, since indices that exist in one matrix wouldn’t exist in the other. It also implies that the final matrix C is of the same shape as A and B. 

---
### **Scalar matrix multiplication

In addition to adding matrices, we can multiply a matrix by a scalar. This involves simply taking the scalar and multiplying each of the entries of the matrix by it (the shape of the resultant matrix stays constant.

![[Pasted image 20260108134012.png]]

These two operations, addition of matrices and scalar-matrix multiplication, lead us directly to matrix subtraction, since computing A – B is the same as computing the matrix addition A + (–B), and computing –B is the product of a scalar –1 and the matrix B.

Multiplying two matrices starts to get interesting. For reasons beyond the scope of this text (motivations in a more theoretical flavor of linear algebra where matrices represent linear transformations), we define the matrix product 𝐴·𝐵 as:

![[Pasted image 20260108134526.png]]

In simpler terms, this means that the value at the index (i,j) of 𝐴·𝐵 is the sum of the product of the entries in the *i*th row of A with those of the jth column of B. Figure 1-4 is an example of matrix multiplication.

![[Pasted image 20260108134540.png]]

Note that matrix multiplication is not commutative, i.e., 𝐴·𝐵≠𝐵·𝐴. Of course, if we were to take a matrix A that is 2 by 3 and a matrix B that is 3 by 5, for example, by the rules of matrix multiplication, 𝐵·𝐴 doesn’t exist. However, even if the product were defined due to both matrices being, square, where square means that the matrix has an equal number of rows and columns, the two products will not be the same (this is an exercise for you to explore on your own). However, matrix multiplication is associative, i.e., 𝐴·(𝐵+𝐶)=𝐴·𝐵+𝐴·𝐶.

One of the most important matrices in linear algebra is the identity matrix, which is a square matrix with 1s along the main diagonal and 0s in every other entry. This matrix is usually denoted as I. When computing the product of I with any other matrix A, the result is always A—thus its name, the identity matrix. Try multiplying a few matrices of your choosing with the appropriate-sized identity matrix to see why this is the case.

---

### **Inversion** 

The inverse of matrix A is matrix B, such that AB = BA = I, the identity matrix (similar in idea to a number’s reciprocal—when dividing by a number on both sides of an equation, we can also think of this operation as multiplying both sides by its reciprocal). If such a B exists, we denote it as 𝐴-1. From this definition, we know that A must be, at the very least, a square matrix since we are able to multiply A on either side by the same matrix 𝐴-1, as you can see in Figure 1-6. Matrix inversion is deeply tied to other properties of matrices that we will discuss soon, which are the backbone of fundamental data science techniques. These techniques influenced their more complex neural variants, which researchers still use to this day.

![[Pasted image 20260108140100.png]]

### Vector Operations

