// Owen Lindsey
// Professor Hughes, Bill
// This was done in class. 
// CST-350 
// 10/27/2024

using Microsoft.AspNetCore.Mvc;
using RegisterAndLoginApp.Models;
using RegisterAndLoginApp.Services.Buisness;

namespace RegisterAndLoginApp.Controllers
{
    public class UserController : Controller
    {
        static UserCollection users = new UserCollection();
        UserModel searchResults = new UserModel();
        List<UserModel> user = new List<UserModel>();

        /// <summary>
        /// Get the Id and return all the information about the user.
        /// </summary>
        /// <returns></returns>
        public IActionResult Index(int id)
        {
            // First we need to instantiate the UserCollection buisness layer
            UserCollection buisnessLayer = new UserCollection();
            // Send the id and return the entire user model
            searchResults = buisnessLayer.GetUserById(id);
            return View(searchResults);
        }

        /// <summary>
        /// Retrieves all users and returns a view with the list of users
        /// </summary>
        /// <returns>A view containing all users</returns>
        public IActionResult AllUsers()
        {
            // Instantiate the buisness layer
            UserCollection buisnessLayer = new UserCollection();

            List<UserModel> allUsers = buisnessLayer.GetAllUsers();
            return View(allUsers);
        }

        /// <summary>
        /// Displays the edit form for a specific user
        /// </summary>
        /// <param name="id">The ID of the user to edit</param>
        /// <returns>The edit view for the specified user</returns>
        [HttpGet]
        public IActionResult Edit(int id)
        {
            var user = users.GetUserById(id);
            if (user == null || user.Id == 0)
            {
                return NotFound();
            }
            return View(user);
        }

        /// <summary>
        /// Processes the edit form submission for a user
        /// </summary>
        /// <param name="id">The ID of the user being edited</param>
        /// <param name="user">The updated user model</param>
        /// <returns>Redirects to AllUsers on success, or returns to the edit view on failure</returns>
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(int id, [Bind("Id,Username,Group")] UserModel user)
        {
            // Log the received data for debugging purposes
            Console.WriteLine($"Received POST: id={id}, User.Id={user.Id}, Username={user.Username}, Group={user.Group}");

            // Check if the ID in the route matches the ID in the user model
            if (id != user.Id)
            {
                Console.WriteLine("ID mismatch");
                return NotFound(); // Return 404 if IDs don't match
            }

            // Validate the model state
            if (!ModelState.IsValid)
            {
                Console.WriteLine("ModelState is invalid:");
                // Loop through all model state errors and log them
                foreach (var key in ModelState.Keys)
                {
                    var modelStateVal = ModelState[key];
                    foreach (var error in modelStateVal.Errors)
                    {
                        Console.WriteLine($"Key: {key}, Error: {error.ErrorMessage}");
                    }
                }
               
            }

            try
            {
                // Attempt to update the user in the database
                users.UpdateUser(user);
                Console.WriteLine("User updated successfully");

                // Set a success message in TempData to be displayed on the next request
                TempData["SuccessMessage"] = "User updated successfully.";

                // Redirect to the AllUsers action to show the updated list
                return RedirectToAction(nameof(AllUsers));
            }
            catch (Exception ex)
            {
                // Log any errors that occur during the update process
                Console.WriteLine($"Error updating user: {ex.Message}");

                // Add a model error to be displayed to the user
                ModelState.AddModelError("", "Unable to save changes. " + ex.Message);
            }

            // If we reach here, it means there was an error
            // Return to the edit view with the current user data
            return View(user);
        }

        /// <summary>
        /// Displays the delete confirmation page for a specific user
        /// </summary>
        /// <param name="id">The ID of the user to delete</param>
        /// <returns>The delete confirmation view for the specified user</returns>
        [HttpGet]
        public IActionResult Delete(int id)
        {
            var user = users.GetUserById(id);
            if (user == null || user.Id == 0)
            {
                return NotFound();
            }
            return View(user);
        }

        /// <summary>
        /// Processes the deletion of a user
        /// </summary>
        /// <param name="id">The ID of the user to delete</param>
        /// <returns>Redirects to AllUsers on success, or returns to the delete view on failure</returns>
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            var user = users.GetUserById(id);
            if (user == null || user.Id == 0)
            {
                return NotFound();
            }

            try
            {
                users.DeleteUser(user);
                Console.WriteLine("User deleted successfully");
                TempData["SuccessMessage"] = "User deleted successfully.";
                return RedirectToAction(nameof(AllUsers));
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error deleting user: {ex.Message}");
                ModelState.AddModelError("", "Unable to delete user. " + ex.Message);
            }

            return View(user);
        }
    }
}