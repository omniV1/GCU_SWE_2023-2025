# Owen Lindsey
# CST-180
# 10/26i/2025
# animal_shelter.py

"""Animal shelter simulator classes matching the project pseudocode."""

from __future__ import annotations

from typing import Optional, Union


# DEFINE class Animal (Base Class)
# Represents a generic animal with common attributes: name and age.
class Animal:
    # FUNCTION __init__(self, name="", age=0)
    # Initialize the base animal with common attributes.
    def __init__(self, name: str = "", age: int = 0) -> None:
        # SET self.name EQUALS name
        # Store the provided name for this animal.
        self.name = name
        # SET self.age EQUALS age
        # Store the provided age for this animal.
        self.age = age

    # FUNCTION __str__(self)
    # Provide a readable description for the base animal instance.
    def __str__(self) -> str:
        # RETURN formatted string describing the animal
        # Format the animal's common details for display.
        return f"Name: {self.name}, Age: {self.age}"


# DEFINE class Dog (inherits from Animal)
# Represents a dog with name, age, and breed details.
class Dog(Animal):
    # FUNCTION __init__(self, name="", age=0, breed="")
    # Initialize the dog; defaults allow creation with no immediate data.
    def __init__(self, name: str = "", age: int = 0, breed: str = "") -> None:
        # CALL super().__init__(name, age)
        # Initialize the base Animal attributes using the parent constructor.
        super().__init__(name, age)
        # SET self.breed EQUALS breed
        # Store the provided breed for this dog.
        self.breed = breed

    # FUNCTION __str__(self)
    # Provide a readable description for the dog instance.
    def __str__(self) -> str:
        # RETURN formatted string describing the dog
        # Format the dog's details for display.
        return f"Dog: Name: {self.name}, Age: {self.age}, Breed: {self.breed}"


# DEFINE class Cat (inherits from Animal)
# Represents a cat with name, age, and fur color.
class Cat(Animal):
    # FUNCTION __init__(self, name="", age=0, fur_color="")
    # Initialize the cat with optional attributes for quick testing.
    def __init__(self, name: str = "", age: int = 0, fur_color: str = "") -> None:
        # CALL super().__init__(name, age)
        # Initialize the base Animal attributes using the parent constructor.
        super().__init__(name, age)
        # SET self.fur_color EQUALS fur_color
        # Store the fur color for this cat.
        self.fur_color = fur_color

    # FUNCTION __str__(self)
    # Provide a readable description for the cat instance.
    def __str__(self) -> str:
        # RETURN formatted string describing the cat
        # Format the cat's details for display.
        return f"Cat: Name: {self.name}, Age: {self.age}, Fur Color: {self.fur_color}"


# DEFINE class Bird (inherits from Animal)
# Represents a bird with name, age, and wingspan.
class Bird(Animal):
    # FUNCTION __init__(self, name="", age=0, wingspan=0.0)
    # Initialize the bird, tracking wingspan for variety in data.
    def __init__(self, name: str = "", age: int = 0, wingspan: float = 0.0) -> None:
        # CALL super().__init__(name, age)
        # Initialize the base Animal attributes using the parent constructor.
        super().__init__(name, age)
        # SET self.wingspan EQUALS wingspan
        # Store the wingspan measurement for this bird.
        self.wingspan = wingspan

    # FUNCTION __str__(self)
    # Provide a readable description for the bird instance.
    def __str__(self) -> str:
        # RETURN formatted string describing the bird
        # Format the bird's details for display.
        return f"Bird: Name: {self.name}, Age: {self.age}, Wingspan: {self.wingspan}"


# DEFINE Animal AS Union[Dog, Cat, Bird]
# Provide a convenient alias for the animal types supported by the kennel.
Animal = Union[Dog, Cat, Bird]


# DEFINE class Kennel
# Container that holds exactly one animal at a time.
class Kennel:
    # FUNCTION __init__(self, animal=None)
    # Create a kennel, optionally seeding it with an animal.
    def __init__(self, animal: Optional[Animal] = None) -> None:
        # SET self.animal EQUALS animal
        # Track the current animal inside the kennel.
        self.animal = animal

    # FUNCTION GetAnimalType(self)
    # Report the type name for the current animal or show empty state.
    def GetAnimalType(self) -> str:
        # IF self.animal IS None THEN RETURN "None" ELSE RETURN class name
        # Provide the class name string for whichever animal is stored.
        return "None" if self.animal is None else self.animal.__class__.__name__

    # FUNCTION __str__(self)
    # Provide a readable summary for the kennel and its occupant.
    def __str__(self) -> str:
        # IF self.animal IS None THEN RETURN "Kennel(empty)" ELSE RETURN formatted string
        # Format the kennel representation based on whether it contains an animal.
        return "Kennel(empty)" if self.animal is None else f"Kennel Animal: {self.animal}"


if __name__ == "__main__":
    # DEFINE dog1 AS Dog("Buddy", 3, "Labrador")
    # Create a sample dog instance for demonstration.
    dog1 = Dog("Buddy", 3, "Labrador")
    # DEFINE cat1 AS Cat("Mittens", 2, "Tabby")
    # Create a sample cat instance for demonstration.
    cat1 = Cat("Mittens", 2, "Tabby")
    # DEFINE bird1 AS Bird("Sky", 1, 0.35)
    # Create a sample bird instance for demonstration.
    bird1 = Bird("Sky", 1, 0.35)

    # DEFINE kennel AS Kennel()
    # Initialize an empty kennel ready to store animals.
    kennel = Kennel()

    # SET kennel.animal EQUALS dog1
    # Place the dog in the kennel and print status.
    kennel.animal = dog1
    # PRINT(kennel)
    # Show the kennel with the dog inside.
    print(kennel)
    # PRINT(kennel.GetAnimalType())
    # Show the type of animal held in the kennel.
    print(kennel.GetAnimalType())

    # SET kennel.animal EQUALS cat1
    # Replace the kennel occupant with the cat and print status.
    kennel.animal = cat1
    # PRINT(kennel)
    # Show the kennel with the cat inside.
    print(kennel)
    # PRINT(kennel.GetAnimalType())
    # Show the type of animal held in the kennel.
    print(kennel.GetAnimalType())

    # SET kennel.animal EQUALS bird1
    # Replace the kennel occupant with the bird and print status.
    kennel.animal = bird1
    # PRINT(kennel)
    # Show the kennel with the bird inside.
    print(kennel)
    # PRINT(kennel.GetAnimalType())
    # Show the type of animal held in the kennel.
    print(kennel.GetAnimalType())
