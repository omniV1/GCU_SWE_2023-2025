///Owen Lindsey 
///Professor Sluiter 
///CSt-250 
///This work was done with the help of the assignment guide 

using CarClassLibrary;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;

namespace CarshopConsoleApp
{

    class Program
    {
        static Store CarStore = new();

        static void Main(string[] args)
        {
            Console.Out.WriteLine("Welcome to the car store. ");

            int action = ChooseAction();

            while (action != 0)
            {
                switch (action)
                {
                    case 1:
                        Console.Out.WriteLine("You chose to add a new car to the store:");
                        
                        ///reads the car Make safely as it 
                        ///avoids a NullReferenceException because
                        ///if a string is not found it will allow 
                        ///itself to be empty
                        Console.Out.WriteLine("What is the car make?");
                        string carMake = Console.ReadLine() ?? string.Empty;


                        ///reads the car model safely as it 
                        ///avoids a NullReferenceException because
                        ///if a string is not found it will allow 
                        ///itself to be empty
                        Console.Out.WriteLine("What is the car model");
                        string carModel = Console.ReadLine() ?? string.Empty;

                        ///Reads car price safely because if the program
                        ///does not recieve a decimal the exception will be handled and 
                        ///the user will be required to type only numbers 
                        decimal carPrice = ReadDecimal("What is the price? (only number)");

                        /// New properties that use custom input-reading methods 
                        /// that the above also used 
                        int carYear = ReadInt("Enter the car's year:");
                        bool isNewCar = ReadBoolean("Is the car new? (yes/no)");

                        // Create and add new car to the store
                        Car newCar = new()
                        {
                            Make = carMake,
                            Model = carModel,
                            Price = carPrice,
                            Year = carYear,
                            IsNew = isNewCar
                        };
                        CarStore.CarList.Add(newCar);
                        PrintStoreInventory(CarStore);
                        break;

                    case 2:
                        // You chose to buy a car

                        // Display the list of cars in inventory
                        PrintStoreInventory(CarStore);

                        /// This will safely check if the selected value is within the range 
                        /// of our index of Cars. if the user enters a number less or more than 
                        /// is listed the exception will be handled to prompt the user 
                        /// to enter a valid number 
                        Console.Out.WriteLine("Which car would you like to add to the cart");
                        if (int.TryParse(Console.ReadLine(), out int choice) && choice >= 0 && choice < CarStore.CarList.Count)
                        {
                            // Add the car to the shopping cart
                            CarStore.ShoppingList.Add(CarStore.CarList[choice]);
                            PrintShoppingCart(CarStore);
                        }
                        else
                        {
                            Console.Out.WriteLine("Invalid selection. Please enter a valid car number.");
                        }
                        break;


                    case 3:
                        //checkout

                        PrintShoppingCart(CarStore);
                        Console.Out.WriteLine("Your total cost is ${0}", CarStore.Checkout());

                        break;

                    default:
                        Console.Out.WriteLine("Invalid action. Please choose a valid option.");
                        break;
                }
                action = ChooseAction();
            }
        }


        /// <summary>
        /// Prompts the user to choose an action and ensures that the input is a valid number
        /// </summary>
        static int ChooseAction()
        {
            while (true)
            {
                Console.Write("Choose an action (0) quit (1) add a car (2) add item to cart (3) checkout: ");
                if (int.TryParse(Console.ReadLine(), out int choice))
                {
                    return choice;
                }
                Console.WriteLine("Invalid input. Please enter a number.");
            }
        }
        
        /// <summary>
        /// Prints the inventory of cars available in the store
        /// </summary>
        /// <param name="carStore">The store whose inventory will be printed</param>
        static public void PrintStoreInventory(Store carStore)
        {
            Console.Out.WriteLine("These are the cars in the Store inventory:");
            int i = 0;
            foreach (var c in carStore.CarList)
            {
                Console.Out.WriteLine(String.Format("Car # = {0} {1}", i, c.Display)); i++;
                ;
            }
        }
        /// <summary>
        /// Prints the list of cars that the user has added to the shopping cart
        /// </summary>
        /// <param name="carStore">The store whose shopping cart will be printed</param>
        static public void PrintShoppingCart(Store carStore)
        {
            Console.Out.WriteLine("These are the cars in your shopping cart:");
            int i = 0;
            foreach (var c in carStore.ShoppingList)
            {
                Console.Out.WriteLine(String.Format("Car # = {0} {1} ", i, c.Display));
            }
        }

        /// <summary>
        /// Reads an integer value from the user input safely
        /// It continues to prompt until a valid integer is entered
        /// A valid integer entered by the user
        /// </summary>
        /// <param name="message">The prompt message for the user.</param>
        static int ReadInt(string message)
        {
            while (true)
            {
                Console.Out.WriteLine(message);
                if (int.TryParse(Console.ReadLine(), out int result))
                {
                    return result;
                }
                Console.Out.WriteLine("Invalid input. Please enter a number.");
            }
        }
        /// <summary>
        /// Reads a decimal value from the user input safely
        /// It continues to prompt until a valid decimal is entered
        /// A valid decimal number entered by the user
        /// </summary>
        /// <param name="message">The prompt message for the user.</param>
        static decimal ReadDecimal(string message)
        {
            while (true)
            {
                Console.Out.WriteLine(message);
                if (decimal.TryParse(Console.ReadLine(), out decimal result))
                {
                    return result;
                }
                Console.Out.WriteLine("Invalid input. Please enter a valid decimal number.");
            }
        }
        /// <summary>
        /// Reads a boolean value from the user input safely
        /// It continues to prompt until 'yes' or 'no' is entered
        /// True if the user enters 'yes', false if 'no'
        /// </summary>
        /// <param name="message">The prompt message for the user.</param>
        static bool ReadBoolean(string message)
        {
            while (true)
            {
                Console.Out.WriteLine(message);
                string response = Console.ReadLine() ?? string.Empty;

                // Check for null before calling ToLower
                if (response != null)
                {
                    response = response.ToLower();
                }
                else
                {
                    response = string.Empty;
                }

                if (response == "yes") return true;
                if (response == "no") return false;
                Console.Out.WriteLine("Invalid input. Please answer 'yes' or 'no'.");
            }
        }

    }
    }

