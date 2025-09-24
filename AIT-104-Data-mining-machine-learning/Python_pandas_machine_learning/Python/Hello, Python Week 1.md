
This paper will serve as a notepad for Week 1's lessons provided by Kaggle at [Course](https://www.kaggle.com/learn/python)!

# July 1 

- [x] Complete Module 1 
- [x] Complete Module 2
- [ ] complete Module 3




# Module 1 Notes

### Symbols

| Character | Definition                                                     | Example                                                                                                                        |
| --------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| :         | Starts a code block. <br><br>Similar to { } in other languages | if spam_amount > 0:<br>    print("But I don't want ANY spam!")<br><br>viking_song = "Spam Spam Spam"<br>print(viking_song)<br> |
|           |                                                                |                                                                                                                                |
|           |                                                                |                                                                                                                                |


# Thoughts: 

If you're a good programmer and familiar with other languages this course day will be light. The practice exercise are great and a good way to ease into learning. 




# Module 2 Notes
| Functions | Definition                                                                  | Example                                                                                                                                                                                                                                                                                                         | Usage                                                                                                                                                                                                                                                              |     |
| --------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| abs       | returns the absolute value of a specified number                            | x = abs(3+5j)<br>print(x) = 5.830951894845301                                                                                                                                                                                                                                                                   | it returns the positive value of the input. For complex numbers, it returns the magnitude of the number                                                                                                                                                            |     |
| help      | built-in function explains what built in functions will do in a given line  | help(print)                                                                                                                                                                                                                                                                                                     | Used when a dev wants to understand the built in functions                                                                                                                                                                                                         |     |
| round     | round a number to a given precision in decimal digits                       | help(round(2.01)2)                                                                                                                                                                                                                                                                                              | a built-in function used to round a number to a specified number of decimal places                                                                                                                                                                                 |     |
| docstring | triple quoted string that comes immediately after the header of a function. | def least_difference(a, b, c):<br>    """Return the smallest difference between any two numbers<br>    among a, b and c.<br>    <br>    >>> least_difference(1, 5, -5)<br>    4<br>    """<br>    diff1 = abs(a - b)<br>    diff2 = abs(b - c)<br>    diff3 = abs(a - c)<br>    return min(diff1, diff2, diff3) | help(least_difference)<br><br>Help on function least_difference in module __main__:<br><br>least_difference(a, b, c)<br>    Return the smallest difference between any two numbers<br>    among a, b and c.<br>    <br>    >>> least_difference(1, 5, -5)<br>    4 |     |
 
 
 

# Module 3 Notes


| Operators | Definition                                           | Usage                                                                                                                                                                                                                                                                                                                       |
| --------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| and       | returns true if both expressions are True            | True andTrue and False<br><br>False                                                                                                                                                                                                                                                                                         |
| or        | returns true if at least one expression returns True | True or True and False<br><br>Returns true                                                                                                                                                                                                                                                                                  |
| elif      | a contraction of else if                             | def inspect(x):<br>    if x == 0:<br>        print(x, "is zero")<br>    elif x > 0:<br>        print(x, "is positive")<br>    elif x < 0:<br>        print(x, "is negative")<br>    else:<br>        print(x, "is unlike anything I've ever seen...")<br><br>inspect(0)<br>inspect(-15)<br><br>0 is zero<br>-15 is negative |
