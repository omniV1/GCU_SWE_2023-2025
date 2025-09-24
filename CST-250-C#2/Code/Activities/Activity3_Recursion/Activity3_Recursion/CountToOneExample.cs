using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Activity3_Recursion
{
    internal class CountToOneExample
    {
        static void Main(string[] args)
        {
            Console.Out.Write("Please enter an integer.\nI will do some math and eventually arrive at 1\n"); 

            int startingNumber = int.Parse(Console.ReadLine());
            int x = CountToOne(startingNumber);
            Console.ReadLine(); 
        }
         static public int CountToOne(int n)
        {
            Console.Out.WriteLine("N is {0}", n); 
            if (n == 1) 
                    {
                return 1; 
                     }
            else
            {
                if (n % 2 == 0)
                {
                    Console.Out.WriteLine("N is even. Divide by 2");
                    return CountToOne(n / 2); 
                }
                else 
                {
                    Console.Out.WriteLine("N is odd. Add 1"); 
                    return CountToOne( n + 1); 
                }
            }
        }
    }
}
