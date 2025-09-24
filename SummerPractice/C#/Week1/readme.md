# Week 1 C# Refresher - Summary of Concepts

## Overview

This guide provides a summary of the key C# concepts covered in the first week of the refresher course. 

## Topics Covered

### 1. Data Types and Variables
- **Primitive Types:** `int`, `double`, `char`, `bool`
- **Reference Types:** `string`

#### Code Example
```csharp
int number = 9;
double decimalNumber = 26.5;
char letter = 'A';
string message = "HI IM OWEN";
bool isTrue = true;

Console.WriteLine("Integer: " + number);
Console.WriteLine("Double: " + decimalNumber);
Console.WriteLine("Character: " + letter);
Console.WriteLine("String: " + message);
Console.WriteLine("Boolean: " + isTrue);
```
Notes

- ***Primitive types*** store simple values.
- ***Reference types***store references to objects.

#### 2. Control Structures

- ***Conditionals:*** if, else if, else
- ***Loops:*** for, while

#### Code Example

``` csharp
if (number > 5)
{
    Console.WriteLine("Number is greater than 5");
}
else
{
    Console.WriteLine("Number is less than 5");
}

for (int i = 0; i < number; i++)
{
    Console.WriteLine("For Loop: " + i);
}

int count = 0;
while (count < 11)
{
    Console.WriteLine("While Loop: " + count);
    count++;
}
```
#### Notes
- ***Conditionals control the flow of execution based on boolean conditions.***
- 
- ***Loops repeat a block of code multiple times.***

#### 3. Methods
- ***Declaration and Invocation***
- 
- ***Return Types and Parameters***

#### Code Example

``` csharp
public static void PrintMessage(string msg)
{
    Console.WriteLine(msg);
}

PrintMessage("This is a custom method!");
```

#### Notes
- ***Methods*** encapsulate reusable code blocks.

#### 4. Object-Oriented Programming (OOP)

- ***Classes and Objects***

- ***Fields, Properties (Getters and Setters), and Methods
Encapsulation***

#### Code Example

```csharp

class Person
{
    public string? Name { get; set; }
    public int Age { get; set; }

    public void Introduce()
    {
        Console.WriteLine("Hi, my name is " + Name + " and I am " + Age + " years old.");
    }
}

Person person = new Person
{
    Name = "Owen Lindsey",
    Age = 26
};
person.Introduce();
```
#### Notes
- ***Classes:*** Blueprints for creating objects.
- ***Objects:*** Instances of classes.
- ***Fields:*** Variables inside a class.
- ***Properties:*** Provide controlled access to fields.
- ***Methods:*** Functions inside a class.
- ***Encapsulation:*** Restricting access to certain details and exposing only necessary parts.

#### 5. Additional Methods

- ***ExtractVowels Method:*** Extracts vowels and their positions from a string.

#### Code Example

```` csharp

static List<(char vowel, int position)> ExtractVowels(string input)
{
    string vowels = "aeiouAEIOU";
    List<(char vowel, int position)> result = new List<(char vowel, int position)>();

    for (int i = 0; i < input.Length; i++)
    {
        if (vowels.Contains(input[i]))
        {
            result.Add((input[i], i));
        }
    }

    return result;
}

Console.WriteLine("Enter a string: ");
string userInput = Console.ReadLine();
List<(char vowel, int position)> vowels = ExtractVowels(userInput);

Console.WriteLine("Vowels in the input:");
foreach (var item in vowels)
{
    Console.WriteLine($"Vowel: {item.vowel}, Position: {item.position}");
}
```


## Definitions Table

| Term                    | Definition                                                                                   |
|-------------------------|----------------------------------------------------------------------------------------------|
| **Primitive Types**     | Basic data types such as `int`, `double`, `char`, and `bool`.                                |
| **Reference Types**     | Data types that store references to objects, such as `string`.                               |
| **Conditionals**        | Control structures that allow execution of code blocks based on boolean conditions (`if`, `else if`, `else`). |
| **Loops**               | Control structures that repeat a block of code multiple times (`for`, `while`).              |
| **Method**              | A reusable block of code that performs a specific task. Methods are defined within classes and can be invoked to perform operations. |
| **Class**               | A blueprint for creating objects, defining their attributes (fields) and behaviors (methods). |
| **Object**              | An instance of a class, containing fields and methods defined by the class.                  |
| **Field**               | A variable declared inside a class to store data.                                            |
| **Property**            | Provides controlled access to fields.                                                        |
| **Encapsulation**       | Restricting access to certain details of an object and exposing only necessa