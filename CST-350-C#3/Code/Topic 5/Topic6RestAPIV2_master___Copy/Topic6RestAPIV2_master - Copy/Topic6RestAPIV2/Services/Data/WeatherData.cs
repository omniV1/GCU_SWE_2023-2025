using MySql.Data.MySqlClient;
using System.Data.SqlClient;
using Topic6RestAPIV2.Models;

namespace Topic6RestAPIV2.Services.Data
{
    // Step 2.
    // Create a method that can be called and will populate the list
    public class WeatherData
    {
        // Class level variable
        string conn = @"datasource=localhost; port=3306; user=root; password=root; database=weather";

        /// <summary>
        /// Get All Products
        /// </summary>
        /// <returns></returns>
        public List<WeatherModel> GetAllWeather()
        {
            // Create a new instance of the Product Model
            List<WeatherModel> allWeather = new List<WeatherModel>();

            // Create the database query
            string sqlStatement = "SELECT * FROM weather_data";

            using (MySqlConnection connection = new MySqlConnection(conn))
            {
                MySqlCommand command = new MySqlCommand(sqlStatement, connection);

                try
                {
                    connection.Open();
                    MySqlDataReader reader = command.ExecuteReader();

                    while (reader.Read())
                    {
                        // Make sure to start with index 1 since 0 is this id
                        allWeather.Add(new WeatherModel((string)reader[1], (string)reader[2], (int)reader[3], (int)reader[4], (DateTime)reader[5]));
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
            // Return the list
            return allWeather;
        }

        public List<WeatherModel> GetWeatherSearch(string weather)
        {
            // Create a new instance of the product model
            List<WeatherModel> allWeather = new List<WeatherModel>();

            // Create the database query with weather being the placeholder
            string sqlStatement = "SELECT * FROM weather_data WHERE weather = @weather";

           
            using (MySqlConnection connection = new MySqlConnection(conn))
            {
                MySqlCommand command = new MySqlCommand(sqlStatement, connection);

                // Define the value of the weather placeholder
                command.Parameters.Add("@weather", MySqlDbType.VarChar, 10).Value = weather;


                try
                {
                    connection.Open();
                    MySqlDataReader reader = command.ExecuteReader();

                    while (reader.Read())
                    {
                        // Make sure to start with index 1 since 0 is this id
                        allWeather.Add(new WeatherModel((string)reader[1], (string)reader[2], (int)reader[3], (int)reader[4], (DateTime)reader[5]));
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
            // Return the list
            return allWeather;
        }
    }


        /// <summary>
        /// Populate the weather data list
        /// </summary>
        /// <returns></returns>
        //public List<WeatherModel> PopulateWeatherData()
        //{
        //    // Create a list that can be returned
        //    // We did this in several in class exercises
        //    // Create a new instance of the List containing weather models
        //    List<WeatherModel> weatherData = new List<WeatherModel>();

        //    // Create the list using hard coded data
        //    weatherData.Add(new WeatherModel("Phoenix", "Sunny", 78, 6, new DateOnly(2024, 02, 09)));
        //    weatherData.Add(new WeatherModel("Phoenix", "Cloudy", 56, 7, new DateOnly(2024, 02, 10)));
        //    weatherData.Add(new WeatherModel("Phoenix", "Rainy", 45, 20, new DateOnly(2024, 02, 11)));
        //    weatherData.Add(new WeatherModel("Phoenix", "Sunny", 85, 1, new DateOnly(2024, 02, 15)));

        //    // Return to Data Access Layer
        //    return weatherData;

        //}




    }
