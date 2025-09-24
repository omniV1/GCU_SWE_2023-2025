// Owen Lindsey
// 09/21/2024
// CST-201 Exercise 3
// This work is my own
using System;

class Program
{
    /// <summary>
    /// Deletes the ith element from a sorted array while maintaining the sorted order
    /// </summary>
    /// <param name="arr">The input sorted array</param>
    /// <param name="i">The index of the element to delete (1-based)</param>
    /// <returns>A new sorted array with the ith element removed</returns>
    /// <exception cref="ArgumentOutOfRangeException">Thrown when i is out of the valid range.</exception>
    static int[] DeleteIthElementSorted(int[] arr, int i)
    {
        // Check if the provided index is within the valid range
        if (i < 1 || i > arr.Length)
        {
            throw new ArgumentOutOfRangeException(nameof(i), "Index out of range");
        }

        // Create a new array with one less element
        int[] newArray = new int[arr.Length - 1];

        // Copy elements before the ith element
        Array.Copy(arr, 0, newArray, 0, i - 1);

        // Copy elements after the ith element, effectively shifting them one position to the left
        Array.Copy(arr, i, newArray, i - 1, arr.Length - i);

        return newArray;
    }

    static void Main()
    {
        // Initialize the original sorted array
        int[] sortedArray = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Specify which element to delete (5th element in this case)
        int i = 1;

        // Print the original array
        Console.WriteLine("Original sorted array: " + string.Join(", ", sortedArray));

        try
        {
            // Attempt to delete the ith element
            int[] newSortedArray = DeleteIthElementSorted(sortedArray, i);

            // Print the new array after deletion
            Console.WriteLine($"Sorted array after deleting {i}th element: " + string.Join(", ", newSortedArray));
        }
        catch (ArgumentOutOfRangeException e)
        {
            // Handle the case where an invalid index was provided
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}