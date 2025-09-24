using Microsoft.AspNetCore.Mvc;
using RegisterAndLoginApp.Models;
using RegisterAndLoginApp.Services.Buisness;

namespace RegisterAndLoginApp.Controllers
{
    public class UserController : Controller
    {
        static UserCollection users = new UserCollection();

        UserModel searchResults = new UserModel();

        List<UserModel> user2 = new UserModel();
        /// <summary>
        /// Get the Id and return all the information about the user.
        /// </summary>
        /// <returns></returns>
        public IActionResult Index(int id)
        {
            // First we need to instantiate the UserCollection buisness layer\
            UserCollection buisnessLayer = new UserCollection();

            // Send the id and return the entire user model
            searchResults = buisnessLayer.GetUserById(id);

            return View(searchResults);
        }

        public IActionResult AllUsers()
        {
            // Instantiate the buisness layer
            UserCollection buisnessLayer = new UserCollection();
            
            Users2 = buisnessLayer.GetAllUsers();

            return View(users);
        }
    }
}