using Microsoft.AspNetCore.Identity;
using Milestone.Models;
using Milestone.Models.Interfaces;
using System.Data.SqlClient;



namespace Milestone.Services.Data.DAO
{
    public class UserDAO : IUserManager
    {
        // Define a connection string for MSSQL
        static string conn = @"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=UserAuth;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False";





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
                            // Return user if the creds are valid
                            return user;
                        }
                        // Create a UserModel object to store user default id of 0
                        UserModel user2 = new UserModel();
                        {

                        };
                        return user2;
                    }
                }


            }

        }

        public int AddUser(UserModel user)
        {
            int newUserId = 0;

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                // Check if the username already exists in the database
                // This is to ensure we don't create a user with a duplicate username
                string checkQuery = "SELECT COUNT(*) FROM UserAccount WHERE Username = @Username";
                using (SqlCommand checkCommand = new SqlCommand(checkQuery, connection))
                {
                    // Add the provided username as a parameter to the SQL query
                    checkCommand.Parameters.AddWithValue("@Username", user.Username);

                    // Execute the query and get the count of matching rows
                    int existingUserCount = (int)checkCommand.ExecuteScalar();

                    // If the count is greater than 0, it means the username already exists
                    if (existingUserCount > 0)
                    {
                        // Return 0 to indicate that the registration failed due to a duplicate username
                        return 0;
                    }
                }

                // If the username is unique, insert the new user into the database
                string insertQuery = "INSERT INTO UserAccount (Username, MyPassword, GroupName) VALUES (@Username, @MyPassword, @GroupName); SELECT SCOPE_IDENTITY();";
                using (SqlCommand insertCommand = new SqlCommand(insertQuery, connection))
                {
                    // Add the new user's details as parameters to the SQL query
                    insertCommand.Parameters.AddWithValue("@Username", user.Username);
                    insertCommand.Parameters.AddWithValue("@MyPassword", user.PasswordHash);
                    insertCommand.Parameters.AddWithValue("@GroupName", user.Group);

                    // Execute the insert query and retrieve the new user's ID
                    newUserId = Convert.ToInt32(insertCommand.ExecuteScalar());
                }
            }

            // Return the new user's ID, which can be used to perform additional actions (e.g., log in the user)
            return newUserId;
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
            using (SqlConnection connection = new SqlConnection(conn))
            {
                // Open connection to db
                connection.Open();

                query = "SELECT * FROM UserAccount";

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
        /// <summary>
        /// Updates an existing user in the database
        /// </summary>
        /// <param name="user">The user model with updated information</param>
        public void UpdateUser(UserModel user)
        {
            Console.WriteLine($"UserDAO: Updating user - Id={user.Id}, Username={user.Username}, Group={user.Group}");
            string query = "UPDATE UserAccount SET Username = @Username, GroupName = @GroupName WHERE Id = @Id";

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    // Add parameters to the SQL command
                    command.Parameters.AddWithValue("@Id", user.Id);
                    command.Parameters.AddWithValue("@Username", user.Username);
                    command.Parameters.AddWithValue("@GroupName", user.Group);

                    // Execute the update command and get the number of affected rows
                    int rowsAffected = command.ExecuteNonQuery();
                    Console.WriteLine($"UserDAO: Rows affected by update: {rowsAffected}");

                    // If no rows were affected, throw an exception
                    if (rowsAffected == 0)
                    {
                        throw new Exception("User not found or no changes were made.");
                    }
                }
            }
            Console.WriteLine("UserDAO: User updated successfully");
        }

        /// <summary>
        /// Deletes a user from the database
        /// </summary>
        /// <param name="user">The user model to be deleted</param>
        /// <returns>The deleted user model</returns>
        public UserModel DeleteUser(UserModel user)
        {
            string query = "DELETE FROM UserAccount WHERE Id = @Id";
            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    // Add the user ID parameter to the SQL command
                    command.Parameters.AddWithValue("@Id", user.Id);

                    // Execute the delete command and get the number of affected rows
                    int rowsAffected = command.ExecuteNonQuery();

                    // If a row was affected, return the deleted user model
                    if (rowsAffected > 0)
                    {
                        return user;
                    }
                    else
                    {
                        // If no rows were affected, throw an exception
                        throw new Exception("User not found or could not be deleted.");
                    }
                }
            }
        }


    }
}



