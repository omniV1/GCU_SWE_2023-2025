using System;
using System.Collections.Generic;

namespace CSharpReview
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variables and Data types
            int number = 9;
            double decimalNumber = 26.5;
            char letter = 'A';
            string message = "HI IM OWEN";
            bool isTrue = true;

            // Output to the console
            Console.WriteLine("Integer: " + number);
            Console.WriteLine("Double: " + decimalNumber);
            Console.WriteLine("Character: " + letter);
            Console.WriteLine("String: " + message);
            Console.WriteLine("Boolean: " + isTrue);

            // Control structure
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

            // Prompt the user to enter a string
            Console.WriteLine("Enter a string: ");

            // Read the user's input from the console
            string userInput = Console.ReadLine();

            // Call the ExtractVowels method with the user's input and store the result in the 'vowels' variable
            List<(char vowel, int position)> vowels = ExtractVowels(userInput);

            // Print the extracted vowels along with their positions
            Console.WriteLine("Vowels in the input:");
            foreach (var item in vowels)
            {
                Console.WriteLine($"Vowel: {item.vowel}, Position: {item.position}");
            }

            // Call the custom method to print a message
            PrintMessage("This is a custom method!");

            // Create a Person object and call its method
            Person person = new Person
            {
                Name = "Owen Lindsey",
                Age = 26
            };
            person.Introduce();

            // Wait for the user to press a key before closing the console window
            Console.ReadKey();
        }

        // Custom method to print a message
        static void PrintMessage(string msg)
        {
            Console.WriteLine(msg);
        }

        // Method to extract vowels and their positions from the input string
        static List<(char vowel, int position)> ExtractVowels(string input)
        {
            // Define the vowels
            string vowels = "aeiouAEIOU";
            // Initialize a list to store the vowels and their positions
            List<(char vowel, int position)> result = new List<(char vowel, int position)>();

            // Iterate through each character in the input string
            for (int i = 0; i < input.Length; i++)
            {
                // Check if the character is a vowel
                if (vowels.Contains(input[i]))
                {
                    // Add the vowel and its position to the result list
                    result.Add((input[i], i));
                }
            }

            // Return the list containing the vowels and their positions
            return result;
        }
    }

    // Person class with properties and a method
    class Person
    {
        public string? Name { get; set; }
        public int Age { get; set; }

        public void Introduce()
        {
            Console.WriteLine("Hi, my name is " + Name + " and I am " + Age + " years old.");
        }
    }
}
