using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalClasses
{
    internal class Robin : Animal, IFlyable, IDomesticated
    {
        public Robin()
        {
            Console.WriteLine("Robin constructor\n------------------------------------");
        }
        public void FeedMe()
        {
            Console.WriteLine("Yummy worms");  
        }

        public void Flying() 
        {
            Console.WriteLine("Flying"); 
        }

        public void Landing()
        {
            Console.WriteLine("landing");
        }

        public void Sing()
        {
           Console.WriteLine("Chirp Chirp"); 
        }

        public void TouchMe()
        {
            Console.WriteLine("Landed on your shoulder to say hello\n-------------------------------");
        }
    }
}
