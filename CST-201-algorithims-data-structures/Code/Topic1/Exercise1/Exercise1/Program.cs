// This code is my own
// Owen Lindsey
// Professor Demland, David
// CST-201
// Exercise1

using System;
using System.Collections.Generic;

class Program
{
    // Method to find common elements in two sorted lists
    static List<int> FindCommonElements(List<int> list1, List<int> list2)
    {
        List<int> result = new List<int>(); // List to store common elements
        int a = 0; // Pointer for list1
        int b = 0; // Pointer for list2

        // Continue until we reach the end of either list
        while (a < list1.Count && b < list2.Count)
        {
            if (list1[a] == list2[b])
            {
                // If elements are equal, add to result and move both pointers
                result.Add(list1[a]);
                a++;
                b++;
            }
            else if (list1[a] < list2[b])
            {
                // If element in list1 is smaller, move list1 pointer
                a++;
            }
            else
            {
                // If element in list2 is smaller, move list2 pointer
                b++;
            }
        }

        return result; // Return the list of common elements
    }

    static void Main(string[] args)
    {
        // Initialize two sorted lists
        List<int> list1 = new List<int> { 2, 5, 5, 5 };
        List<int> list2 = new List<int> { 2, 2, 3, 5, 5, 7 };

        // Call the FindCommonElements method
        List<int> commonElements = FindCommonElements(list1, list2);

        // Print the common elements
        Console.WriteLine("Common elements: " + string.Join(", ", commonElements));
    }
}