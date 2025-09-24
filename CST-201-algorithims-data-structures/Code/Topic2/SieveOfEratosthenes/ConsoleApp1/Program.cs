using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // maximum data set to iterate through is 100
            int maximum = 100000000;
            bool[] prime = new bool[maximum + 1];
            // iterate through all values from maximum and set them to true 
            for (int i = 0; i <= maximum; i++)
            {
                prime[i] = true;
            }
            // assume 0 and 1 are known false because they do not result in prime 
            prime[1] = false;
            prime[0] = false;
            //iterate from 2 to the square root of the limit
            for (int p = 2; p * p <= maximum; p++)
            {
                // if p is prime mark multiples as not prime
                if (prime[p])
                {
                    for (int i = p * p; i <= maximum; i += p)
                    {
                        prime[i] = false;
                    }
                }
            }
            for (int i = 2; i <= maximum; i++)
            {
                if (prime[i])
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}