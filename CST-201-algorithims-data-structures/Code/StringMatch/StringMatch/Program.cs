using System;

public class StringMatcher
{
    public static int BruteForceStringMatch(string text, string pattern, char wildcard = '?')
    {
        // Assigns n to the number of items in the  array text
        int n = text.Length;

        // Assigns n to the number of items in the array pattern
        int m = pattern.Length;

        // the first loop is used to iterate through both lists stopping where there is no text to match
        for (int i = 0; i <= n - m; i++)
        {
            // set j to zero to iterate through each index
            int j = 0;

            // compares both of the lengths     
            while (j < m && (pattern[j] == wildcard || pattern[j] == text[i + j]))
            {
                // moves to the next character in the pattern
                j++;
            }
            // if j is the same as m return i because both m and n are the same and store it in variable i 
            if (j == m)
            {
                return i;
            }
        }

        return -1;
    }

    public static void Main(string[] args)
    {
        string text = "a,b,c,d,e,f,g";
        string pattern = "c,d,?,f";

        int result = BruteForceStringMatch(text, pattern);

        if (result != -1)
        {
            Console.WriteLine($"Pattern '{pattern}' found in '{text}' at index: {result}");
        }
        else
        {
            Console.WriteLine($"Pattern '{pattern}' not found in '{text}'");
        }
    }
}

// In class challenge make c d * g work (where the * means any character between d ----> g)