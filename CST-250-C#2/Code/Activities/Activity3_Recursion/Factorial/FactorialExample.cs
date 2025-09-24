using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Factorial
{
    internal class FactorialExample
    {
        static void Main(string[] args)
        {
            int startingNumber = 80;
            Console.WriteLine(factorial(startingNumber));
            Console.ReadLine();
        } 
        static int factorial(int x)
        {
           Console.Out.WriteLine("x is {0}", x);
            if (x == 1)
            {
                return 1; 
            }
            else
            {
                return x * factorial(x - 1); 
            }
        }
       
        }
    }

