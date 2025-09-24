using RegisterAndLoginApp.Models;
using System.Data.SqlClient;
using System.Diagnostics;


namespace RegisterAndLoginApp.Services.DAO
{
    public class UserDAO : IUserManager
    {
        // Define a connection string for MSSQL
        static string conn = @"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=UserAuth;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False";

        /// <summary>
        /// Add a new user
        /// </summary>
        /// <param name="user"></param>
        /// <returns></returns>
        public int AddUser(UserModel user)
        {
            // declare and initialize
            string query = "";
            int result = -1; 
            // using is the garabage collector to manage our resources 
            // creates a new SQL connection
            using (SqlConnection connection = new SqlConnection(conn))
            {
                // Open the connection to the database 
                connection.Open();

                // Define the sql query with parameter place holder
                // to prevent sql injection attacks
                query = @"INSERT INTO UserAccount (Username, MyPassword, GroupName)
                         VALUES (@Username, @MyPassword, @GroupName)
                           SELECT SCOPE_IDENTITY();"; // SELECT COPE_IDENTITY returns the last inserted ID

                // Create a SQL command object using the query and open connection
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    // Add parameters to the comanmd to safely pass user input 
                    // values, avoid SQL injection
                    command.Parameters.AddWithValue("@Username", user.Username);
                    command.Parameters.AddWithValue("@MyPassword", user.PasswordHash);
                    command.Parameters.AddWithValue("@GroupName", user.Group);

                    // Execute the query and retrieve the new inserted ID using Execute Scaler
                    if (int.TryParse(command.ExecuteScalar().ToString(), out result))
                    {
                        return result; 
                    }
                    else
                    {
                        // My homework is to complete this so the user knows to reenter the int
                        throw new InvalidOperationException("Failed to retrieve inserted ID."); 
                    }
                }

            }
        }
        /// <summary>
        /// This method will be used to verify a login attempt
        /// </summary>
        /// <param name="username"></param>
        /// <param name="password"></param>
        /// <returns></returns>
        public UserModel CheckCredentials(string username, string password)
        {
            // Declare and initialize 
            string query = "";

            // Open a new SQL conncetion

            using (SqlConnection connection = new SqlConnection(conn))
            {
                // open the connection to the db
                connection.Open();

                // define our query
                query = "SELECT * FROM UserAccount WHERE username = @Username AND MyPassword = @MyPassword";

                // create a SQL command object
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    // Add the username parameter 
                    command.Parameters.AddWithValue("@Username", username);
                    command.Parameters.AddWithValue("@MyPassword", password);

                    // Execute the command and object the SqlDataReader
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        // Check if any records are returned (meaning a user with matching credentials) 
                        if(reader.Read())
                        {
                            // We know there is at least one row
                            // Create a user model object to store the users details from the db
                            UserModel user = new UserModel
                            {
                                Id = reader.GetInt32(reader.GetOrdinal("Id")),
                                Username = reader.GetString(reader.GetOrdinal("Username")),
                                PasswordHash = reader.GetString(reader.GetOrdinal("MyPassword")),
                                Group = reader.GetString(reader.GetOrdinal("GroupName"))

                            };
                            // Return user if the creds are valid
                            return user; 
                        }
                        // Create a UserModel object to store user default id of 0
                        UserModel user2 = new UserModel();
                        {
                            // lol idk why this is happening 
                        };
                        return user2;
                    }
                }


            }

        }

        public void DeleteUser(UserModel user)
        {
            throw new NotImplementedException();
        }
        /// <summary>
        /// get all users and return the list
        /// </summary>
        /// <returns>List<Usermodel></USermodel></returns>
        /// <exception cref="NotImplementedException"></exception>
        public List<UserModel> GetAllUsers()
        {
            string query = ""; 

            List<UserModel> userList = new List<UserModel>();

            // Step 1: create a connection to the db
            using(SqlConnection connection = new SqlConnection(conn))
            {
            // Open connection to db
            connection.Open(); 
                
            query = ("SELECT * FROM UserAccount");

                // Step 2: SQL command 
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    // Step 3: create the reader
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            // Create a userModel object to store the users details
                            UserModel user = new UserModel(); 
                            // populate user
                            user.Id = reader.GetInt32(reader.GetOrdinal("Id"));
                            user.Username = reader["username"].ToString();
                            user.PasswordHash = reader["MyPassword"].ToString();
                            user.Group = reader["GroupName"].ToString(); 

                            // Add each user to list 
                            userList.Add(user);
                        }
                       
                    }
                }

            }
            // Return user list
            return userList;
        }

        /// <summary>
        /// Get user by id and return it 
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        /// <exception cref="NotImplementedException"></exception>
        public UserModel GetUserById(int id)
        {
           string query = ""; 

            // Find the matching id 
            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                // define our query
                query = string.Format("SELECT * From UserAccount WHERE Id = {0}", id);

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                  
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        if (reader.Read())
                        {
                            // We know there is at least one row
                            // Create a user model object to store the users details from the db
                            UserModel user = new UserModel
                            {
                                Id = reader.GetInt32(reader.GetOrdinal("Id")),
                                Username = reader.GetString(reader.GetOrdinal("Username")),
                                PasswordHash = reader.GetString(reader.GetOrdinal("MyPassword")),
                                Group = reader.GetString(reader.GetOrdinal("GroupName"))

                            };
                            //Return users information
                            return user;
                        }
                        UserModel user2 = new UserModel
                        {
                            Id = 0
                        };

                        return user2; 
                    }


                }
            }

        }

        public void UpdateUser(UserModel user)
        {
            throw new NotImplementedException();
        }


        // Define the conncetion string  MySQL

        // static string serverName = "localhost";
        // static string username = "root";
        // static string password = "root";
        // static string database = "UserAuth";
        // static string port = "3306"; 

        // set connection string 

        // string interpolation
        // static string conn = $"serverName={localhost}; username={root}; password={root}, database={UserAuth}, Port={3306}";

        // MySqlConnection connection = new MySqlConnection(conn); 

    }
}
