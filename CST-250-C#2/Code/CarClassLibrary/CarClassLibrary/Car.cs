/// Owen Lindsey
/// Professor Sluiter
/// CST-250
/// This work was done with the help of the assignment guideusing System.Collections.Generic;


namespace CarClassLibrary
{
   /// <summary>
    /// Represents a car with properties for Make, Model, and Price.
    /// </summary>
    public class Car
    {
        /// <summary>
        /// Gets amd sets the make of the car
        ///  set to string.Empty to remove the possible null reference
        /// </summary>
        public string Make { get; set; } = string.Empty;

        /// <summary>
        /// Gets and sets the model of the car.
        /// set to string.Empty to remove the possible null reference 
        /// </summary>
        public string Model { get; set; } = string.Empty;

        /// <summary>
        /// Gets amd sets the price of the car
        /// </summary>
        public decimal Price { get; set; }
        
        /// <summary>
        /// sets or gets if the car is new or used
        /// </summary>
        public bool IsNew { get; set; }

        /// <summary>
        /// sets or gets the year the car was made 
        /// </summary>
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
        /// Initializes a new instance of the <see cref="Car"/> class with default values.
        /// </summary>
        /// <remarks>
        /// Useful for debugging and initializing a car object without specific details.
        /// </remarks>
        public Car()
        {
            Make = "Nothing";
            Model = "Nothing";
            Price = 0;
        }

        /// <summary>
        /// Gets a string representation of the car details.
        /// </summary>
        public string Display
        {
            get
            {
                return String.Format("{0} {1} ${2} Year: {3}, New: {4}", Make, Model, Price, Year, IsNew ? "Yes" : "No");
            }
        }

        
    }
}
