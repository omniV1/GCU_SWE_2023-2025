# Owen Lindsey
# CST-180
# 10/26/2025
# test_animal_shelter.py

"""Unit tests for the animal shelter classes.

This test suite verifies all functionality of the Dog, Cat, Bird, and Kennel classes.
Run with: python -m unittest test_animal_shelter.py -v
"""

import unittest
from animal_shelter import Dog, Cat, Bird, Kennel


# ====================================================================================
# DOG CLASS TESTS
# ====================================================================================
# These tests verify that the Dog class correctly stores name, age, and breed,
# handles both default and custom parameters, and formats output properly.
# ====================================================================================

class TestDog(unittest.TestCase):
    """Test cases for the Dog class."""

    def test_dog_constructor_with_parameters(self):
        """Test Dog constructor with all parameters."""
        # PURPOSE: Verify that Dog stores all attributes correctly when provided
        # Create a dog with specific name, age, and breed
        dog = Dog("Buddy", 3, "Labrador")

        # VERIFY: Check each attribute was stored correctly
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.age, 3)
        self.assertEqual(dog.breed, "Labrador")

    def test_dog_constructor_default(self):
        """Test Dog constructor with default parameters."""
        # PURPOSE: Verify that Dog can be created with no parameters (uses defaults)
        # This tests the overloaded constructor requirement
        dog = Dog()

        # VERIFY: All attributes should have default values
        self.assertEqual(dog.name, "")
        self.assertEqual(dog.age, 0)
        self.assertEqual(dog.breed, "")

    def test_dog_str(self):
        """Test Dog __str__ method."""
        # PURPOSE: Verify the Dog's string representation matches required format
        # This tests the overloaded __str__ requirement
        dog = Dog("Charlie", 7, "Golden Retriever")
        expected = "Dog: Name: Charlie, Age: 7, Breed: Golden Retriever"

        # VERIFY: String output matches the required format exactly
        self.assertEqual(str(dog), expected)

    def test_dog_partial_parameters(self):
        """Test Dog constructor with partial parameters."""
        # PURPOSE: Verify Dog works when only some parameters are provided
        # Tests flexibility of the overloaded constructor
        dog = Dog("Rex", 5)

        # VERIFY: Provided values are stored, missing values use defaults
        self.assertEqual(dog.name, "Rex")
        self.assertEqual(dog.age, 5)
        self.assertEqual(dog.breed, "")  # Should use default empty string


# ====================================================================================
# CAT CLASS TESTS
# ====================================================================================
# These tests verify that the Cat class correctly stores name, age, and fur color,
# handles both default and custom parameters, and formats output properly.
# ====================================================================================

class TestCat(unittest.TestCase):
    """Test cases for the Cat class."""

    def test_cat_constructor_with_parameters(self):
        """Test Cat constructor with all parameters."""
        # PURPOSE: Verify that Cat stores all attributes correctly when provided
        # Create a cat with specific name, age, and fur color
        cat = Cat("Mittens", 2, "Tabby")

        # VERIFY: Check each attribute was stored correctly
        self.assertEqual(cat.name, "Mittens")
        self.assertEqual(cat.age, 2)
        self.assertEqual(cat.fur_color, "Tabby")

    def test_cat_constructor_default(self):
        """Test Cat constructor with default parameters."""
        # PURPOSE: Verify that Cat can be created with no parameters (uses defaults)
        # This tests the overloaded constructor requirement
        cat = Cat()

        # VERIFY: All attributes should have default values
        self.assertEqual(cat.name, "")
        self.assertEqual(cat.age, 0)
        self.assertEqual(cat.fur_color, "")

    def test_cat_str(self):
        """Test Cat __str__ method."""
        # PURPOSE: Verify the Cat's string representation matches required format
        # This tests the overloaded __str__ requirement
        cat = Cat("Luna", 5, "Orange Tabby")
        expected = "Cat: Name: Luna, Age: 5, Fur Color: Orange Tabby"

        # VERIFY: String output matches the required format exactly
        self.assertEqual(str(cat), expected)

    def test_cat_partial_parameters(self):
        """Test Cat constructor with partial parameters."""
        # PURPOSE: Verify Cat works when only some parameters are provided
        # Tests flexibility of the overloaded constructor
        cat = Cat("Whiskers", 3)

        # VERIFY: Provided values are stored, missing values use defaults
        self.assertEqual(cat.name, "Whiskers")
        self.assertEqual(cat.age, 3)
        self.assertEqual(cat.fur_color, "")  # Should use default empty string


# ====================================================================================
# BIRD CLASS TESTS
# ====================================================================================
# These tests verify that the Bird class correctly stores name, age, and wingspan,
# handles both default and custom parameters, and formats output properly.
# Note: Wingspan is a float value representing the bird's wingspan measurement.
# ====================================================================================

class TestBird(unittest.TestCase):
    """Test cases for the Bird class."""

    def test_bird_constructor_with_parameters(self):
        """Test Bird constructor with all parameters."""
        # PURPOSE: Verify that Bird stores all attributes correctly when provided
        # Create a bird with specific name, age, and wingspan (float)
        bird = Bird("Sky", 1, 0.35)

        # VERIFY: Check each attribute was stored correctly
        self.assertEqual(bird.name, "Sky")
        self.assertEqual(bird.age, 1)
        self.assertEqual(bird.wingspan, 0.35)

    def test_bird_constructor_default(self):
        """Test Bird constructor with default parameters."""
        # PURPOSE: Verify that Bird can be created with no parameters (uses defaults)
        # This tests the overloaded constructor requirement
        bird = Bird()

        # VERIFY: All attributes should have default values
        self.assertEqual(bird.name, "")
        self.assertEqual(bird.age, 0)
        self.assertEqual(bird.wingspan, 0.0)

    def test_bird_str(self):
        """Test Bird __str__ method."""
        # PURPOSE: Verify the Bird's string representation matches required format
        # This tests the overloaded __str__ requirement
        bird = Bird("Tweety", 2, 0.25)
        expected = "Bird: Name: Tweety, Age: 2, Wingspan: 0.25"

        # VERIFY: String output matches the required format exactly
        self.assertEqual(str(bird), expected)

    def test_bird_partial_parameters(self):
        """Test Bird constructor with partial parameters."""
        # PURPOSE: Verify Bird works when only some parameters are provided
        # Tests flexibility of the overloaded constructor
        bird = Bird("Eagle", 4)

        # VERIFY: Provided values are stored, missing values use defaults
        self.assertEqual(bird.name, "Eagle")
        self.assertEqual(bird.age, 4)
        self.assertEqual(bird.wingspan, 0.0)  # Should use default 0.0


# ====================================================================================
# KENNEL CLASS TESTS
# ====================================================================================
# These tests verify the Kennel class correctly manages animal storage.
# KEY REQUIREMENT: A Kennel can only hold ONE animal at a time.
# When a new animal is added, it REPLACES the previous animal.
# Tests also verify GetAnimalType() method and proper string formatting.
# ====================================================================================

class TestKennel(unittest.TestCase):
    """Test cases for the Kennel class."""

    # ================================================================================
    # CONSTRUCTOR TESTS - Verify kennel can be created empty or with an animal
    # ================================================================================

    def test_kennel_constructor_empty(self):
        """Test Kennel constructor with no parameters."""
        # PURPOSE: Verify Kennel can be created empty (default state)
        kennel = Kennel()

        # VERIFY: Kennel should have no animal initially
        self.assertIsNone(kennel.animal)

    def test_kennel_constructor_with_dog(self):
        """Test Kennel constructor with a Dog."""
        # PURPOSE: Verify Kennel can be initialized with a Dog
        dog = Dog("Buddy", 3, "Labrador")
        kennel = Kennel(dog)

        # VERIFY: Kennel should contain the provided dog
        self.assertEqual(kennel.animal, dog)

    def test_kennel_constructor_with_cat(self):
        """Test Kennel constructor with a Cat."""
        # PURPOSE: Verify Kennel can be initialized with a Cat
        cat = Cat("Mittens", 2, "Tabby")
        kennel = Kennel(cat)

        # VERIFY: Kennel should contain the provided cat
        self.assertEqual(kennel.animal, cat)

    def test_kennel_constructor_with_bird(self):
        """Test Kennel constructor with a Bird."""
        # PURPOSE: Verify Kennel can be initialized with a Bird
        bird = Bird("Sky", 1, 0.35)
        kennel = Kennel(bird)

        # VERIFY: Kennel should contain the provided bird
        self.assertEqual(kennel.animal, bird)

    # ================================================================================
    # ADDING ANIMALS TESTS - Verify animals can be added to empty kennels
    # ================================================================================

    def test_kennel_add_dog(self):
        """Test adding a Dog to an empty Kennel."""
        # PURPOSE: Verify a Dog can be added to an empty Kennel
        kennel = Kennel()
        dog = Dog("Rex", 5, "Beagle")
        kennel.animal = dog

        # VERIFY: Kennel should now contain the dog
        self.assertEqual(kennel.animal, dog)

    def test_kennel_add_cat(self):
        """Test adding a Cat to an empty Kennel."""
        # PURPOSE: Verify a Cat can be added to an empty Kennel
        kennel = Kennel()
        cat = Cat("Whiskers", 3, "Black")
        kennel.animal = cat

        # VERIFY: Kennel should now contain the cat
        self.assertEqual(kennel.animal, cat)

    def test_kennel_add_bird(self):
        """Test adding a Bird to an empty Kennel."""
        # PURPOSE: Verify a Bird can be added to an empty Kennel
        kennel = Kennel()
        bird = Bird("Tweety", 2, 0.25)
        kennel.animal = bird

        # VERIFY: Kennel should now contain the bird
        self.assertEqual(kennel.animal, bird)

    # ================================================================================
    # CRITICAL TEST - REQUIREMENT #6: Cannot add more than one animal to the kennel
    # ================================================================================

    def test_kennel_replace_animal(self):
        """Test replacing an animal in the Kennel (only one animal at a time)."""
        # PURPOSE: Verify that a kennel can only hold ONE animal at a time
        # This tests the CRITICAL requirement: when you add a new animal,
        # it REPLACES the old one (kennel doesn't hold multiple animals)
        kennel = Kennel()
        dog = Dog("Buddy", 3, "Labrador")
        cat = Cat("Mittens", 2, "Tabby")

        # STEP 1: Add dog first
        kennel.animal = dog
        self.assertEqual(kennel.animal, dog)

        # STEP 2: Replace with cat (dog is no longer in kennel)
        kennel.animal = cat
        self.assertEqual(kennel.animal, cat)
        # VERIFY: The kennel does NOT contain the dog anymore
        self.assertNotEqual(kennel.animal, dog)

    # ================================================================================
    # GetAnimalType() METHOD TESTS - Verify the method returns correct animal type
    # ================================================================================

    def test_kennel_get_animal_type_empty(self):
        """Test GetAnimalType method with empty kennel."""
        # PURPOSE: Verify GetAnimalType returns "None" when kennel is empty
        kennel = Kennel()

        # VERIFY: Should return "None" for empty kennel
        self.assertEqual(kennel.GetAnimalType(), "None")

    def test_kennel_get_animal_type_dog(self):
        """Test GetAnimalType method with a Dog."""
        # PURPOSE: Verify GetAnimalType correctly identifies a Dog
        # This uses the __class__.__name__ attribute to get "Dog"
        dog = Dog("Buddy", 3, "Labrador")
        kennel = Kennel(dog)

        # VERIFY: Should return "Dog"
        self.assertEqual(kennel.GetAnimalType(), "Dog")

    def test_kennel_get_animal_type_cat(self):
        """Test GetAnimalType method with a Cat."""
        # PURPOSE: Verify GetAnimalType correctly identifies a Cat
        cat = Cat("Mittens", 2, "Tabby")
        kennel = Kennel(cat)

        # VERIFY: Should return "Cat"
        self.assertEqual(kennel.GetAnimalType(), "Cat")

    def test_kennel_get_animal_type_bird(self):
        """Test GetAnimalType method with a Bird."""
        # PURPOSE: Verify GetAnimalType correctly identifies a Bird
        bird = Bird("Sky", 1, 0.35)
        kennel = Kennel(bird)

        # VERIFY: Should return "Bird"
        self.assertEqual(kennel.GetAnimalType(), "Bird")

    # ================================================================================
    # __str__ METHOD TESTS - Verify proper output formatting (matches requirements)
    # ================================================================================

    def test_kennel_str_empty(self):
        """Test Kennel __str__ method when empty."""
        # PURPOSE: Verify empty kennel displays correctly
        kennel = Kennel()

        # VERIFY: Empty kennel should display as "Kennel(empty)"
        self.assertEqual(str(kennel), "Kennel(empty)")

    def test_kennel_str_with_dog(self):
        """Test Kennel __str__ method with a Dog."""
        # PURPOSE: Verify kennel with dog displays in required format
        # Format: "Kennel Animal: Dog: Name: X, Age: Y, Breed: Z"
        dog = Dog("Charlie", 7, "Golden Retriever")
        kennel = Kennel(dog)
        expected = "Kennel Animal: Dog: Name: Charlie, Age: 7, Breed: Golden Retriever"

        # VERIFY: Output matches the exact required format
        self.assertEqual(str(kennel), expected)

    def test_kennel_str_with_cat(self):
        """Test Kennel __str__ method with a Cat."""
        # PURPOSE: Verify kennel with cat displays in required format
        # Format: "Kennel Animal: Cat: Name: X, Age: Y, Fur Color: Z"
        cat = Cat("Luna", 5, "Orange Tabby")
        kennel = Kennel(cat)
        expected = "Kennel Animal: Cat: Name: Luna, Age: 5, Fur Color: Orange Tabby"

        # VERIFY: Output matches the exact required format
        self.assertEqual(str(kennel), expected)

    def test_kennel_str_with_bird(self):
        """Test Kennel __str__ method with a Bird."""
        # PURPOSE: Verify kennel with bird displays in required format
        # Format: "Kennel Animal: Bird: Name: X, Age: Y, Wingspan: Z"
        bird = Bird("Tweety", 2, 0.25)
        kennel = Kennel(bird)
        expected = "Kennel Animal: Bird: Name: Tweety, Age: 2, Wingspan: 0.25"

        # VERIFY: Output matches the exact required format
        self.assertEqual(str(kennel), expected)


# ====================================================================================
# TEST EXECUTION
# ====================================================================================
# Run this file to execute all 28 unit tests
# Command: python -m unittest test_animal_shelter.py -v
# The -v flag provides verbose output showing each test as it runs
#
# TEST SUMMARY:
# - 4 tests for Dog class (constructor, default, str, partial params)
# - 4 tests for Cat class (constructor, default, str, partial params)
# - 4 tests for Bird class (constructor, default, str, partial params)
# - 16 tests for Kennel class (constructors, adding animals, replacing animals,
#   GetAnimalType method, and str method with all animal types)
#
# Total: 28 tests covering all project requirements
# ====================================================================================

if __name__ == "__main__":
    # Run all test cases
    unittest.main()
