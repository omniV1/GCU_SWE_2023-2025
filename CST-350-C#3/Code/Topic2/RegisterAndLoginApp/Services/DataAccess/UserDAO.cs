using RegisterAndLoginApp.Models;
using System.Data.SqlClient;

namespace RegisterAndLoginApp.Services.DataAccess
{
    public class UserDAO
    {
        string connectionString = @"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=UserInfo;Integrated Security=True;Connect Timeout=30;Encrypt=False;Trust Server Certificate=False;Application Intent=ReadWrite;Multi Subnet Failover=False";

        public int AddUser(UserModel user)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                string query = @"
                INSERT INTO users(Username, MyPassword, GroupName) 
                VALUES (@Username, @MyPassword, @GroupName);
                SELECT SCOPE_IDENTITY();";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@Username", user.Username);
                    command.Parameters.AddWithValue("@MyPassword", user.PasswordHash);
                    command.Parameters.AddWithValue("@GroupName", user.Group);

                    // Execute the query and get the newly inserted ID
                    object result = command.ExecuteScalar();
                    return Convert.ToInt32(result);

                }


            }
        }
    }
}
