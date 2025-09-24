using Topic6RestAPIV2.Models;
using Topic6RestAPIV2.Services.DataAccess;

namespace Topic6RestAPIV2.Services.Business
{
    public class WeatherBAL
    {
        // Step 4:
        // We know from the requirements there are three items
        // that need to be implemented in the Business Layer
        // 1. Convert Date format
        // 2. Cal average temp
        // 3. Get the list of data

        /// <summary>
        /// Request the data from the Data Access Layer
        /// and then return it to the Controller
        /// </summary>
        /// <returns></returns>
        public List<WeatherModel> GetAllWeatherData()
        {
            // Get the data from the Data Access Layer and
            // pass it back to the controller.
            // Alter the date to the correct format.
            WeatherDAO getData = new WeatherDAO();
            // Get the data and return it back up
            List<WeatherModel> allWeatherData = getData.GetAllWeatherData();
            // Iterate through the list and make sure the date is in the proper format.
            for (int i = 0; i < allWeatherData.Count; i++)
            {
                allWeatherData[i].ConvertedDate = allWeatherData[i].DayOfWeather.ToString("MM/dd/yyyy");
            }
            return allWeatherData;
        }

        /// <summary>
        /// Method to calculate the average temp and return it
        /// </summary>
        /// <param name="listofData"></param>
        /// <returns></returns>
        public int CalculateAverageTemp(List<WeatherModel> listofData)
        {
            // Declare and initialize the sum variable
            int tempSum = 0;

            // Iterate through the list and add up the temp
            foreach (WeatherModel weather in listofData)
            {
                tempSum += weather.Temp;
            }

            // Get the average and return it.
            return tempSum / listofData.Count;




        }

        public List<WeatherModel> GetWeatherSearch(string weather)
        {
            WeatherDAO getData = new WeatherDAO();

            // Get data and return it to the Buisness Layer
            return getData.GetWeatherSearch(weather);
        }




    }
}
