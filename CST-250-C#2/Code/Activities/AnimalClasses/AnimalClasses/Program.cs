using System; 



namespace AnimalClasses
{
    class Program
    {
        static void Main(string[] args) 
        {
         /*    Animal beast = new Animal();

            beast.Talk();
            beast.Greet();
            beast.Sing();
         */

            Dog bowser = new Dog();

            bowser.Talk(); 
            bowser.Greet("bowser");
            bowser.Sing();
            bowser.Fetch("Stick");
            bowser.FeedMe(); 
            bowser.TouchMe();

            Robin red = new Robin(); 

            
            red.Greet("red");
            red.Sing();
            red.Flying();
            red.Landing();
            red.TouchMe();
            //red.Fetch("worm");
           // red.FeedMe();
           // red.TouchMe(); 

            GoldFish goldy = new GoldFish();
            goldy.Greet("goldy");
            goldy.splash();
            goldy.FeedMe();

            Cow daisy = new Cow();
            daisy.milk("daisy"); 
            daisy.TouchMe();
            daisy.FeedMe();

            Goats billy = new Goats();
            billy.Greet(); 
            billy.milk("billy"); 
            billy.TouchMe();
            billy.FeedMe();
            
            

            Console.ReadLine(); 
        }
    }
}
