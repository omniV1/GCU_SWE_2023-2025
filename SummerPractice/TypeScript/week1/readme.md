# Week 1 TypeScript Practice Exercise

## Overview

This practice exercise is designed to help refresh my understanding of key TypeScript concepts. It includes tasks to work with data types, control structures, functions, and object-oriented programming (OOP). 

## Exercise Instructions

### Part 1: Data Types and Variables (10 minutes)

1. **Declare and Initialize Variables**:
   - Create a file named `part1_variables.ts`.
   - Declare variables of different data types and initialize them with values.
   - Use `number`, `string`, `boolean`, `array`, and `tuple`.

#### Code Example (`part1_variables.ts`)
``` TypeScript
(() => {
    let age: number = 30;
    let name: string = "John Doe";
    let isActive: boolean = true;
    let scores: number[] = [85, 90, 78];
    let user: [string, number] = ["Alice", 25];

    console.log(`Name: ${name}, Age: ${age}, Active: ${isActive}`);
    console.log(`Scores: ${scores}`);
    console.log(`User: ${user[0]}, ${user[1]}`);
})();
```

### Part 2: Control Structures (10 minutes)

2. **Write Conditional Statements**:
   - Create a file named `part2_control_structures.ts`.
   - Use `if`, `else if`, `else` to handle different conditions.
   - Use `switch` to handle multiple conditions.

#### Code Example (`part2_control_structures.ts`)
``` TypeScript
(() => {
    let age: number = 20;

    if (age > 18) {
        console.log("Adult");
    } else if (age > 12) {
        console.log("Teenager");
    } else {
        console.log("Child");
    }

    let day: number = new Date().getDay();
    switch (day) {
        case 0:
            console.log("Sunday");
            break;
        case 1:
            console.log("Monday");
            break;
        default:
            console.log("Another day");
    }
})();
```

### Part 3: Loops (10 minutes)

3. **Write Looping Structures**:
   - Create a file named `part3_loops.ts`.
   - Use `for`, `while`, `do-while`, `for-of`, and `for-in` loops to iterate over arrays and objects.

#### Code Example (`part3_loops.ts`)
``` TypeScript
(() => { 
    let scores: number[] = [85, 90, 78];

    for (let i = 0; i < scores.length; i++) {
        console.log(`Score ${i + 1}: ${scores[i]}`);
    }

    let count: number = 0;
    while (count < 3) {
        console.log(`Count: ${count}`);
        count++;
    }

    let languages: string[] = ["TypeScript", "JavaScript", "Python"];
    for (let lang of languages) {
        console.log(lang);
    }

    let person = { name: "John", age: 30 };
    for (let key in person) {
        console.log(`${key}: ${person[key as keyof typeof person]}`);
    }
})();
```
### Part 4: Functions (10 minutes)

4. **Create and Use Functions**:
   - Create a file named `part4_functions.ts`.
   - Define functions with different return types and parameters.
   - Use optional and default parameters.
   - Implement arrow functions.

#### Code Example (`part4_functions.ts`)
``` TypeScript
(() => {
    function greet(name: string, greeting: string = "Hello"): string {
        return `${greeting}, ${name}!`;
    }

    console.log(greet("Alice"));
    console.log(greet("Bob", "Hi"));

    let multiply = (a: number, b: number = 1): number => a * b;
    console.log(multiply(5, 2));
    console.log(multiply(5));
})();
```
### Part 5: Object-Oriented Programming (20 minutes)

5. **Create Classes and Objects**:
   - Create a file named `part5_oop.ts`.
   - Define a class with fields, properties, and methods.
   - Create instances of the class and call its methods.
   - Implement inheritance and polymorphism.
   - Define and implement an interface.

#### Code Example (`part5_oop.ts`)
``` TypeScript
(() => {
    class Animal {
        constructor(private name: string) {}

        public getName(): string {
            return this.name;
        }

        public speak(): void {
            console.log(`${this.name} makes a sound.`);
        }
    }

    class Dog extends Animal {
        constructor(name: string, private breed: string) {
            super(name);
        }

        public getBreed(): string {
            return this.breed;
        }

        public speak(): void {
            console.log(`${this.getName()} barks.`);
        }
    }

    interface Pet {
        play(): void;
    }

    class Cat extends Animal implements Pet {
        public speak(): void {
            console.log(`${this.getName()} meows.`);
        }

        public play(): void {
            console.log(`${this.getName()} is playing.`);
        }
    }

    let dog = new Dog("Rex", "Labrador");
    dog.speak();
    console.log(`Breed: ${dog.getBreed()}`);

    let cat = new Cat("Whiskers");
    cat.speak();
    cat.play();
})();
```
---

## Definitions Table

| Term                    | Definition                                                                                   |
|-------------------------|----------------------------------------------------------------------------------------------|
| **Primitive Types**     | Basic data types such as `number`, `string`, and `boolean`.                                   |
| **Reference Types**     | Data types that store references to objects, such as `any`, `array`, `tuple`, `enum`, `void`, `null`, `undefined`, and `never`. |
| **Conditionals**        | Control structures that allow execution of code blocks based on boolean conditions (`if`, `else if`, `else`, `switch`). |
| **Loops**               | Control structures that repeat a block of code multiple times (`for`, `while`, `do-while`, `for-of`, `for-in`). |
| **Function**            | A reusable block of code that performs a specific task. Functions are defined within classes and can be invoked to perform operations. |
| **Arrow Function**      | A shorter syntax for writing functions.                                                      |
| **Class**               | A blueprint for creating objects, defining their attributes (fields) and behaviors (methods). |
| **Object**              | An instance of a class, containing fields and methods defined by the class.                  |
| **Field**               | A variable declared inside a class to store data.                                            |
| **Property**            | Provides controlled access to fields.                                                        |
| **Method**              | Functions inside a class.                                                                    |
| **Encapsulation**       | Restricting access to certain details of an object and exposing only necessary parts through methods. |
| **Inheritance**         | A mechanism where one class (subclass) inherits the attributes and behaviors of another class (superclass). |
| **Polymorphism**        | The ability of different objects to respond in a unique way to the same method call.         |
| **Interface**           | Defines the shape of an object.                                                              |
| **Abstract Class**      | Defines common behaviors and properties that subclasses must implement.                      |
