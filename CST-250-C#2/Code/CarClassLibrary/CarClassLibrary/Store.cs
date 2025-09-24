
/// Owen Lindsey
/// Professor Sluiter
/// CST-250
/// This work was done with the help of the assignment guideu

namespace CarClassLibrary
{
    /// <summary>
    /// Represents a store that manages a list of cars for sale and a shopping list for customers.
    /// </summary>
    public class Store
    {
        /// <summary>
        /// List of cars available in the store.
        /// </summary>
        public List<Car> CarList { get; set; }

        /// <summary>
        /// Customer's shopping list of cars.
        /// </summary>
        public List<Car> ShoppingList { get; set; }

        /// <summary>
        /// Initializes new Store instance with empty car and shopping lists.
        /// </summary>
        public Store()
        {
            CarList = new List<Car>();
            ShoppingList = new List<Car>();
        }

        /// <summary>
        /// Calculates total cost of cars in shopping list and clears the list.
        /// </summary>
        /// <returns>Total cost of cars in shopping list.</returns>
        public decimal Checkout()
        {
            decimal totalCost = 0;

            // Calculate the total cost of items in the shopping list.
            foreach (var car in ShoppingList)
            {
                totalCost += car.Price;
            }

            // Clear the shopping list after checkout.
            ShoppingList.Clear();

            return totalCost;
        }
    }
}
