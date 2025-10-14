

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

## 4.2 Namespaces and scope resolution

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

## Levels of scope

In fact four levels of scope exist. A level between the local function scope and global scope was omitted for clarity. A function can be defined within another function – in such a case the scope of the outer function is checked before the global scope is checked.

As the code executes, the global scope namespace is filled with names as they are defined. The function call creates a new namespace to track the variables in the function's local scope. The new local namespace automatically contains the parameter value `cals_left`. When the expression `cals_left - soda_cals` is evaluated, the interpreter finds `cals_left` in the local namespace, then finds `soda_cals` in the global namespace after unsuccessfully searching the local namespace.

As the code executes, the global scope namespace is filled with names as they are defined. The function call creates a new namespace to track the variables in the function's local scope. The new local namespace automatically contains the parameter value `cals_left`. When the expression `cals_left - soda_cals` is evaluated, the interpreter finds `cals_left` in the local namespace, then finds `soda_cals` in the global namespace after unsuccessfully searching the local namespace.

As the code executes, the global scope namespace is filled with names as they are defined. The function call creates a new namespace to track the variables in the function's local scope. The new local namespace automatically contains the parameter value `cals_left`. When the expression `cals_left - soda_cals` is evaluated, the interpreter finds `cals_left` in the local namespace, then finds `soda_cals` in the global namespace after unsuccessfully searching the local namespace.