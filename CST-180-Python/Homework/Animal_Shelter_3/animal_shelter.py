# Owen Lindsey
# CST-180
# 11/09/2025
# animal_shelter.py

"""Animal shelter simulator classes matching the project pseudocode."""

from __future__ import annotations

from typing import Dict, List, Optional, Union


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
        return (
            "Kennel(empty)" if self.animal is None else f"Kennel Animal: {self.animal}"
        )


class Shelter:
    """Animal shelter that manages kennels, capacity, and a waitlist."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Shelter capacity must be positive.")

        self.capacity = capacity
        self.kennels: List[Kennel] = []
        self.waitlist: Dict[str, List[str]] = {}

    @staticmethod
    def _normalize_type(animal_type: str) -> str:
        """Normalize animal type names for comparisons and storage."""
        return animal_type.strip().lower()

    def add_animal(self, animal: Animal) -> bool:
        """Add an animal to an empty kennel or create a new kennel if allowed."""
        for kennel in self.kennels:
            if kennel.animal is None:
                kennel.animal = animal
                return True

        if len(self.kennels) < self.capacity:
            self.kennels.append(Kennel(animal))
            return True

        return False

    def adopt_animal(
        self, animal_type: str, adopter_name: Optional[str] = None
    ) -> Optional[Animal]:
        """Adopt the first animal of the requested type, or track a waitlist."""
        normalized_type = self._normalize_type(animal_type)

        for kennel in self.kennels:
            if kennel.animal and kennel.animal.__class__.__name__.lower() == normalized_type:
                adopted = kennel.animal
                kennel.animal = None
                return adopted

        if adopter_name:
            self.waitlist.setdefault(normalized_type, []).append(adopter_name)

        return None

    def get_waitlist(self, animal_type: str) -> List[str]:
        """Return the waitlist for a given animal type."""
        return list(self.waitlist.get(self._normalize_type(animal_type), []))

    def has_empty_kennel(self) -> bool:
        """Indicate whether any kennel is empty."""
        return any(kennel.animal is None for kennel in self.kennels)

    def total_animals(self) -> int:
        """Count how many animals currently reside in the shelter."""
        return sum(1 for kennel in self.kennels if kennel.animal is not None)

    def __str__(self) -> str:
        """Display the shelter status summary."""
        kennel_descriptions = ", ".join(str(kennel) for kennel in self.kennels)
        kennel_output = kennel_descriptions if kennel_descriptions else "No kennels yet"
        return (
            f"Shelter(capacity={self.capacity}, "
            f"kennels={len(self.kennels)}, animals={self.total_animals()}, {kennel_output})"
        )


if __name__ == "__main__":
    # Sample animals that will move through the shelter.
    dog1 = Dog("Buddy", 3, "Labrador")
    cat1 = Cat("Mittens", 2, "Tabby")
    bird1 = Bird("Sky", 1, 0.35)

    # Create a shelter that can expand up to three kennels.
    shelter = Shelter(capacity=3)

    # Add dog and cat to demonstrate kennel reuse.
    shelter.add_animal(dog1)
    shelter.add_animal(cat1)
    print(shelter)

    # Adopt a cat, which frees a kennel for another incoming animal.
    adopted_cat = shelter.adopt_animal("Cat")
    print(f"Adopted: {adopted_cat}")
    print(f"Empty kennel available? {shelter.has_empty_kennel()}")

    # Adding the bird now fills the empty kennel instead of creating a new one.
    shelter.add_animal(bird1)
    print(shelter)

    # Attempt to adopt a rabbit, which we do not currently have; add adopter to waitlist.
    rabbit_request = shelter.adopt_animal("Rabbit", adopter_name="Alice")
    print(f"Rabbit adoption result: {rabbit_request}")
    print(f"Rabbit waitlist: {shelter.get_waitlist('Rabbit')}")
