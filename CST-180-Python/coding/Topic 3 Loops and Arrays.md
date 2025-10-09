

## 3.1

### List Basics

List is an object type. Defined by **container** and **mutable**. A **container** is an object that groups related objects together. <mark style="background: #ADCCFFA6;">A list is a mutable container (the size can expand or contract), it also has an order (sequence); thus contained objects maintain a left-to-right positional order. You can access elements in the list via indexing operations</mark> that specify the position of desired element in the list. Lists can be a different object type such as strings, integers, floats, or even other lists. 

A list can also be created using the built in list() function

list() accepts arguments such as list('abc') which takes a string argument, that string argument (this arg can be another list, string, tuple) and returns a new list with the elements ['a','b','c']. 


### Accessing list elements 

An **index** is a zero-based integer matching to a specific position in the list's sequence of elements.  

EX. 
```python
Owens_numbers = [10, 0, 5, 8, 0, 3]

if 0 in Owens_numbers:
    index = Owens_numbers.index(0)  # Gets first occurrence
    print(f"Element '0' is at index {index}")
else:
    print("Element '0' is not found")
```

this uses an integer to access the element at index 0 the element first element (10) of Owens_number.

An index can also be an expression as long as that expression evaluates into an integer. 

Replacing the index with an integer variable, such as in Owens_number, allows the programmer to quickly and easily lookup the i + 1 element in a list.

```python
oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 1) and (nth_person <= 5):
    print(f'The {nth_person}th oldest person lived {oldest_people[nth_person-1]} years')

```

**OUTPUT:** 

```text
Enter N (1-5): 3
The 3th oldest person lived 117 years
```


### Common list operations and in-place list modification 

The following table includes common operations performed on lists including creating lists, accessing list elements, slicing, and concatenation. Some of the operations might be familiar as sequence type operations also supported by strings. Note that slicing a list and concatenating two lists will return a new list.

Unlike the string sequence type, a list is mutable, meaning a list can grow and shrink without replacing the entire list with an updated copy. Such growing and shrinking capability is called in-place modification. The highlighted rows show in-place modification operations.

| Operation           | Description                                                           | Example code                                             | Example output  |
| ------------------- | --------------------------------------------------------------------- | -------------------------------------------------------- | --------------- |
| my_list = [1, 2, 3] | Creates a list.                                                       | my_list = [1, 2, 3]<br>print(my_list)                    | [1, 2, 3]       |
| list(iter)          | Creates a list.                                                       | my_list = list('123')<br>print(my_list)                  | ['1', '2', '3'] |
| my_list[index]      | Gets an element from a list.                                          | my_list = [1, 2, 3]<br>print(my_list[1])                 | 2               |
| my_list[start:end]  | Gets a _new_ list containing some of another list's elements.         | my_list = [1, 2, 3]<br>print(my_list[1:3])               | [2, 3]          |
| my_list1 + my_list2 | Gets a _new_ list with elements of my_list2 added to end of my_list1. | my_list = [1, 2] + [3] <br>print(my_list)                | [1, 2, 3]       |
| ==my_list[i] = x==      | ==Changes the value of the element at index i in-place.==                 | ==my_list = [1, 2, 3]<br>my_list[2] = 9 <br>print(my_list)== | ==[1, 2, 9]==       |
| ==del my_list[i]==      | ==Deletes the element from index i from a list.==                         | ==my_list = [1, 2, 3]<br>del my_list[1]<br>print(my_list)==  | ==[1, 3]==          |
The difference between in-place modification of a list and an operation that creates an entirely new list is important. In-place modification affects any variable that references the list and can have unintended side effects. Consider the following code in which the variables your_teams and my_teams reference the same list (via the assignment `your_teams = my_teams`). If either your_teams or my_teams modifies an element of the list, then the change is reflected in the other variable as well.

![[Pasted image 20250929061053.png]]

In the above example, changing the elements of my_teams also affects the contents of your_teams. The change occurs because my_teams and your_teams are bound to the same list object. The code `my_teams[1] = 'Lakers'` modifies the element in position 1 of the shared list object, thus changing the value of both my_teams[1] and your_teams[1].

The programmer of the above example probably meant to only change my_teams. The correct approach would have been to create a _copy_ of the list instead. One simple method to create a copy is to use slice notation with no start or end indices, as in `your_teams = my_teams[:]`.

![[Pasted image 20250929061206.png]]



## 3.2 List Basics

### Creating a list

A Container is a construct used to group related values together and contains references to other objects instead of data. A list is a container created by surrounding a sequence of variables or literals with brackets[]. 

Ex: `my_list = [10, 'abc']` creates a new list variable my_list that contains the two items: 10 and 'abc'. A list item is called an element. A list is mutable, meaning that the elements in a list can be replaced, reordered, or removed.

A list is also a sequence, meaning the contained elements are ordered by position in the list, known as the element's index, starting with 0. `my_list = [ ]` creates an empty list.

![[Pasted image 20250929065300.png]]

### Accessing list elements

Lists are useful for reducing the number of variables in a program. Instead of having a separate variable for the name of every student in a class, or for every word in an email, a single list can store an entire collection of related variables.

Individual list elements can be accessed using an indexing expression by using brackets as in my_list[i], where i is an integer. This allows a programmer to quickly find the i'th element in a list.

A list's index must be an integer. The index cannot be a floating-point type, even if the value is a whole number like 0.0 or 1.0. Using any type besides an integer will produce a runtime error, and the program will terminate.

![[Pasted image 20250929065247.png]]

Since lists are mutable, a programmer can also use methods to add and remove elements. A method instructs an object to perform some action, and is executed by specifying the method name following a "." symbol and an object. The append() list method is used to add new elements to a list. Elements can be removed using the pop() or remove() methods. Methods are covered in greater detail in another section.

**Adding elements to a list:**

- list.append(value): Adds value to the end of list. Ex: `my_list.append('abc')`

**Removing elements from a list:**

- list.pop(i): Removes the element at index i from list. Ex: `my_list.pop(1)`
- list.remove(v): Removes the first element whose value is v. Ex: `my_list.remove('abc')`
  
  ### Sequence-type methods and functions

Sequence-type functions are built-in functions that operate on sequences like lists and strings. Sequence-type methods are methods built into the class definitions of sequences like lists and strings. A subset of such functions and methods is provided below.

|Operation|Description|
|---|---|
|len(list)|Find the length of the list.|
|list1 + list2|Produce a new list by concatenating list2 to the end of list1.|
|min(list)|Find the element in the list with the smallest value. All elements must be of the same type.|
|max(list)|Find the element in the list with the largest value. All elements must be of the same type.|
|sum(list)|Find the sum of all elements of a list (numbers only).|
|list.index(val)|Find the index of the first element in the list whose value matches val.|
|list.count(val)|Count the number of occurrences of the value val in the list.|
![[Pasted image 20250929065908.png]]

Note that lists can contain mixed types of objects. Ex: `x = [1, 2.5, 'abc']` creates a new list x that contains an integer, a floating-point number, and a string. 

![[Pasted image 20250929070209.png]]


## 3.3 Dictionary basics 

### Creating a dictionary 

Consider a normal English language dictionary. A reader looks up the word "cat" and finds the definition, "A small, domesticated carnivore." The relationship between "cat" and its definition is _associative_, i.e., "cat" is associated with words describing "cat."

A **dictionary** is a Python container used to describe associative relationships. <mark style="background: #FFB8EBA6;">A dictionary is represented by the dict object type. A dictionary associates (or "maps") keys with values.</mark> A **key** is a term that can be located in a dictionary, such as the word "cat" in the English dictionary. A **value** describes some data associated with a **key**, such as a definition. <mark style="background: #FFB8EBA6;">A key can be any immutable type, such as a number, string, or tuple; a value can be any type.</mark>

A dict object is created using curly braces { } to surround the key:value pairs that comprise the dictionary contents. Ex: `players = {'Lionel Messi': 10, 'Cristiano Ronaldo': 7}` creates a dictionary called players with two keys: 'Lionel Messi' and 'Cristiano Ronaldo', associated with the values 10 and 7 (their respective jersey numbers). An empty dictionary is created with the expression `players = { }`.

<mark style="background: #FFB8EBA6;">Dictionaries are typically used in place of lists when an associative relationship exists.</mark> Ex: If a program contains a collection of anonymous student test scores, those scores should be stored in a list. However, if each score is associated with a student name, a dictionary could be used to associate student names to their score. <mark style="background: #FFB8EBA6;">Other examples of associative relationships include last names and addresses, car models and price, or student ID number and university email address.</mark>

Note that order _is_ maintained in the dict when printed (not standard before Python 3.7).

![[Pasted image 20250929071350.png]]

![[Pasted image 20250929071606.png]]
### Accessing dictionary entries

Though dictionaries maintain a left-to-right ordering, dictionary entries cannot be accessed by indexing. To access an entry, the key is specified in brackets [ ]. If no entry with a matching key exists in the dictionary, then a KeyError runtime error occurs and the program is terminated.

### Adding, modifying, and removing dictionary entries

A dictionary is mutable, so entries can be added, modified, and deleted as necessary by a programmer. A new dictionary entry is added by using brackets to specify the key: `prices['banana'] = 1.49`. A dictionary key is unique; attempting to create a new entry with a key that already exists in the dictionary _replaces_ the existing entry. The del keyword is used to remove entries from a dictionary: `del prices['papaya']` removes the entry whose key is 'papaya'. If the requested key to delete does not exist, then a KeyError occurs.

**Adding new entries to a dictionary:**

- dict[k] = v: Adds the new key-value pair k-v, if dict[k] does not already exist.  
    Example: `students['John'] = 'A+'`

**Modifying existing entries in a dictionary:**

- dict[k] = v: Updates the existing entry dict[k], if dict[k] already exists.  
    Example: `students['Jessica'] = 'A+'`

**Removing entries from a dictionary:**

- del dict[k]: Deletes the entry dict[k].  
    Example: `del students['Rachel']`

# 3.4 Loops (general)

### Loop concept

People who have children may be familiar with looping around the block until a baby falls asleep.

![[Pasted image 20250929073538.png]]

### Loop basics

A loop is a program construct that repeatedly executes the loop's statements (known as the loop body) while the loop's expression is true; when the expression is false, execution proceeds past the loop. Each time through a loop's statements is called an iteration.

![[Pasted image 20250929073707.png]]


1. A loop is like a branch, but the loop jumps back to the expression when done. Thus, the loop's statements may execute multiple times before execution proceeds past the loop.

2. This program receives an input value. If the value > -1, the program adds the value to a sum, receives another input, and repeats. val is 2, so the loop's statements execute, making sum 2.

3. The loop's statements ended by receiving the next input, which is 4. The loop's expression 4 > -1 is true, so the loop's statements execute again, making sum 2 + 4 or 6.

4. The loop's statements receive the next input of 1. The loop's expression 1 > -1 is true, so the loop's statements execute a third time, making sum 6 + 1 or 7.

5. The next input is -1. This time, -1 > -1 is false, so the loop is not entered. Instead, execution proceeds past the loop, where a statement puts sum, which is 7, to the output.



## 3.5 While loops

### While loop: Basics

A **while loop** is a construct that repeatedly executes an indented block of code (known as the loop body) as long as the loop's expression is True. 

At the end of the loop body, execution goes back to the while loop statement and the loop expression is evaluated _again_. 

If the loop expression is True, the loop body is executed again. <mark style="background: #FFB8EBA6;">But, if the expression evaluates to False, then execution instead proceeds to below the loop body.</mark> Each execution of the loop body is called an **iteration**, and looping is also called _iterating_.

### Example: While loop with a sentinel value

The following example uses the statement `while user_value != 'q':` to allow a user to end a face-drawing program by entering the character 'q'. The letter 'q' in this case is a sentinel value, a value that when evaluated by the loop expression causes the loop to terminate.

The code `print(user_value*5)` produces a new string, which repeats the value of user_value five times. In this case, the value of user_value may be "-", so the result of the multiplication is "-----". Another valid (but long) method is the statement `print(f'{user_value}{user_value}{user_value}{user_value}{user_value}')`.

Note that `input` may read in a multi-character string from the user, so only the first character is extracted from user_input with `user_value = user_input[0]`.

Once execution enters the loop body, execution continues to the body's end, even if the expression becomes False midway through.

![[Pasted image 20250929080826.png]]


Each iteration of the program below prints one line with the year and the number of ancestors in that year. (Note: the program's output numbers are largely due to not considering breeding among distant relatives, but nevertheless, a person has many ancestors.)

The program checks for `year_considered >= user_year` rather than for `year_considered != user_year`, because year_considered might be reduced past user_year without equaling it, causing an infinite loop. An infinite loop is a loop that will always execute because the loop's expression is always True. A common error is to accidentally create an infinite loop by assuming equality will be reached. Good practice is to include greater than or less than along with equality in a loop expression to help avoid infinite loops.

A program with an infinite loop may print output excessively, or just seem to stall (if the loop contains no printing). A user can halt a program by pressing Control-C in the command prompt running the Python program. Alternatively, some IDEs have a stop button.

![[Pasted image 20250929081110.png]]



## More While Loops 

Greatest Common Divisor

The following is an example of using a loop to compute a mathematical quantity. The program GCD, using Euclid's algorithm.

```text
If `num_a > num_b`, set `num_a` to `num_a - num_b`, else set `num_b` to `num_b - num_a`. Repeat until `num_a` equals `num_b`, at which point `num_a` and `num_b` both equal the GCD.`
```


### Conversation

Below is a program that has a "conversation" with the user. The program asks the user to type something and then randomly prints one of four possible responses until the user enters "Goodbye". Note that the first few lines of the program represent a <mark style="background: #BBFABBA6;">docstring</mark>: <mark style="background: #FFB8EBA6;">a multi-line string literal delimited at the beginning and end by triple quotes. Use either single (') or double (") quotes.</mark>

Each time through the while loop, the program will check if the user-entered string `user_text` is equal to the string literal "Goodbye". If the two strings are not equal, the while loop body executes. Within the while loop body, the program obtains a random number between 0 and 2 by using the random library. The randint() function provides a new random number each time the function is called. The arguments to randint(), 0 and 2, provide the minimum and maximum values that the function may return. Using the number given by randint(), the program's elif statements branch to a particular response.

### Example: Getting input until a sentinel is seen

Loops are commonly used to process a series of input values. A sentinel value is used to terminate a loop's processing. The example below computes the average of an input list of positive integers, ending with 0. The 0 is not included in the average.

![[Pasted image 20250930072907.png]]

## 3.7 For loops

A common programming task is to access all of the elements in a container. Ex: Printing every item in a list. A for loop statement loops over each element in a container one at a time, assigning a variable with the next element that can then be used in the loop body. The container in the for loop statement is typically a list, tuple, or string. Each iteration of the loop assigns the name given in the for loop statement with the next element in the container.

The for loop above iterates over the list `['Bill', 'Nicole', 'John']`. The first iteration assigns the variable name with 'Bill', the second iteration assigns name with 'Nicole', and the final iteration assigns name with 'John'. For sequence types like lists and tuples, the assignment order follows the position of the elements in the container, starting with position 0 (the leftmost element) and continuing until the last element is reached.

Iterating over a dictionary using a for loop assigns the loop variable with the _keys_ of the dictionary. The values can then be accessed using the key.

![[Pasted image 20250930081004.png]]

A for loop can also iterate over a string. Each iteration assigns the loop variable with the next character of the string. Strings are sequence types just like lists, so the behavior is identical (leftmost character first, then each following character).

![[Pasted image 20250930081248.png]]

### For loop examples

For loops can be used to perform action during each loop iteration. A simple example is printing the value, as above examples demonstrated. The program below uses an additional variable to sum list elements to calculate weekly and average daily revenue.

![[Pasted image 20250930081505.png]]

A for loop may also iterate backward over a sequence, starting at the last element and ending with the first element, by using the reversed() function to reverse the order of the elements.


## 3.8 While vs. for loops

### While loop and for loop correspondence

Both while loops and for loops can be used to count a specific number of loop iterations. A for loop combined with range() is generally preferred over while loops, since for loops are less likely to become stuck in an infinite loop situation. A programmer may easily forget to increment a while loop's variable (causing an infinite loop), but for loops iterate over a finite number of elements in a container and are thus guaranteed to complete.

![[Pasted image 20250930085221.png]]

## 3.9 Nested loops

### Nested loops

A nested loop is a loop that appears as part of the body of another loop. The nested loops are commonly referred to as the outer loop and inner loop.

Nested loops have various uses. One use is to generate all combinations of some items. Ex: The following program generates all two-letter .com Internet domain names. Recall that `ord()` converts a one-character string into an integer, and `chr()` converts an integer into a character. Thus, `chr(ord('a') + 1)` results in 'b'.

![[Pasted image 20250930123900.png]]

Modify the program to include two-character .com names where the second character can be a letter or a number, e.g., a2.com. Hint: Add a second while loop nested in the outer loop, but following the first inner loop, that iterates through the numbers 0-9.

![[Pasted image 20250930130109.png]]

Here is a nested loop example that graphically depicts an integer's magnitude by using asterisks, creating what is commonly called a _histogram_.

Run the program below and observe the output. Modify the program to print one asterisk per 5 units. So if the user enters 40, print 8 asterisks.

![[Pasted image 20250930130835.png]]

# 3.10 Break and continue

A break statement in a loop causes the loop to exit immediately. A break statement can sometimes yield a loop that is easier to understand.

In the example below, the nested for loops generate possible meal options for the number of empanadas and tacos that can be purchased. The inner loop body calculates the cost of the current meal option. If the meal cost is equal to the user's amount of money, the search is over, so the break statement immediately exits the inner loop. The outer loop body also checks if the meal cost and the user's amount of money are equal, and if so, that break statement exits the outer loop.

The program could be written without break statements, but the loops' condition expressions would be more complex and the program would require additional code, making the program harder to understand.

![[Pasted image 20251002115537.png]]

a = 1 
b = 1 
c = 0 

```python

Problem #1 
a = 1 
b = 1 
c = 0 

mult = 0 
while 1(a) < 10: 
	mult = 1(b) * 1(a)
	 if 1(mult) > 0(c): 
		break
# it breaks here and the line below do not execute
	a = 1(a) + 1 
# z gets set to a = 1
z = a
	 
Problem 2
a = 4
b = 5
c = 20 

mult = 0 
while 4(a) < 10: 
	mult = 5(b) * 4(a)
	 if 20(mult) > 20(c): 
		break
	a = 4(a) + 1 
# z gets set to a = 1
z = 5

# second run 

mult = 0 
while 5(a) < 10: 
	mult = 5(b) * 5(a)
	 if 25(mult) > 20(c): 
		break
# it breaks here and the line below do not execute
	#a = (a) + 1 
z = 5
```


### Continue statements

A continue statement in a loop causes an immediate jump to the while or for loop header statement. A continue statement can improve the readability of a loop. The example below extends the previous meal finder program to find meal options for which the total number of items purchased is evenly divisible by the number of diners. In addition, the following program will output all possible meal options, instead of reporting the first meal option found.

The program uses two nested for loops to try all possible combinations of tacos and empanadas. If the total number of tacos and empanadas is not exactly divisible by the number of diners (Ex: `(num_tacos + num_empanadas) % num_diners != 0`), the continue statement will immediately proceed to the next iteration of the for loop.

Break and continue statements can be helpful to avoid excessive indenting/nesting within a loop. However, because someone reading a program could easily overlook a break or continue statement, such statements should be used only when their use is clear to the reader.

![[Pasted image 20251002122725.png]]
```python
n = 4
stop = int(input())

for n in range(1, 6):
	print(n)
	
	if n >= stop: 
		print('stop')
		break
		
 # thoughts? 
 # 1 -> 6 run print n and if n is greater than or equal to the input of stop then print stop and exit
 
 #output 
 # 1
 # 2
 # 3
 # 4
 # stop
 
 # Problem 2
 # input of threshold is  = 3
 n = 0 
 threshold = int(input())
  
 for n in range(0, 5): 
	 if n >= threshold: 
		 print('_') 
		 continue 
		
	print(n)
	
	# Thoughts? 
	# n = 0 -> 3 print 0 1 2 on a new line then print _ _  on a new line
	
	# Problem 3
	a = int(input()) = 3
	b = int(input()) = 27
	c = int(input()) = 12
	
	# while 3 is less than 27 (TRUE) // while 6 is less than 27 (TRUE)
	# while 9 is less than 27 (TRUE)
	# while 12 is less than 27 (TRUE)
	# while 15 is less than 27 (TRUE)
	while a < b: 
		print(a) # 3 6 9 12 15
		# 3 is not greater than 12 // 6 is not greater than 12
		# 9 is not greater than 12 // 12 is equal to not greater than 12 
		# 15 greater than 12 BREAK
		if a > c: 
			break 
	a += 3    # a = 6 // 9 // 12  // 15
	
	
	# Problem 4
	stop = int(input()) = 11 
	
	for a in range(4):
		result = 0
		
		for b in range(3):
			result += b
			
		result += a
			
		print(result)
			
		if result > stop:
			break
			
# `a = 3`: prints `3`, `3 > 12`? No, continues, `a = 6`
# `a = 6`: prints `6`, `6 > 12`? No, continues, `a = 9`
# `a = 9`: prints `9`, `9 > 12`? No, continues, `a = 12`
# `a = 12`: prints `12`, `12 > 12`? No, continues, `a = 15`
# `a = 15`: prints `15`, `15 > 12`? **Yes, BREAK**

	# Problem 5
threshold = int(input()) = 2

for a in range(0,4):
	print(a + 1, end=': ')
	
	for b in range(0,1): 
		if a > threshold:
			print('_,',end='')
			continue
		print(b, end=',')
	print()
 
# a = 1: prints 1: b = 1 > 1 prints 0,
# a = 2: prints 2: b = 1 > 1 prints 0,
# final output = 1:0,
#                2:_
```

"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. Create a for loop that compares each character of the two strings. For each matching character, add one point to user_score. Upon a mismatch, end the loop.  
  
Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'

User score: 4
```python
user_score = 0
simon_pattern = input()
user_pattern  = input()

# Loop through each position (0, 1, 2, ... 9) 
for i in range(len(simon_pattern)): 
# Compare the character at position i in both strings 
	if simon_pattern[i] == user_pattern[i]: 
		user_score += 1 
	else: 
# Mismatch found, stop checking 
		break
print(f'User score: {user_score}')
```

# 3.11 Loop else

A loop may include an else clause that executes only if the loop terminates normally and doesn't use a break statement. Thus, the complete forms of while and for loops are:

![[Pasted image 20251002131427.png]]

The loop else construct executes if the loop completes normally. In the following example, a special message "All names printed" is displayed if the entire list of names is completely iterated through.

![[Pasted image 20251002131514.png]]

The country of Denmark allows parents to pick from around 7,000 names for newborn infants. Names not on the list must receive special approval from the Names Investigation Department of Copenhagen University. (Surprisingly, many countries have naming laws, probably to avoid names like "[Brfxxccxxmnpcccclllmmnprxvclmnckssqlbb11116](https://en.wikipedia.org/wiki/Naming_law_in_Sweden#Brfxxccxxmnpcccclllmmnprxvclmnckssqlbb11116)", pronounced "Albin".)

The program below checks if a user-entered name is an appropriate Danish name. If the name is not found in the list of legal names, then a suggestion is made to a close match. A close match is an acceptable name starting with the same letter. If no close matches are found, the loop else clause informs the user. If there are multiple names with the same letter, the first in the list is used.

Run the program below.

1. Enter the acceptable name "Bjork".
2. Try the name "Michaal", which is not an acceptable name. The program will suggest a replacement since there is an acceptable name starting with 'M'.
3. Try the name "Zoidberg", which is not an acceptable name. The list doesn't contain a name starting with 'Z', so the program will print a special message and terminate.

```python
# A few legal, acceptable Danish names
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn', 
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne', 
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia', 
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne', 
    'Dorte'
]

user_name = input('Enter desired name:\n')
if user_name in legal_names:
    print(f'{user_name} is an acceptable Danish name. Congratulations.')
else:
    print(f'{user_name} is not acceptable.')
    for name in legal_names:
        if user_name[0] == name[0]:
            print(f'You might consider: {name},', end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')
```

# 3.12 Counting

### Counting with a while loop

Commonly, a loop should iterate a specific number of times, such as 10 times. The programmer can use a variable to count the number of iterations, called a loop variable. To iterate N times using an integer loop variable i, a loop1 with the following form is used:

![[Pasted image 20251004185233.png]]

A common error is to forget to include the loop variable update (e.g., i = i +1) at the end of the loop, causing an unintended infinite loop.

The following program outputs the amount of money in a savings account each year for the user-entered number of years, with $10000 initial savings and 5% yearly interest:

![[Pasted image 20251004185308.png]]
![[Pasted image 20251004185517.png]]

### Other forms of counting

Counting down is also common, as in counting from 5 to 1. The loop body executes when i is 5, 4, 3, 2, and 1, but the loop body does not execute when i reaches 0.
![[Pasted image 20251004185638.png]]

The loop body executes when i is 5, 4, 3, 2, and 1, but the loop body does not execute when i reaches 0.

Counting sometimes occurs by steps greater than 1. Ex: A loop that prints even values from 0 to 100 (i.e., counts from 0 to 100 by 2s) is:

![[Pasted image 20251004185654.png]]
![[Pasted image 20251004185832.png]]

### Calculate a factorial.

Write a program that lets a user enter N and that outputs N! (N factorial, meaning N*(N-1)*(N-2)*...*2*1). Hint:Use a loop variable i that counts from total-1 down to 1. Compare your output with some of these answers: 1:1, 2:2, 3:6, 4:24, 5:120, 8:40320.

![[Pasted image 20251004191310.png]]

### Shorthand operators

Because assignments such as `i = i + 1` are so common in programs, the programming language provides a shorthand version: `i += 1`. Similar operators include +=, -=, *=, and /=. For example, `num *= x` is shorthand for `num = num * x`. The item on the right can be an expression, so `num *= x + y` is shorthand for `num = num * (x + y)`. Usage of such operators is common in loops.

![[Pasted image 20251004191322.png]]

### 3.13 LAB: Password modifier

Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

- i becomes 1
- a becomes @
- m becomes M
- B becomes 8
- s becomes $

Ex: If the input is:

```
mypassword
```

the output is:

```
Myp@$$word!
```

_Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given `password` variable._

# 3.16 List methods

### Common list methods

A list method can perform a useful operation on a list such as adding or removing elements, sorting, reversing, etc.

The table below shows the available list methods. Many of the methods perform in-place modification of the list contents — a programmer should be aware that a method that modifies the list in-place changes the underlying list object, and thus may affect the value of a variable that references the object.

![[Pasted image 20251004194517.png]]

![[Pasted image 20251004194526.png]]

A good practice is to use list methods to add and delete list elements, rather than alternative add/delete approaches. Alternative approaches include syntax such as `my_list[len(my_list):] = [val]` to add to a list, or `del my_list[0]` to remove from a list. Using a list method yields more readable code.

The list.sort() and list.reverse() methods rearrange a list element's ordering, performing in-place modification of the list.

The list.index() and list.count() return information about the list and do not modify the list.

## 3.16.1: In-place modification using list methods.

1. vals is a list containing elements 1, 4, and 16.
2. The statement vals.append(9) appends element 9 to the end of the list.
3. The statement vals.insert(2, 18) inserts element 18 into position 2 of the list.
4. The statement vals.pop() removes the last element, 9, from the list.
5. The statement vals.remove(4) removes the first instance of element 4 from the list.
6. The statement vals.remove(55) removes the first instance of element 55 from the list. The list does not contain the element 55 so vals is the same.
   
## 3.17 List slicing

A programmer can use slice notation to read multiple elements from a list, creating a new list that contains only the desired elements. The programmer indicates the start and end positions of a range of elements to retrieve, as in `my_list[0:2]`. The 0 is the position of the first element to read, and the 2 indicates the last element. Every element between 0 and 2 from my_list is in the new list. The end position, 2, is _not_ included in the resulting list.

![[Pasted image 20251009144854.png]]

The slice `boston_bruins[0:2]` produces a new list containing the elements in positions 0 and 1: ['Tyler', 'Zdeno']. The end position is _not_ included in the produced list – to include the final element of a list in a slice, specify an end position past the end of the list. Ex: `boston_bruins[1:3]` produces the list ['Zdeno', 'Patrice'].

![[Pasted image 20251009145150.png]]

An optional component of slice notation is the stride, which indicates how many elements are skipped between extracted items in the source list. Ex: The expression my_list[0:5:2] has a stride of 2, thus skipping every other element, and resulting in a slice that contains the elements in positions 0, 2, and 4. The default stride value is 1 (the expressions my_list[0:5:1] and my_list[0:5] being equivalent).

If the reader has studied string slicing, then list slicing should be familiar. In fact, slicing has the same semantics for most sequence-type objects

A table of common list slicing operations is given below. Note that omission of the start or end positions, such as my_list[:2] or my_list[4:], has the same meaning as in string slicing. my_list[:2] includes every element up to position 2. my_list[4:] includes every element following position 4 (including the element at position 4).

## Table 3.17.1: Common list slicing operations.

|Operation|Description|Example code|Example output|
|---|---|---|---|
|my_list[start:end]|Get a list from start to end (minus 1).|`my_list = [5, 10, 20]   print(my_list[0:2])`|[5, 10]|
|my_list[start:end:stride]|Get a list of every stride element from start to end (minus 1).|`my_list = [5, 10, 20, 40, 80]   print(my_list[0:5:3])`|[5, 40]|
|my_list[start:]|Get a list from start to end of the list.|`my_list = [5, 10, 20, 40, 80]   print(my_list[2:])`|[20, 40, 80]|
|my_list[:end]|Get a list from beginning of the list to the end (minus 1).|`my_list = [5, 10, 20, 40, 80]   print(my_list[:4])`|[5, 10, 20, 40]|
|my_list[:]|Get a copy of the list.|`my_list = [5, 10, 20, 40, 80]   print(my_list[:])`|[5, 10, 20, 40, 80]|
![[Pasted image 20251009150054.png]]

## 3.18 Tuple basics