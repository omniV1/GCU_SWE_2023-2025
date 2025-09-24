using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalClasses
{
       internal class Dog : Animal , IDomesticated
    {
      public Dog() 
        {
            Console.WriteLine("Dog constructor. Good puppy.\n---------------"); 

        }
        public new void Talk()
        {
            Console.WriteLine("Bark Bark Bark"); 
        }
        public override void Sing()
        {
            Console.WriteLine("Hooooooooooowwwwwwwl!");
        }
        public void Fetch(string thing)
        {
            Console.WriteLine("Oh boy. Here is your " + thing + ". Let's do it again!"); 
        }

        public void TouchMe()
        {
            Console.WriteLine("Please scratch behind my ears\n---------------------------------");
        }

        public void FeedMe()
        {
            Console.WriteLine("It's suppertime. The very best time of day!!!");
        }

     
    }
}
