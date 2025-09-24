markdown
Copy code
# Week 1 Java Refresher - Summary of Concepts

## Overview

This guide provides a summary of the key Java concepts covered in the first week of the refresher course.

## Topics Covered

### 1. Data Types and Variables
- ***Primitive Types:*** `int`, `float`, `double`, `char`, `boolean`
- ***Reference Types:*** `String`

#### Code Example
```java
int number = 10;
double decimalNumber = 20.5;
char letter = 'A';
String message = "Hello, World!";
boolean isTrue = true;

System.out.println("Integer: " + number);
System.out.println("Double: " + decimalNumber);
System.out.println("Character: " + letter);
System.out.println("String: " + message);
System.out.println("Boolean: " + isTrue);
```
### Notes
- ***Primitive*** types store simple values.
- ***Reference*** types store addresses of objects.
  
### 2. Control Structures 
***Conditionals:*** if, else if, else, switch

***Loops:*** for, while, do-while, for-each

#### Code Example

```java
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
```
### Notes

- ***Conditionals*** control the flow of execution based on boolean conditions.

- ***Loops*** repeat a block of code multiple times.

### 3. Methods

- ***Declaration and Invocation***
  
- ***Return Types and Parameters***
  
- ***Method Overloading***

Code Example
```java

public static void printMessage(String msg) {
    System.out.println(msg);
}

printMessage("This is a custom method!");
```
### Notes

- Methods encapsulate reusable code blocks.
  
- Overloading allows methods to have the same name but different parameters.
### 4. Object-Oriented Programming (OOP)

- ***Classes and Objects***

- ***Fields, Properties (Getters and Setters), and Methods***

- ***Inheritance and Polymorphism***

- ***Encapsulation and Abstraction***
  
### Code Example

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
        System.out.println("Hi, my name is " + name + " and I am " + age + " years old.");
    }
}

Person person = new Person();
person.setName("John Doe");
person.setAge(30);
person.introduce();
```
#### Notes
- ***Classes:*** Blueprints for creating objects.

- ***Objects:*** Instances of classes.

- ***Fields:*** Variables inside a class.

- ***Methods:*** Functions inside a class.

- ***Encapsulation:*** Restricting access to certain details and exposing only necessary parts.

- ***Inheritance:*** Mechanism for a new class to inherit properties and behavior from an existing class.

- ***Polymorphism:*** Ability to process objects differently based on their data type or class.

# Definitions Table

| Term                    | Definition                                                                                   |
|-------------------------|----------------------------------------------------------------------------------------------|
| **Primitive Types**     | Basic data types such as `int`, `float`, `double`, `char`, and `boolean`.                    |
| **Reference Types**     | Data types that store references to objects, such as `String`.                               |
| **Conditionals**        | Control structures that allow execution of code blocks based on boolean conditions (`if`, `else if`, `else`, `switch`). |
| **Loops**               | Control structures that repeat a block of code multiple times (`for`, `while`, `do-while`, `for-each`). |
| **Method**              | A reusable block of code that performs a specific task. Methods are defined within classes and can be invoked to perform operations. |
| **Method Overloading**  | Defining multiple methods with the same name but different parameters within a class.        |
| **Class**               | A blueprint for creating objects, defining their attributes (fields) and behaviors (methods). |
| **Object**              | An instance of a class, containing fields and methods defined by the class.                  |
| **Field**               | A variable declared inside a class to store data.                                            |
| **Encapsulation**       | Restricting access to certain details of an object and exposing only necessary parts through methods. |
| **Inheritance**         | A mechanism where one class (subclass) inherits the attributes and behaviors of another class (superclass). |
| **Polymorphism**        | The ability of different objects to respond in a unique way to the same method call.         |
