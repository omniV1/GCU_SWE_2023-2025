using System.Data.SqlClient;
using RegisterAndLoginApp.Models;
using RegisterAndLoginApp.Services.DAO;
namespace RegisterAndLoginApp.Services.Buisness
{
    public class UserCollection : IUserManager
    {
        private List<UserModel> _users;

        public UserCollection()
        {
            _users = new List<UserModel>();
            GenerateUserData();
        }

        private void GenerateUserData()
        {
            UserModel user1 = new UserModel();
            user1.Username = "Owen";
            user1.SetPassword("lindsey");
            user1.Group = "Admin";
            AddUser(user1);

            UserModel user2 = new UserModel();
            user2.Username = "Sarah";
            user2.SetPassword("Lindsey");
            user2.Group = "Admin, User";
            AddUser(user2);
        }

        public int AddUser(UserModel user)
        { 
            user.Id = _users.Count + 1;
            _users.Add(user);
            return user.Id;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="username"></param>
        /// <param name="password"></param>
        /// <returns></returns>
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

        public void DeleteUser(UserModel user)
        {
            _users.Remove(user);
        }

        public List<UserModel> GetAllUsers()
        {
           UserDAO dataLayer = new UserDAO();
            return dataLayer.GetAllUsers();
        }
        /// <summary>
        /// Given an id number. Find the user with the matching id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
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
        /// <param name="user"></param>
        public void UpdateUser(UserModel user)
        {
            //Declare and initialize 
            int userId = -1;
            UserModel findUser = new UserModel();

            // Find matching id number
            //findUser variable will equal null if not found
            findUser = GetUserById(user.Id);

            // update exisiting user 
            if (findUser != null)
            {
                // Get the index of the user to update
                userId = _users.IndexOf(findUser);

                // update the user at this Id
                _users[userId] = user;

            }

            // find the user with the matching id and replace it 
            _users[_users.FindIndex(u => u.Id == user.Id)] = user;
        }

        // Method to generate and add fake user data to the 'user' list
        public void MakeSomeFakeData()
        {
            // Create and add some fake users to the list
            _users.Add(new UserModel { Id = 1, Username = "user1", PasswordHash = "password1" });
            _users.Add(new UserModel { Id = 2, Username = "user2", PasswordHash = "password2" });
            _users.Add(new UserModel { Id = 3, Username = "user3", PasswordHash = "password3" });
        }
    }
}