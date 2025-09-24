// Owen Lindsey
// Professor Demland, David
// CST-201
// Exercise 2 
// This work is my own 

using System;

class ComparisonCountingSort
{

    public static int[] Sort(int[] A)
    {
        int n = A.Length;
        int[] Count = new int[n];
        int[] S = new int[n];

        // Count smaller elements 
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (A[i] < A[j])
                    Count[j]++;
                else
                    Count[i]++;
            }
        }

        // Place elements in sorted order
        for (int i = 0; i < n; i++)
        {
            S[Count[i]] = A[i];
        }
        return S;
    }
    public static void Main(string[] args)
    {
        int[] arr = { 60, 35, 81, 98, 14, 47 };
        Console.WriteLine("Original array: " + string.Join(",", arr));

        int[] sortedArr = Sort(arr);
        Console.WriteLine("Sorted array: " + string.Join(",", sortedArr));
    }
}