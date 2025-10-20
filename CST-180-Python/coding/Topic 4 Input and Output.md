

## 4.1 User-defined function basics

### Functions (general)

A program may perform the same operation repeatedly, causing a large and confusing program due to redundancy. Program redundancy can be reduced by creating a grouping of predefined statements for repeated operations, known as a function. Even without redundancy, functions can prevent a main program from becoming large and confusing.

### Function basics

A function is a named series of statements.

- A function definition consists of the function's name and a block of statements. Ex: `def calc_pizza_area():` is followed by an indented block of statements.
- A function call is an invocation of the function's name, causing the function's statements to execute.

Python comes with a number of built-in functions, such as `input()`, `int()`, `len()`, etc. The def keyword is used to create new functions.

The function call calc_pizza_area() in the animation below causes execution to jump to the function's statements. Execution returns to the original location after executing the function's last statement.

Good practice is to follow the convention of naming functions with lowercase letters and underscores, such as get_name or calc_area.

Other aspects of function definition, like the (), are discussed later.


### Return statements

A function may return one value using a return statement. Below, the compute_square() function returns the square of its argument.

A function can return only one item, not two or more (though a list or a tuple with multiple elements could be returned). A function with no return statement, or a return statement with no following expression, returns the value `None`. None is a special keyword that indicates no value.

A return statement may appear at any point in a function, not just as the last statement. A function may also contain multiple return statements in different locations.

### Parameters

A programmer can influence a function's behavior via an input.

- A parameter is a function input specified in a function definition. Ex: A pizza area function might have diameter as an input.
- An argument is a value provided to a function's parameter during a function call. Ex: A pizza area function might be called as `calc_pizza_area(12.0)` or as `calc_pizza_area(16.0)`.

A parameter is like a variable definition. Upon entering the function, the parameter is bound to the argument object provided by the call, creating a shared reference to the object. Upon return, the parameter can no longer be used.

An argument may be an expression, like `12.0`, `x`, or `x * 1.5`.

### Multiple or no parameters

A function may have multiple parameters separated by commas. Parameters are assigned with argument values: First parameter with the first argument, second with the second, etc.

A function definition with no parameters must still have the parentheses, as in: `def calc_something():`. The call to such a function must include parentheses and must be empty, as in: `calc_something()`.

### Hierarchical function calls

A function's statements may include function calls, known as hierarchical function calls or nested function calls. Code such as `user_input = int(input())` consists of such a hierarchical function call, in which the input() function is called and evaluates to a value that is then passed as an argument to the int() function.

# 4.2 Namespaces and scope resolution

### Namespace

A namespace maps names to objects. The Python interpreter uses namespaces to track all of the objects in a program. For example, when executing `z = x + y`, the interpreter looks in a namespace to find the value of the objects referenced by `x` and `y`, evaluates the expression, and then updates `z` in the namespace with the expression's result.

A namespace is a normal Python dictionary whose keys are the names and whose values are the objects. A programmer can examine the names in the current local and global namespace by using the `locals()` and `globals()` built-in functions.

```python
print('Initial global namespace: ')
print(globals())

my_var = "This is a variable"
print('\nCreated new variable')
print(globals())

def my_func():
    pass

print('\nCreated new function')
print(globals())

                           ---OUTPUT---
Initial global namespace: 
{}
 
Created new variable
{'my_var': 'This is a variable'}
 
Created new function
{'my_var': 'This is a variable', 'my_func': <function my_func at 0x2349d4>}
```

By default, a few names already exist in the global namespace – those names have been omitted in the output for brevity. Notice that `my_var` and `my_func` are added into the namespace once assigned.

### Scope and scope resolution

Scope is the area of code where a name is visible. Namespaces are used to make scope work. Each scope, such as global scope or a local function scope, has its own namespace. If a namespace contains a name at a specific location in the code, then that name is visible and a programmer can use it in an expression.

At least three nested scopes are active at any point in a program's execution:

1. Built-in scope – Contains all of the built-in names of Python, such as `int()`, `str()`, `list()`, `range()`, etc.
2. Global scope – Contains all globally defined names outside of any functions.
3. Local scope – Refers to scope within the currently executing function but is the same as global scope if no function is executing.

When a name is referenced in code, the local scope's namespace is the first checked, followed by the global scope, and finally the built-in scope. If the name cannot be found in any namespace, the interpreter generates a `NameError`. The process of searching for a name in the available namespaces is called scope resolution.

### Levels of scope

In fact four levels of scope exist. A level between the local function scope and global scope was omitted for clarity. A function can be defined within another function – in such a case the scope of the outer function is checked before the global scope is checked.

As the code executes, the global scope namespace is filled with names as they are defined. The function call creates a new namespace to track the variables in the function's local scope. The new local namespace automatically contains the parameter value `cals_left`. When the expression `cals_left - soda_cals` is evaluated, the interpreter finds `cals_left` in the local namespace, then finds `soda_cals` in the global namespace after unsuccessfully searching the local namespace.

As the code executes, the global scope namespace is filled with names as they are defined. The function call creates a new namespace to track the variables in the function's local scope. The new local namespace automatically contains the parameter value `cals_left`. When the expression `cals_left - soda_cals` is evaluated, the interpreter finds `cals_left` in the local namespace, then finds `soda_cals` in the global namespace after unsuccessfully searching the local namespace.

As the code executes, the global scope namespace is filled with names as they are defined. The function call creates a new namespace to track the variables in the function's local scope. The new local namespace automatically contains the parameter value `cals_left`. When the expression `cals_left - soda_cals` is evaluated, the interpreter finds `cals_left` in the local namespace, then finds `soda_cals` in the global namespace after unsuccessfully searching the local namespace.

### More scoping and namespaces

The concept of scopes and namespaces explains how multiple variables can share the same name, yet have different values. Consider the following program that first creates a variable `tmp` in the global namespace, then creates another variable named `tmp` in a local function. The assignment statement in the `avg()` function creates a new variable within the function's local namespace. When the function returns, the namespace is deleted as well (since the local variables are now out of scope). The later statement `print f'Sum: {tmp:f}'` looks up the name `tmp` in the global scope, finding the `tmp` previously created with the statement `tmp = a + b`.

Note that the Python Tutor tool below uses the term "frame" in place of "namespace".

By default, any assignment statement automatically creates (or modifies) a name in the local namespace only, even if the same name exists in a higher global or built-in scope. A global statement such as global tmp forces the interpreter to consider the variable in the global scope, thus allowing modification of existing global variables instead of creating local variables.

# 4.3 Print functions

**Printing from a function**

A common operation for a function is to print text. Large text outputs can clutter the main program, especially if the text needs to be output multiple times. A function that only prints typically does not return a value. A function with no return statement is called a void function, and such a function returns the value None.

A function that produces output can also return a value, but this material separates these operations for clarity. A function that both outputs and returns a value is not void.

Calling a print function multiple times
One benefit of a print function is that complex output statements can be written in code once. Then the print function can be called multiple times to produce the output instead of rewriting complex statements for every necessary instance. Changes to output and formatting are made easier and are less prone to error.

![[Pasted image 20251020144256.png]]

# 4.4 Dynamic typing

**Dynamic and static typing**

A programmer can pass any type of object as an argument to a function. Consider a function add(x, y) that adds the two parameters:
![[Pasted image 20251020144341.png]]

A programmer can call the add() function using two integer arguments, as in add(5, 7), which returns a value of 12. Alternatively, a programmer can pass in two string arguments, as in add('Tora', 'Bora'), which would concatenate the two strings and return 'ToraBora'.

The function's behavior of adding together different types is a concept called polymorphism. Polymorphism is an inherent part of the Python language. For example, consider the multiplication operator. 

*If the two operands are numbers, then the result is the product of those two numbers. If one operand is a string and the other an integer (e.g., 'x' * 5), then the result is a repetition of the string five times: 'xxxxx'.

Python uses dynamic typing to determine the type of objects as a program executes. Ex: The consecutive statements num = 5 and num = '7' first assign with an integer type and then a string type. The type of num can change depending on the value it references. The interpreter is responsible for checking that all operations are valid as the program executes. If the function call add(5, '100') is evaluated, an error is generated when adding the string to an integer.

In contrast to dynamic typing, many other languages like C, C++, and Java use static typing, which requires the programmer to define the type of every variable and every function parameter in a program's source code. Ex: string name = "John" declares a string variable in C++. When the source code is compiled, the compiler attempts to detect non type-safe operations, and halts the compilation process if such an operation is found.

Dynamic typing typically allows for more flexibility of the code that a programmer can write, but at the expense of potentially introducing more bugs, since there is no compilation process by which types can be checked.

Python uses duck typing, a form of dynamic typing based on the maxim, "If a bird walks, swims, and quacks like a duck, then call it a duck." For example, if an object can be concatenated, sliced, indexed, and converted to lower case, doing everything that a string can do, then treat the object like a string.

# 4.5 Reasons for defining functions

**Improving program readability**

Programs can become hard for humans to read and understand. Decomposing a program into functions can aid program readability, yield an initially correct program, and ease future maintenance. The following program contains two user-defined functions, making the main program (after the function definitions) easier to read and understand. For larger programs, the effect is even greater.

![[Pasted image 20251020144511.png]]

Modular program development
Programmers commonly use functions to write programs modularly. Modular development is the process of dividing a program into separate modules that can be developed and tested separately and integrated into a single program.

A programmer can use function stubs (described in depth elsewhere) to capture the high-level behavior of the required functions (or modules) before diving into the details of each function, like planning a route for a road trip before starting to drive.

Avoid writing redundant code
A function can be defined once, then called from multiple places in a program, thus avoiding redundant code. Examples of such functions are math module functions like sqrt() that relieve a programmer from having to write several lines of code each time a square root needs to be computed.

The skill of decomposing a program's behavior into a good set of functions is a fundamental part of programming that helps characterize a good programmer. Each function should have easily recognizable behavior, and the behavior of the main program (and any function that calls other functions) should be easily understandable via the sequence of function calls.

A general guideline (especially for beginner programmers) is that a function's definition usually shouldn't have more than about 30 lines of code, although this guideline is not a strict rule.

![[Pasted image 20251020144542.png]]


# 4.6 Functions with branches/loops

**Example: Auction website fee calculator**

**Note:** This section requires knowledge of if-else and loop statements.
A function's block of statements may include branches, loops, and other statements. The following example uses a function to compute the fee charged by eBay when a user sells an item online.

![[Pasted image 20251020144648.png]]

# 4.7 Functions are objects

**Functions as objects**

A function is also an object in Python, having a type, identity, and value. A function definition like def print_face(): creates a new function object with the name print_face bound to that object.

A part of the value of a function object is compiled bytecode that represents the statements to be executed by the function. A bytecode is a low-level operation, such as adding, subtracting, or loading from memory. One Python statement might require multiple bytecode operations. Ex: The function below adds 1 to an argument and returns the result. The corresponding bytecode for the function requires 4 bytecode operations to perform the addition, and 2 to return the result.

![[Pasted image 20251020144748.png]]


All Python code is compiled before execution by the interpreter. Statements entered in an interactive interpreter are compiled immediately, then executed. Modules are compiled when imported, and functions are compiled when the interpreter evaluates the function definition.

A statement like print_face() causes the function object to execute a call operation, which in turn executes the function's bytecode. A programmer never has to deal with bytecode – bytecode is used internally by the interpreter.

Because a function is an object, a function can be used in an assignment statement just like other objects. This is illustrated in the following animation.

![[Pasted image 20251020144822.png]]

The interpreter creates a new function object when the definition def print_face() is evaluated. The function object contains as part of its value the function's bytecode. Since a function is just an object, assignment operations work the same: func = print_face binds the name func to the same object as print_face, thus creating multiple names for a single function. Both func() and print_face() perform the same call operation and jump execution to print_face.

Functions can be passed like any other object as an argument to another function. Consider the following example, which defines two different functions: print_human_head() and print_monkey_head(). A third function, print_figure(), accepts a function as an argument, calling that function to print a head and then print a body.Passing functions as arguments can sometimes improve the readability of code. The above example could have been implemented using an if statement to call either print_human_head() or print_monkey_head() followed by a call to a print_body() function. However, the code is simplified by reducing the required number of function calls in the first code block to the more simple print_figure(face).

Whereas objects like integers support many operations (adding, subtracting, etc.), functions only support the call operation.

Function attributes
Functions also support adding attributes with the attribute reference "." operator, but that concept is out of scope for the discussion here.

# 4.8 Functions: Common errors

**Copy-paste errors**

A common error is to copy and paste code among functions but not complete all necessary modifications to the pasted code. For example, a programmer might have developed and tested a function to convert a temperature value in Celsius to Fahrenheit, and then copied and modified the original function into a new function to convert Fahrenheit to Celsius as shown:

![[Pasted image 20251020144920.png]]

The programmer forgot to change the return statement to return Celsius rather than Fahrenheit. Copying and pasting code is a common and useful time-saver and can reduce errors by starting with correct code. When you copy and paste code, be extremely vigilant in making all necessary modifications. Just as dark alleys or wet roads may be dangerous and cause you to observe your surroundings or drive carefully, the awareness of error potential in copying and pasting may cause you to modify a pasted function correctly.

**Return errors**

Another common error is to return the wrong variable, like if return temperature had been used in the temperature conversion program by accident. The function will work and sometimes even return the correct value.

Another common error is to fail to return a value for a function. If execution reaches the end of a function's statements without encountering a return statement, then the function returns a value of None. If the function is expected to return an actual value, then such an assignment can cause confusion.

# 4.9 Function arguments

**Function arguments and mutability**

Arguments to functions are passed by object reference, a concept known in Python as pass-by-assignment. When a function is called, new local variables are created in the function's local namespace by binding the names in the parameter list to the passed arguments.

![[Pasted image 20251020145050.png]]


The semantics of passing object references as arguments is important because modifying an argument that is referenced elsewhere in the program may cause side effects outside of the function scope. When a function modifies a parameter, whether or not that modification is seen outside the scope of the function depends on the mutability of the argument object.

If the object is immutable, such as a string or integer, then the modification is limited to inside the function. Any modification to an immutable object results in the creation of a new object in the function's local scope, thus leaving the original argument object unchanged.
If the object is mutable, then in-place modification of the object is seen outside the scope of the function. Any operation like adding elements to a container or sorting a list that is performed within a function will also affect any other variables in the program that reference the same object.
The following program illustrates how the modification of a list argument's elements inside a function persists outside of the function call.

Sometimes a programmer needs to pass a mutable object to a function but wants to make sure that the function does not modify the object at all. One method to avoid unwanted changes is to pass a copy of the object as the argument instead, like in the statement my_func(num_list[:]).

# 4.10 Keyword arguments and default parameter values

**Keyword arguments**

Sometimes a function requires many arguments. In such cases, a function call can become very long and difficult to read. Furthermore, a programmer might easily make a mistake when calling such a function if the ordering of the arguments is given incorrectly. Consider the following program:

Figure 4.10.1: A function with many arguments.
```python
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description('The Lord of the Rings', 'J. R. R. Tolkien', 'George Allen & Unwin', 
                       1954, 1.0, 22, 456)
```

In the example above, a programmer might very easily swap the positions of some of the arguments in the function call, potentially introducing a bug into the program. Python provides for keyword arguments that allow arguments to map to parameters by name, instead of implicitly by position in the argument list. When using keyword arguments, the argument list does not need to follow a specific order.

Figure 4.10.2: Using keyword arguments.
```python

def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
                       year=1954, author='J. R. R. Tolkien', version=1.0,
                       num_pages=456, num_chapters=22)
```


Keyword arguments provide a bit of clarity to potentially confusing function calls. Good practice is to use keyword arguments for any function containing more than approximately four arguments.

Keyword arguments can be mixed with positional arguments, provided that the keyword arguments come last. A common error is to place keyword arguments before all position arguments, which generates an exception.

Figure 4.10.3: All keyword arguments must follow positional arguments.
```python
def split_check(amount, num_people, tax_percentage, tip_percentage):
    # ...

split_check(125.00, tip_percentage=0.15, num_people=2, tax_percentage=0.095)
```


**Default parameter values**
Sometimes a function has parameters that are optional. A function can have a default parameter value for one or more parameters, meaning that a function call can optionally omit an argument, and the default parameter value will be substituted for the corresponding omitted argument.

The following function prints a date in a particular style, given parameters for day, month, and year. The fourth parameter indicates the desired style, with 0 meaning American style, and 1 meaning European style. For July 30, 2012, the American style is 7/30/2012 and the European style is 30/7/2012.

Figure 4.10.4: Parameter with a default value.
```python
def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(f'{month}/{day}/{year}')
    elif style == 1:  # European
        print(f'{day}/{month}/{year}')
    else:
        print('Invalid Style')

print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1)
print_date(30, 7, 2012)  # style argument not provided! Default value of 0 used.
7/30/2012
30/7/2012
7/30/2012
```

The fourth (and last) parameter is defined with a default value: style=0. If the function call does not provide a fourth argument, then style has value 0. A parameter's default value is the value used in the absence of an argument in the function call.

The same can be done for other parameters, as in: def print_date(day=1, month=1, year=2000, style=0). If positional arguments are passed (i.e., not keyword-arguments), then only the last arguments can be omitted. The following are valid calls to this print_date() function:

Figure 4.10.5: Valid function calls with default parameter values.
```python
print date(30, 7, 2012, 0)   # Defaults: none
print_date(30, 7, 2012)      # Defaults:                            style=0
print_date(30, 7)            # Defaults:                 year=2000, style=0
print_date(30)               # Defaults:        month=1, year=2000, style=0
print_date()                 # Defaults: day=1, month=1, year=2000, style=0
```

If a parameter does not have a default value, then failing to provide an argument (either keyword or positional) generates an error.

A common error is to provide a mutable object, like a list, as a default parameter. Such a definition can be problematic because the default argument object is created only once, at the time the function is defined (when the script is loaded), and not every time the function is called. Modification of the default parameter object will persist across function calls, which is likely not what a programmer intended. The below program demonstrates the problem with mutable default objects and illustrates a solution that creates a new empty list each time the function is called.

![[Pasted image 20251020145527.png]]

The left program shows a function append_to_list() that has an empty list as default value of my_list. A programmer might expect that each time the function is called without specifying my_list, a new empty list will be created and the result of the function will be [value]. However, the default object persists across function calls. The solution replaces the default list with None, checking for that value, and then creating a new empty list in the local scope if necessary.

Mixing keyword arguments and default parameter values
Mixing keyword arguments and default parameter values allows a programmer to omit arbitrary arguments from a function call. Because keyword arguments use names instead of position to match arguments to parameters, any argument can be omitted as long as that argument has a default value.

Consider the print_date function from above. If every parameter has a default value, then the user can use keyword arguments to pass specific arguments anywhere in the argument list. Below are some sample function calls:

Figure 4.10.7: Mixing keyword arguments and default parameter values allows omitting arbitrary arguments.
```python
def print_date(day=1, month=1, year=2000, style=0):
    # ...
print_date(day=30, year=2012)   # Defaults:        month=1,            style=0
print_date(style=1)             # Defaults: day=1, month=1, year=2000
print_date(year=2012, month=4)  # Defaults: day=1,                     style=0
```
