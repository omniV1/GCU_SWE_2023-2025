##### Owen Lindsey
##### CST-250
##### 2/18/2024
##### Resources at bottom

#  CST-250 Activity 3: Recursion Examples in C#

## 1. Count to One

- The output for the number 29 using the specified algorithm is a sequence of numbers: 29, 30, 15, 16, 8, 4, 2, 1. This sequence demonstrates how the algorithm iteratively processes the number by either dividing it by 2 if it's even, or adding 1 if it's odd, until it reaches 1.
  
![CountToOne-29](https://github.com/omniV1/250/blob/main/Activities/Activity3_Recursion/screenshots/CountToOne-29.png)

## 2. Factorial


- Using both the iterative and recursive approaches to calculate the factorial of 6, the output is 720. This result demonstrates that both methods yield the same outcome, confirming that 
6!= 720
6!=720, which is the product of multiplying the number 6 by every positive integer less than itself (6 × 5 × 4 × 3 × 2 × 1).

![Factorial](https://github.com/omniV1/250/blob/main/Activities/Activity3_Recursion/screenshots/Factorial-6.png)


## 3. Greatest Common Divisor

- The Main method initializes two integers, number1 with a value of 250 and number2 with a value of 12. It then calls the gcd method with these two numbers and stores the result in the variable answer.
The gcd method checks if n2 is 0. If it is, the method returns n1 as the GCD. Otherwise, it prints the current remainder (n1 % n2) using Console.Out.WriteLine and calls itself recursively with n2 and n1 % n2 as the new parameters.
This recursive calling continues until n2 becomes 0. At each step, if n2 is not 0, it prints the message indicating the current remainder.
Once n2 becomes 0, it returns n1 as the GCD and prints the final result using Console.Out.WriteLine in the Main method.
The process continues recursively until it finds that the remainder is 0, at which point it concludes that the GCD is 2 (as you've already seen from the calculation).
Finally, it prints "The gcd of 250 and 12 is 2".

![GCD](https://github.com/omniV1/250/blob/main/Activities/Activity3_Recursion/screenshots/GCD-250-12.png)

## 4. KnightsTour


The screenshot shows a program attempting to solve the Knight's Tour problem, incrementing its attempt count by one million with each output line. This indicates a backtracking algorithm is at work, making a large number of moves to find a solution, and periodically reporting the number of moves attempted, reaching up to 47 million moves. The output does not confirm a successful tour; it merely tracks the algorithm's progress.

![KnightsTour](https://github.com/omniV1/250/blob/main/Activities/Activity3_Recursion/screenshots/KnightsTour.png)
