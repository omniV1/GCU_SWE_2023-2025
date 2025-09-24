using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalClasses
{
    internal class GoldFish : Animal, ISwimming, IDomesticated
    {
        public GoldFish() 
        {
            Console.WriteLine("Goldfish constructor\n-----------------------------------------"); 
        }
        public void splash()
        {
            Console.WriteLine("Splish splash");
        }
        public void Greet(string name)
        {
            Console.WriteLine("Gulp");

        }

        /// <summary>
        ///  intentionall let unimplemented please dont pet your fish
        /// </summary>
        /// <exception cref="NotImplementedException"></exception>
        public void TouchMe()
        {
            throw new NotImplementedException();
        }

        public void FeedMe()
        {
            Console.WriteLine("SWISH SWISH ZOOM\n----------------------------------------------");
        }
    }
}
