///Owen Lindsey
///Professor Sluiter
///CST-250
///This work was done with the help of the assignment guide 
///1/14/2024

namespace CarShopGUI
{
    /// <summary>
    /// Represents a car with properties for Make, Model, and Price.
    /// </summary>
    public class Car
    { 
        /// Gets amd sets the make of the car
        ///  set to string.Empty to remove the possible null reference
     
        public string Make { get; set; } = string.Empty;

       
        /// Gets and sets the model of the car.
        /// set to string.Empty to remove the possible null reference 
    
        public string Model { get; set; } = string.Empty;

       
        /// Gets amd sets the price of the car
       
        public decimal Price { get; set; }

       
        /// sets amd gets if the car is new or used
        
        public bool IsNew { get; set; }

      
        /// sets and gets the year the car was made 
        
        public int Year { get; set; }

        /// <summary>
        /// Initializes a new instance of the <see cref="Car"/> class with specified make, model, and price
        /// </summary>
        /// <param name="make">The make of the car.</param>
        /// <param name="model">The model of the car.</param>
        /// <param name="price">The price of the car.</param>
        public Car(string make, string model, decimal price)
        {
            Make = make;
            Model = model;
            Price = price;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="Car"/> class with default values
        /// </summary>
        /// <remarks>
        /// Useful for debugging and initializing a car object without specific details
        /// </remarks>
        public Car()
        {
            Make = "Nothing";
            Model = "Nothing";
            Price = 0;
            Year = 0; 
            IsNew = false;
        }

        /// <summary>
        /// Gets a string representation of the car details
        /// </summary>
        public string Display
        {
            get
            {
                return string.Format("{0} {1} ${2} Year: {3}, New: {4}", Make, Model, Price, Year, IsNew ? "Yes" : "No");
            }
        }


    }
}
