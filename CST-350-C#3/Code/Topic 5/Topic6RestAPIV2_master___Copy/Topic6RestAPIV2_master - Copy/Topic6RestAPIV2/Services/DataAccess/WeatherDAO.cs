using System.Diagnostics;
using Topic6RestAPIV2.Models;
using Topic6RestAPIV2.Services.Data;

namespace Topic6RestAPIV2.Services.DataAccess
{
    public class WeatherDAO
    {

        // Instantiate the Data Layer so we can get data
        WeatherData sampleData = new WeatherData();

        // Step 3.
        /// <summary>
        /// Notice how this is an action using "Get"
        /// We want to get all weather data and pass
        /// to the Business Layer
        /// </summary>
        /// <returns></returns>
        public List<WeatherModel> GetAllWeatherData()
        {

            // Get the data and return it to the Businss Layer
            return sampleData.GetAllWeather();
        }

        public List<WeatherModel> GetWeatherSearch(string weather)
        {
            // Get the data and return it to the Buisness Layer
            return sampleData.GetWeatherSearch(weather);
        }



        }
    }
