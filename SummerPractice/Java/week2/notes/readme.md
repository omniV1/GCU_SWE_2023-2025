# Week 2 Java Refresher - Detailed Summary of Concepts

## Overview

This guide provides a detailed summary of the key concepts used in the Java application that processes user input to display either vowels or consonants along with their positions. It leverages Java and object-oriented programming principles to perform string processing and display results.

## Topics Covered

### 1. Data Types and Variables
- **Primitive Types**: `int`, `double`, `char`, `boolean`, `float`, `long`, `byte`, `short`
- **Reference Types**: `String`

#### Code Example
``` java
int number = 10; 
double decimalNumber = 26.5;
char letter = 'A';
String message = "HI I AM OWEN";
boolean isTrue = true; 
float floatNumber = 5.5f; 
long longNumber = 10000000L; 
byte byteNumber = 2; 
short shortNumber = 100;
```
#### Notes
- Primitive types store simple values.
- Reference types store references to objects.

### 2. Control Structures
- **Conditionals**: `if`, `else`, `switch`
- **Loops**: `for`, `while`

#### Code Example
``` java
if (number > 5) {
    System.out.println("Number is greater than 5"); 
} else {
    System.out.println("Number is 5 or less");
}

for (int i = 0; i < 5; i++) {
   System.out.println("For Loop: " + i); 
}

int count = 0; 
while (count < 5) {
    System.out.println("While Loop: " + count); 
    count++; 
}

switch (number) { 
    case 10: 
        System.out.println("Number is 10"); 
        break; 
    case 5: 
        System.out.println("Number is 5");
        break; 
    default: 
        System.out.println("Number is not 10 or 5"); 
}
```
#### Notes
- Conditionals control the flow of execution based on boolean conditions.
- Loops repeat a block of code multiple times.

### 3. Arrays and Collections
- **Arrays**: Fixed-size sequences of elements of the same type.
- **ArrayList**: Resizable-array implementation of the List interface.

#### Code Example
``` java
int[] numbers = {1, 2, 3, 4, 5}; 
for (int num : numbers) {
    System.out.println("Array element: " + num); 
}

ArrayList<String> fruits = new ArrayList<>(); 
fruits.add("apple"); 
fruits.add("Banana"); 
fruits.add("Cherry"); 
for (String fruit : fruits) {
    System.out.println("ArrayList element: " + fruit);
}
```
#### Notes
- Arrays have a fixed size.
- ArrayLists can dynamically resize and offer more functionality.

### 4. Methods and Parameters
- **Method Overloading**: Same method name with different parameters.
- **Recursive Methods**: Methods that call themselves.

#### Code Example
``` java
public static void printMessage(String msg) {
    System.out.println(msg); 
}

public static void printMessage(String msg, int times) {
    for (int i = 0; i < times; i++) {
        System.out.println(msg); 
    }
}

public static int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```
#### Notes
- Methods encapsulate reusable code blocks.
- Overloading allows methods to have the same name but different parameters.
- Recursion is a powerful tool for solving problems that can be broken down into smaller, similar problems.

### 5. Object-Oriented Programming (OOP) Basics
- **Classes and Objects**: Defining and creating instances.
- **Encapsulation**: Using getters and setters to control access.
- **Inheritance**: Creating a subclass (Employee) that inherits from a superclass (Person).
- **Polymorphism**: Overriding methods in the subclass.
- **Interfaces**: Defining methods that a class (Employee) must implement.

#### Code Example
``` java
class Person {
    private String name; 
    private int age; 

    public String getName() {
        return name; 
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age; 
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void introduce() {
        System.out.println("HI MY NAME IS " + name + " MY AGE IS " + age + " YEARS OLD"); 
    }
}

public interface Greetable {
    void greet(); 
} 

class Employee extends Person implements Greetable {
    private String company; 

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company; 
    }

    @Override
    public void introduce() {
        super.introduce();
        System.out.println("I work at: " + company); 
    }

    @Override 
    public void greet() {
        System.out.println("Hello, welcome to: " + company); 
    }
}
```
#### Notes
- Classes are blueprints for creating objects.
- Objects are instances of classes.
- Fields are variables inside a class.
- Properties provide controlled access to fields.
- Methods are functions inside a class.
- Encapsulation restricts access to certain details and exposes only necessary parts.
- Inheritance allows a new class to inherit properties and behavior from an existing class.
- Polymorphism enables different objects to respond in a unique way to the same method call.
- Interfaces define methods that implementing classes must provide.

### 6. Exception Handling
- **Try-Catch Blocks**: Handling exceptions to prevent program crashes.
- **Custom Exceptions**: Creating and using custom exceptions.

#### Code Example
try { 
    int result = divide(10, 0); 
    System.out.println("Result: " + result); 
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
}

public static int divide(int a, int b) throws ArithmeticException {
    if (b == 0) {
        throw new ArithmeticException("Division by zero is not allowed");
    }
    return a / b; 
}

#### Notes
- Exception handling helps in managing errors and maintaining the normal flow of the application.
- Custom exceptions can be created to handle specific error conditions.

### Definitions Table

| Term               | Definition                                                                                   |
|--------------------|----------------------------------------------------------------------------------------------|
| **Primitive Types**| Basic data types such as `int`, `double`, `char`, `boolean`, `float`, `long`, `byte`, `short`.|
| **Reference Types**| Data types that store references to objects, such as `String`.                               |
| **Conditionals**   | Control structures that allow execution of code blocks based on boolean conditions (`if`, `else`, `switch`). |
| **Loops**          | Control structures that repeat a block of code multiple times (`for`, `while`).              |
| **Array**          | Fixed-size sequences of elements of the same type.                                           |
| **ArrayList**      | Resizable-array implementation of the List interface.                                        |
| **Method**         | A reusable block of code that performs a specific task. Methods are defined within classes and can be invoked to perform operations. |
| **Method Overloading**| Having multiple methods in the same scope with the same name but different parameters.       |
| **Recursive Method**| A method that calls itself in order to solve a problem.                                       |
| **Class**          | A blueprint for creating objects, defining their attributes (fields) and behaviors (methods). |
| **Object**         | An instance of a class, containing fields and methods defined by the class.                  |
| **Field**          | A variable declared inside a class to store data.                                            |
| **Property**       | Provides controlled access to fields.                                                        |
| **Encapsulation**  | Restricting access to certain details of an object and exposing only necessary parts through methods. |
| **Inheritance**    | Mechanism where one class (subclass) inherits the attributes and behaviors from another class (superclass). |
| **Polymorphism**   | Ability of different objects to respond in a unique way to the same method call.             |
| **Interface**      | Defines methods that a class must implement.                                                 |
| **Exception Handling**| Mechanism for handling runtime errors to maintain normal application flow.                |
| **Custom Exceptions**| User-defined exceptions to handle specific error conditions.                               |

This guide provides a comprehensive understanding of each component and process involved in the Java application, illustrating how user input is processed and displayed using Java and OOP principles.
