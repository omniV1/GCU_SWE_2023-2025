<div style="text-align: center; padding-top: 100px;">

# Animal Shelter Simulator – Project Design Document

<br>
<br>

**Owen Lindsey**
**Professor David Parker**
**CST-180: Python Programming 1**
**Grand Canyon University**
**November 6, 2025**

<br>
<br>
<br>

</div>
## Important Links
#### [Video: ](https://youtu.be/Y9pTq0iNVK4)
#### [src code: ]()
#### [Video: ]()
<div style="page-break-after: always;"></div>

## Summary

This project establishes an object-oriented design for an animal shelter simulator utilizing **inheritance principles**. The architecture features a base `Animal` class with common attributes (name, age) and behaviors, from which three specialized classes inherit: `Dog`, `Cat`, and `Bird`. Each specialized class extends the base functionality with unique attributes—breed, fur color, and wingspan respectively.

The design includes a `Kennel` class that demonstrates composition by containing exactly one `Animal` instance at a time. Type identification is achieved through Python's `__class__.__name__` attribute, enabling dynamic animal type reporting.

<div style="page-break-after: always;"></div>

## System Architecture

### Data Flow Model

The system follows a three-stage data flow pattern:

**Input Stage**
The system accepts animal details through constructor parameters. Each animal type requires specific attributes as detailed in the table below:

| Animal Type | Required Attributes |
|-------------|-------------------|
| Dog | Name (string), Age (integer), Breed (string) |
| Cat | Name (string), Age (integer), Fur Color (string) |
| Bird | Name (string), Age (integer), Wingspan (float) |

Additionally, the system accepts a selection indicating which animal instance to place within a `Kennel` container.

**Processing Stage**
Object construction utilizes overloaded constructors supporting both no-argument (default) and full-argument initialization patterns. The base `Animal` class handles common attributes through inheritance, while specialized classes manage type-specific data. Each class implements a `__str__()` method for human-readable output. The `Kennel` class employs composition to contain exactly one animal at a time, with dynamic type identification through Python's reflection capabilities (`__class__.__name__`).

**Output Stage**
The system generates formatted string representations of animal objects and kennel status. The `Kennel.GetAnimalType()` method returns the class name of the contained animal, providing type information without explicit type checking.

<div style="page-break-after: always;"></div>

## Class Design

### UML Class Diagram

![[Pasted image 20251106105418.png]]

### Architectural Relationships

The class structure demonstrates two fundamental object-oriented design patterns:

**Inheritance Hierarchy**
The `Animal` base class serves as the foundation, encapsulating common attributes (name, age) and providing a standard `__str__()` implementation. Three specialized classes—`Dog`, `Cat`, and `Bird`—extend this base, each contributing unique domain-specific attributes: breed, fur color, and wingspan respectively.

**Composition Pattern**
The `Kennel` class implements a has-a relationship with `Animal`, maintaining a single animal reference at any given time. This design allows the kennel to work polymorphically with any animal subtype while providing runtime type identification through the `GetAnimalType()` method.

<div style="page-break-after: always;"></div>

## Implementation

### Python Class Definitions

```python
# Base class containing common attributes
class Animal:
    def __init__(self, name: str = "", age: int = 0) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

# Dog inherits from Animal and adds breed
class Dog(Animal):
    def __init__(self, name: str = "", age: int = 0, breed: str = "") -> None:
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed

    def __str__(self) -> str:
        return f"Dog: Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

# Cat inherits from Animal and adds fur_color
class Cat(Animal):
    def __init__(self, name: str = "", age: int = 0, fur_color: str = "") -> None:
        super().__init__(name, age)  # Call parent constructor
        self.fur_color = fur_color

    def __str__(self) -> str:
        return f"Cat: Name: {self.name}, Age: {self.age}, Fur Color: {self.fur_color}"

# Bird inherits from Animal and adds wingspan
class Bird(Animal):
    def __init__(self, name: str = "", age: int = 0, wingspan: float = 0.0) -> None:
        super().__init__(name, age)  # Call parent constructor
        self.wingspan = wingspan

    def __str__(self) -> str:
        return f"Bird: Name: {self.name}, Age: {self.age}, Wingspan: {self.wingspan}"

# Kennel can contain any Animal (or subclass)
class Kennel:
    def __init__(self, animal: Animal | None = None) -> None:
        self.animal = animal

    def GetAnimalType(self) -> str:
        return "None" if self.animal is None else self.animal.__class__.__name__

    def __str__(self) -> str:
        return "Kennel(empty)" if self.animal is None else f"Kennel Animal: {self.animal}"
```

<div style="page-break-after: always;"></div>

## Testing and Validation

### Test Data Set

The following test instances demonstrate the system's capability to handle diverse animal types:

| Instance | Type | Name | Age | Special Attribute | Value |
|----------|------|------|-----|-------------------|-------|
| dog1 | Dog | Buddy | 3 | Breed | Labrador |
| cat1 | Cat | Mittens | 2 | Fur Color | Tabby |
| bird1 | Bird | Sky | 1 | Wingspan | 0.35m |

### Expected Output

When executed with the test data set, the system produces the following output demonstrating proper inheritance, composition, and type identification:

```
Kennel Animal: Dog: Name: Buddy, Age: 3, Breed: Labrador
Dog

Kennel Animal: Cat: Name: Mittens, Age: 2, Fur Color: Tabby
Cat

Kennel Animal: Bird: Name: Sky, Age: 1, Wingspan: 0.35
Bird
```

The output validates that each animal object correctly inherits base attributes while maintaining specialized characteristics, and the kennel successfully reports the contained animal type.

<div style="page-break-after: always;"></div>

## References

Dalbey, J. (2003). *Pseudocode Standard*. California Polytechnic State University. Retrieved from https://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html
