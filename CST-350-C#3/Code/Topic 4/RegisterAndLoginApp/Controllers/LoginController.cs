using Microsoft.AspNetCore.Mvc;
using RegisterAndLoginApp.Filters;
using RegisterAndLoginApp.Models;
using RegisterAndLoginApp.Services.Buisness;
using System.Text;

namespace RegisterAndLoginApp.Controllers
{
    public class LoginController : Controller
    {
        // private static UserCollection users = new UserCollection();

        // Dependency injection (DI) to the user manager 
        // Use the interface IUserManager to define users
        private IUserManager users; 
        
        // Constructor injection. The userManager is injected into 
        // the controller per the settings in program.cs
        public LoginController(IUserManager userManager)
        {
            // Assigns users to the userManager parameter
            users = userManager;
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
            // declare and initialize 
            int result = -1;
            string userJson = "";
            UserModel user = null;

     
            // If the result is greater than 0 (indicating a successful login)
            user = users.CheckCredentials(username, password);

            if (user.Id > 0)
            {
                // Create a new instance of our user model with props
                // This data reps the user data provided during login attempt
                UserModel userData = new() { Id = 1, Username = username, PasswordHash = password, Group = user.Group};

                // Serialize the 'userData' object to a JSON string
                userJson = ServiceStack.Text.JsonSerializer.SerializeToString(userData);

                // Store the serialized user data in the session with the key "User"
                HttpContext.Session.SetString("User", userJson);

                // Return the serialized user data in the session with the key "User" 
                return View("LoginSuccess", userData);
            }
            return View("LoginFailure");

        }

        [SessionCheckFilter]
        public IActionResult MembersOnly()
        {
            return View();
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

        
        public IActionResult ProcessRegister(RegisterViewModel registerViewModel)
        {

            UserModel user = new UserModel(); 

            user.Username = registerViewModel.Username;
           
            user.SetPassword(registerViewModel.Password);

            user.Group = "";

            StringBuilder groupsBuilder = new StringBuilder();

            foreach (var group in registerViewModel.Groups)
            {
                if (group.IsSelected)
                {
                    groupsBuilder.Append(group.GroupName).Append(",");

                }
            }
            user.Group = user.Group.TrimEnd(',');
            users.AddUser(user);
                

             

            return View("Index");
        }
    }
}

    