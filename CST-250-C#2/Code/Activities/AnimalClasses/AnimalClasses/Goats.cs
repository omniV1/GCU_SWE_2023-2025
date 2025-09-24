using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalClasses
{
    internal class Goats : Animal, IDomesticated, IMilkable
    {
        public Goats() 
        {
            Console.WriteLine("Goats constructor\n-----------------------");
        }
        public void FeedMe()
        {
            Console.WriteLine("Goats will eat anything\n--------------------");
        }

        public void milk(string name)
        {
            Console.WriteLine("The goat " + name + " is being milked"); 
        }

        public void Greet()
        {
            Console.WriteLine("Baaaaaaaaaahhh");
        }

        public void TouchMe()
        {
           Console.WriteLine("Goats love scratches behind their ears");
        }
    }
}
