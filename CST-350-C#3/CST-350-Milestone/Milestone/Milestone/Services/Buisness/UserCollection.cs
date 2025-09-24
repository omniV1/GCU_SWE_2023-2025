using System.Data.SqlClient;
using Milestone.Models;
using Milestone.Models.Interfaces;
using Milestone.Services.Data.DAO;

namespace Milestone.Services.Buisness
{
    public class UserCollection : IUserManager
    {
        private List<UserModel> _users;
        private UserDAO dataLayer;

        public UserCollection()
        {
            dataLayer = new UserDAO();
            _users = new List<UserModel>();
        }

        /// <summary>
        /// Adds a user to the database
        /// </summary>
        /// <param name="user"></param>
        /// <returns></returns>
        public int AddUser(UserModel user)
        {
            // Call the AddUser method in the UserDAO class to add the new user to the database
            return dataLayer.AddUser(user);
        }

        /// <summary>
        /// Checks if the provided username and password match a user in the database
        /// </summary>
        /// <param name="username">The username to check</param>
        /// <param name="password">The password to check</param>
        /// <returns>A UserModel if credentials are valid, null otherwise</returns>
        public UserModel CheckCredentials(string username, string password)
        {
            // Declare and init
            // transport data object
            UserModel user = new UserModel();
            // Given a Username Password, find a matching user. Return the user`s ID
            // instantiate the UserDAO
            UserDAO dataAccess = new UserDAO();
            user = dataAccess.CheckCredentials(username, password);

            return user;
        }

        /// <summary>
        /// Deletes a user from the database
        /// </summary>
        /// <param name="user">The user to delete</param>
        /// <returns>The deleted UserModel</returns>
        public UserModel DeleteUser(UserModel user)
        {
            Console.WriteLine($"UserCollection: Deleting user - Id={user.Id}, Username={user.Username}, Group={user.Group}");
            return dataLayer.DeleteUser(user);
        }

        /// <summary>
        /// Retrieves all users from the database
        /// </summary>
        /// <returns>A list of all UserModels</returns>
        public List<UserModel> GetAllUsers()
        {
            UserDAO dataLayer = new UserDAO();
            return dataLayer.GetAllUsers();
        }

        /// <summary>
        /// Given an id number. Find the user with the matching id
        /// </summary>
        /// <param name="id">The id of the user to find</param>
        /// <returns>The UserModel with the matching id</returns>
        public UserModel GetUserById(int id)
        {
            // Instantiate the data acess layer and pass the data up and down n layer 
            UserDAO userDAO = new UserDAO();
            // pass id down to data acess layer
            // and then retrieve it back in userModel
            UserModel userModel = userDAO.GetUserById(id);
            // Then return it back to controller
            return userModel;
        }

        /// <summary>
        /// Find an existing user and update that user 
        /// </summary>
        /// <param name="user">The updated user information</param>
        public void UpdateUser(UserModel user)
        {
            Console.WriteLine($"UserCollection: Updating user - Id={user.Id}, Username={user.Username}, Group={user.Group}");
            dataLayer.UpdateUser(user);
            Console.WriteLine("UserCollection: User updated successfully");
        }

    }
}