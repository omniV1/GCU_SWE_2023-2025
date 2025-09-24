// Owen Lindsey

// 9/21/2024

// CST-201 Exercise 3 1.4.1

// This work is my own 

using System;

class Program
{
    /// <summary>
    /// Deletes the ith element from an array in O(1) time
    /// </summary>
    /// <typeparam name="T">The type of elements in the array</typeparam>
    /// <param name="arr">The input array</param>
    /// <param name="i">The index of the element to delete (1-based)</param>
    /// <returns>A new array with the ith element removed</returns>
    /// <exception cref="ArgumentOutOfRangeException">Thrown when i is out of the valid range</exception>
    static T[] DeleteIthElement<T>(T[] arr, int i)
    {
        // Check if the provided index is within the valid range
        if (i < 1 || i > arr.Length)
        {
            throw new ArgumentOutOfRangeException(nameof(i), "Index out of range");
        }

        // Create a new array with one less element
        T[] newArray = new T[arr.Length - 1];

        // Copy elements before the ith element
        Array.Copy(arr, 0, newArray, 0, i - 1);

        // Copy elements after the ith element
        Array.Copy(arr, i, newArray, i - 1, arr.Length - i);

        return newArray;
    }

    static void Main()
    {
        // Initialize the original array
        int[] array = { 1, 2, 3, 4, 5 };

        // Specify which element to delete (3rd element in this case)
        int i = 4;

        // Print the original array
        Console.WriteLine("Original array: " + string.Join(", ", array));

        try
        {
            // Attempt to delete the ith element
            int[] newArray = DeleteIthElement(array, i);

            // Print the new array after deletion
            Console.WriteLine($"Array after deleting {i}th element: " + string.Join(", ", newArray));
        }
        catch (ArgumentOutOfRangeException e)
        {
            // Handle the case where an invalid index was provided
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}