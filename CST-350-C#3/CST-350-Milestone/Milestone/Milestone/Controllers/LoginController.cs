// Owen Lindsey
// Professor Hughes, Bill
// This was adapted from in class examples. 
// Milestone 1
// CST-350 
// 10/27/2024


using Microsoft.AspNetCore.Mvc;
using Milestone.Filters;
using Milestone.Models;
using Milestone.Services.Buisness;



namespace Milestone.Controllers
{
    public class LoginController : Controller
    {
        // Instantiate the userCollection class and create an object of named users

        private static UserCollection users = new UserCollection();

        private readonly ILogger<LoginController> _logger;

        public LoginController(ILogger<LoginController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }
        /// <summary>
        ///  Define an action method 'ProcessLogin' that handles the user login 
        ///  with the username and password
        /// </summary>
        /// <param name="loginViewModel"></param>
        /// <returns></returns>
        public IActionResult ProcessLogin(string username, string password)
        {
            try
            {
                _logger.LogInformation($"Login attempt - Username: {username}");

                var user = users.CheckCredentials(username, password);
                _logger.LogInformation($"User lookup result - Found: {user != null}, ID: {user?.Id}");

                if (user?.Id > 0)
                {
                    var userData = new UserModel
                    {
                        Id = user.Id,  // Make sure this is the correct ID from the database
                        Username = username,
                        PasswordHash = password,
                        Group = user.Group
                    };

                    var userJson = ServiceStack.Text.JsonSerializer.SerializeToString(userData);
                    _logger.LogInformation($"Serialized user data: {userJson}");

                    HttpContext.Session.SetString("User", userJson);

                    // Verify session was set
                    var sessionCheck = HttpContext.Session.GetString("User");
                    _logger.LogInformation($"Session verification - Data present: {!string.IsNullOrEmpty(sessionCheck)}");

                    return View("LoginSuccess", userData);
                }
                _logger.LogWarning($"Login failed for username: {username}");
                return View("LoginFailure");
            }
            catch (Exception ex)
            {
                _logger.LogError($"Login error: {ex.Message}");
                return View("LoginFailure");
            }
        }

        [SessionCheckFilter]
        public IActionResult MembersOnly()
        {
            // Retrieve the serialized user data from the session
            var userJson = HttpContext.Session.GetString("User");
            var userData = ServiceStack.Text.JsonSerializer.DeserializeFromString<UserModel>(userJson);

            // Split the user's group string into an array of individual groups
            // This is necessary because the group information is stored as a comma-separated string in the database
            string[] groups = userData.Group.Split(',');

            // Check the user's group memberships to determine their access level
            if (groups.Contains("Admin"))
            {
                // If the user is an admin, display the admin-specific content
                // This might include additional functionality or pages that only admins can access
                return View("MembersOnly", userData);
            }
            else if (groups.Contains("Users"))
            {
                // If the user is a regular member (not an admin), display the members-only content
                // This could be the main members-only area where users can access exclusive features
                return View("MembersOnly", userData);
            }
            else
            {
                // If the user doesn't belong to either the "Admin" or "Users" group,
                // they don't have access to the members-only area, so redirect them to the home page
                return RedirectToAction("Index", "Home");
            }
        }

        [SessionCheckFilter]
        public IActionResult Logout()
        {
            HttpContext.Session.Remove("User");
            return View("Index");
        }

        public IActionResult Register()
        {
            return View(new RegisterViewModel());
        }
        
        public IActionResult AddUser(RegisterViewModel registerViewModel)
        {
            if (ModelState.IsValid)
            {
                // Create a new UserModel instance
                UserModel newUser = new UserModel
                {
                    Username = registerViewModel.Username,
                    PasswordHash = registerViewModel.Password, // You'll need to hash and salt the password
                    Group = string.Join(",", registerViewModel.Groups.Where(g => g.IsSelected).Select(g => g.GroupName))
                };

                // Add the new user to the database
                int newUserId = users.AddUser(newUser);

                if (newUserId > 0)
                {
                    // Optionally, you can log the user in automatically after registration
                    var userData = new UserModel
                    {
                        Id = newUserId,
                        Username = newUser.Username,
                        PasswordHash = newUser.PasswordHash,
                        Group = newUser.Group
                    };
                    var userJson = ServiceStack.Text.JsonSerializer.SerializeToString(userData);
                    HttpContext.Session.SetString("User", userJson);

                    return View("LoginSuccess", userData);
                }
                else
                {
                    // Handle registration failure
                    ModelState.AddModelError(string.Empty, "Registration failed. Please try again.");
                }
            }

            // If the model state is invalid or the registration fails, return the view with the errors
            return View(registerViewModel);
        }
        public IActionResult ProcessRegister(RegisterViewModel registerViewModel)
        {
            if (ModelState.IsValid)
            {
                // Create a new UserModel instance
                UserModel newUser = new UserModel
                {
                    Username = registerViewModel.Username,
                    PasswordHash = registerViewModel.Password, // You'll need to hash and salt the password
                    Group = string.Join(",", registerViewModel.Groups.Where(g => g.IsSelected).Select(g => g.GroupName))
                };

                // Add the new user to the database
                int newUserId = users.AddUser(newUser);

                if (newUserId > 0)
                {
                    // Optionally, you can log the user in automatically after registration
                    var userData = new UserModel
                    {
                        Id = newUserId,
                        Username = newUser.Username,
                        PasswordHash = newUser.PasswordHash,
                        Group = newUser.Group
                    };
                    var userJson = ServiceStack.Text.JsonSerializer.SerializeToString(userData);
                    HttpContext.Session.SetString("User", userJson);

                    return View("LoginSuccess", userData);
                }
                else
                {
                    // Handle registration failure
                    ModelState.AddModelError(string.Empty, "Registration failed. Please try again.");
                }
            }

            // If the model state is invalid or the registration fails, return the view with the errors
            return View(registerViewModel);
        }
    }
}
