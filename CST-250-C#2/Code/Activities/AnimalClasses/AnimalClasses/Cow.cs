using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalClasses
{
    internal class Cow : Animal, IMilkable, IDomesticated
    {

        public Cow() 
        {

            Console.WriteLine("Cow Constructor\n--------------------------------------"); 

        }
        public void milk(string name)
        {
            Console.WriteLine("The cow " + name + " is being milked" );
        }

        public void TouchMe()
        {
            Console.WriteLine("Please scratch my back!");
        }

        public void FeedMe()
        {
            Console.WriteLine("Its time to graze \n --------------------------------");
        }
    }
}

