using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalClasses
{
       abstract class Animal
    {
        public Animal()
        {
            Console.WriteLine(""); 
        }
        public void Greet(string name)
        {
            Console.WriteLine( name + " says Hello"); 

        }
        public void Talk()
        {
            Console.WriteLine("Animal talking");
        }
        public virtual void Sing()
        {
            Console.WriteLine("Animal song");
        }
    };
}
