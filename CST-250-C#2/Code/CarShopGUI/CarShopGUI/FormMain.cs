///Owen Lindsey
///Professor Sluiter
///CST-250
///This work was done with the help of the assignment guide 
///1/14/2024





namespace CarShopGUI
{
    public partial class FormMain : Form
    {
        Store store = new();

        BindingSource carListBinding = new();
        BindingSource ShoppingListBinding = new();

        public FormMain()
        {
            InitializeComponent();
            SetBindings();
        }
        private void SetBindings()
        {
            carListBinding.DataSource = store.CarList;
            lbCarInventory.DataSource = carListBinding;
            lbCarInventory.DisplayMember = "Display";
            lbCarInventory.ValueMember = "Display";

            ShoppingListBinding.DataSource = store.ShoppingList;
            lbShoppingCart.DataSource = ShoppingListBinding;
            lbShoppingCart.DisplayMember = "Display";
            lbShoppingCart.ValueMember = "Display";
        }

        private void BtnCreateCar_OnClick_EventHandler(object sender, EventArgs e)
        {
            // Create a new instance of Car
            Car newCar = new()
            {
                Make = txtMake.Text, // Assuming txtMake is your TextBox for Make
                Model = txtModel.Text // Assuming txtModel is your TextBox for Model
            };

            // Check if the text entered into txtYear is a valid year (integer)
            if (int.TryParse(txtYear.Text, out int yearValue))
            {
                // Assign the parsed year to the newCar.Year property
                newCar.Year = yearValue;
            }
            else
            {
                // Handle the case where the entered text is not a valid integer
                MessageBox.Show("Please enter a valid year.");
                return; // Optionally, you could return from the method if the input is not valid
            }

            // Safely parse the price and handle possible parsing errors
            if (decimal.TryParse(txtPrice.Text, out decimal price))
            {
                newCar.Price = price;
            }
            else
            {
                // Handle the error, e.g., show a message to the user
                MessageBox.Show("Please enter a valid price.");
                return; // Exit the event handler early
            }

            // Check which radio button is selected
            if (rbNew.Checked)
            {
                newCar.IsNew = true;
            }
            else if (rbUsed.Checked)
            {
                newCar.IsNew = false;
            }

            // Add the new car to the store's car list
            store.CarList.Add(newCar);

            // Reset the bindings to reflect the changes in the UI
            carListBinding.ResetBindings(false);

            // Clear the text boxes
            txtMake.Text = string.Empty;
            txtModel.Text = string.Empty;
            txtYear.Text = string.Empty;
            txtPrice.Text = string.Empty;

            // Reset the radio buttons if needed
            rbNew.Checked = false;
            rbUsed.Checked = false;

            // Reset the bindings to reflect the changes in the UI
            carListBinding.ResetBindings(false);
        }

        /// <summary>
        /// Event handler for the 'Add to Cart' button click.
        /// Adds the selected car from the inventory to the shopping cart.
        /// </summary>
        /// <param name="sender">The object that raised the event.</param>
        private void BtnAddToCart_OnClick_EventHandler(object sender, EventArgs e)
        {
            // Check if a car is selected in the inventory list.
            if (lbCarInventory.SelectedItem != null)
            {
                // Get the selected car.
                Car selectedCar = (Car)lbCarInventory.SelectedItem;

                // Add the selected car to the shopping list.
                store.ShoppingList.Add(selectedCar);

                // Remove the selected car from the inventory.
                store.CarList.Remove(selectedCar);

                // Update the bindings to refresh both the inventory and shopping cart displays.
               
                ShoppingListBinding.ResetBindings(false);
            }
            else
            {
                // Inform the user that no car has been selected for adding to the cart.
                MessageBox.Show("Please select a car to add to the cart.");
            }
        }
        /// <summary>
        /// Event handler for the 'Checkout' button click.
        /// Calculates the total cost of the cars in the shopping cart and displays it.
        /// </summary>
        /// <param name="sender">The object that raised the event.</param>
        private void BtnCheckout_OnClick_EventHandler(object sender, EventArgs e)
        {
            // Perform the checkout operation which calculates the total and clears the shopping list.
            decimal total = store.Checkout();

            // Display the total cost to the user.
            lblDisplayTotal.Text = $"Total cost: {total:C2}"; // C2 formats the number as a currency

            // Clear the shopping cart / car inventory list in the GUI 
            carListBinding.ResetBindings(false);
            ShoppingListBinding.ResetBindings(false);
        }
        
    }
}
