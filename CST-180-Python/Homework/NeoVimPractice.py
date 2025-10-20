# Create a big fizz buzz program that prints the numbers from 1 to 1000.

# initialize an empty list to store the results
fizz_buzz_list = []
# test.py
print("Hello world")

for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        fizz_buzz_list.append("FizzBuzz")
        print("FizzBuzz")
    elif i % 3 == 0:
        fizz_buzz_list.append("Fizz")
        print("Fizz")
    elif i % 5 == 0:
        fizz_buzz_list.append("Buzz")
        print("Buzz")
    else:
        fizz_buzz_list.append(str(i))
        print(i)
