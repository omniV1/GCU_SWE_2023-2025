namespace RegisterAndLoginApp.Models
{
    public interface IUserManager
    {
        public List<UserModel> GetAllUsers(); // Return all users stored in the system. 
        public UserModel GetUserById(int id); // Give id number, find the matching user. 
        public int AddUser(UserModel user); // Add a new user to the list / database. use during registratoion 
        public void DeleteUser(UserModel user); // Remove the user who matches. 
        public void UpdateUser(UserModel user); // Find the user with matching id and replace it. 
        public UserModel CheckCredentials(string username, string password);  // Verify login. 
    }
}
