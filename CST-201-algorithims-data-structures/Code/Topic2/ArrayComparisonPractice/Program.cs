using System;

class ComparisonCountingSort
{
    public static int[] Sort(int[] A)
    {
        int n = A.Length;
        int[] Count = new int[n]; // Initialize the Count array
        int[] S = new int[n];     // Output array for the sorted elements

        // Step 1: Initialize the Count array to 0
        for (int i = 0; i < n; i++)
        {
            Count[i] = 0;
        }

        // Step 2: Perform comparisons and populate the Count array
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (A[i] < A[j])
                {
                    Count[j]++;
                }
                else
                {
                    Count[i]++;
                }
            }
        }

        // Step 3: Place elements in their correct position in the sorted array
        for (int i = 0; i < n; i++)
        {
            S[Count[i]] = A[i];
        }

        return S; // Return the sorted array
    }

    static void Main()
    {
        int[] A = { 60, 35, 81, 98, 14, 47 };

        // Sort the array using Comparison Counting Sort
        int[] sortedArray = Sort(A);  // Declare and assign sortedArray

        // Output the sorted array
        Console.WriteLine("Sorted array: " + string.Join(", ", sortedArray));
    }
}
