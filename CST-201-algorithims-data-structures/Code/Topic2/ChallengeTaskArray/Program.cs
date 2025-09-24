using System;

int[] numbers = { 45, 12, 85, 32, 89, 39, 69, 44, 42, 1 }; 

for (int i = 0; i < numbers.Length; i++)
{
    for (int j = 0; j < numbers.Length - 1; j++)
    {
        if (numbers[i] > numbers[j])
        {
            {
                int temp = numbers[j]; 
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }
    foreach (int n in numbers)
    {
        {
            Console.WriteLine(n + "");
        }
    }
}