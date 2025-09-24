using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DatabaseSQLMusicApp
{
    internal class AlbumDAO
    {
        public List<Album> albums = new List<Album>();
        private string connectionString = "server=localhost;port=8889;user=root;password=root;database=music";

        public List<Album> GetAllAlbums()
        {
            List<Album> returnThese = new List<Album>();

            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();
                MySqlCommand cmd = new MySqlCommand("SELECT ID, ALBUM_TITLE, ARTIST, YEAR, IMAGE_NAME, DESCRIPTION FROM album", connection);

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        Album album = new Album
                        {
                            ID = reader.GetInt32(0),
                            AlbumName = reader.GetString(1),
                            ArtistName = reader.GetString(2),
                            Year = reader.GetInt32(3),
                            ImageURL = reader.GetString(4), // Assuming you have a property named ImageURL
                            Description = reader.GetString(5)
                        };

                        returnThese.Add(album);
                    }
                }
            }

            return returnThese;
        }
        public List<Album> SearchTitles(string searchTerm)
        {
            List<Album> returnThese = new List<Album>();

            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                // Using a parameterized query to prevent SQL injection
                string query = "SELECT ID, ALBUM_TITLE, ARTIST, YEAR, IMAGE_NAME, DESCRIPTION FROM album WHERE ALBUM_TITLE LIKE @searchTerm";
                MySqlCommand cmd = new MySqlCommand(query, connection);
                cmd.Parameters.AddWithValue("@searchTerm", "%" + searchTerm + "%"); // The % symbols are wildcards for LIKE

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        Album album = new Album
                        {
                            ID = reader.GetInt32(0),
                            AlbumName = reader.GetString(1),
                            ArtistName = reader.GetString(2),
                            Year = reader.GetInt32(3),
                            ImageURL = reader.GetString(4),
                            Description = reader.GetString(5)
                        };

                        returnThese.Add(album);
                    }
                }
            }

            return returnThese;
        }

        internal int addOneAlbum(Album album)
        {
            // connect to the MySQL server
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                // define the SQL statement to insert a new album
                string query = "INSERT INTO album (ALBUM_TITLE, ARTIST, YEAR, IMAGE_NAME, DESCRIPTION) VALUES (@AlbumName, @ArtistName, @Year, @ImageURL, @Description)";

                MySqlCommand command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@AlbumName", album.AlbumName);
                command.Parameters.AddWithValue("@ArtistName", album.ArtistName);
                command.Parameters.AddWithValue("@Year", album.Year);
                command.Parameters.AddWithValue("@ImageURL", album.ImageURL);
                command.Parameters.AddWithValue("@Description", album.Description);

                int affectedRows = command.ExecuteNonQuery(); // returns the number of rows affected by the query

                connection.Close();

                return affectedRows; // if this returns 

            }
        }
    }
}
