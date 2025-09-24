// Owen Lindsey
// 09/21/2024
// CST-201 Exercise 3 
// This work is my own

using System;
using System.Collections.Generic;


class Program
{
    /// <summary>
    /// Checks if two given words are anagrams of each other
    /// </summary>
    /// <param name="word1">The first word to compare</param>
    /// <param name="word2">The second word to compare</param>
    /// <returns>True if the words are anagrams, false otherwise</returns>
    static bool AreAnagrams(string word1, string word2)
    {
        // convert both words to Lowercase to check case-insensitve comparison
        word1 = word1.ToLower();
        word2 = word2.ToLower();

        // Check if the lengths are equal. If not they cannot be anagrams
        if (word1.Length != word2.Length)
        {
            return false;
        }

        // Create a dictionary to count character occurences 
        // The key is the character and the value is its count
        Dictionary<char, int> charCount = new Dictionary<char, int>();

        // Count occurences of each character in the first word
        foreach (char c in word1)
        {
            if (charCount.ContainsKey(c))
            {
                // if the character already exists in the dictonary increment its count
                charCount[c]++;
            }
            else
            {
                // if new character add it to the dictionary with a count of 1
                charCount[c] = 1;
            }
        }

        // check against the second word
        foreach (char c in word2)
        {
            if (!charCount.ContainsKey(c))
            {
                // if a character in word2 thats not in word1, theyre not anagrams 
                return false;
            }
            // Decrement the count for this character
            charCount[c]--;


            if (charCount[c] < 0)
            {
                // if return negative, word2 has more of this character than word1 
                return false;
            }
        }
        // if true, both words are compared and they are anagrams
        return true;
    }
    static void Main(string[] args)
    {

        // prompt user to enter the first word from the console
        Console.WriteLine("Enter the first word");
        string word1 = Console.ReadLine();

        // prompt user to enter the second word from the console
        Console.WriteLine("Enter the second word");
        string word2 = Console.ReadLine();

        // check if the words are anagrams from our AreAnagrams method
        if (AreAnagrams(word1, word2))
        {
            // the words are anagrams
            Console.WriteLine("True");
        }
        else
        {
            // theyre not anagrams
            Console.WriteLine("False");
        }
    }
}
