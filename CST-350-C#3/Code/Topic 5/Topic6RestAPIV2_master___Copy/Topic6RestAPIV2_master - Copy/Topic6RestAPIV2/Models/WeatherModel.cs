namespace Topic6RestAPIV2.Models
{
    // Step 1
    // Class Level Properties
    public class WeatherModel
    {
        public string? City { get; set; }
        public string? Weather { get; set; }
        public int Temp { get; set; }
        public int Wind { get; set; }
        // Avoid using "Date" here as the property name
        // since this is already a keyword
        public DateTime DayOfWeather { get; set; }
        public string? ConvertedDate { get; set; }

        /// <summary>
        /// Parameterized Constructor
        /// </summary>
        /// <param name="city"></param>
        /// <param name="weather"></param>
        /// <param name="temp"></param>
        /// <param name="wind"></param>
        /// <param name="dayOfWeather"></param>
        public WeatherModel(string? city, string? weather, int temp, int wind, DateTime dayOfWeather)
        {
            City = city;
            Weather = weather;
            Temp = temp;
            Wind = wind;
            DayOfWeather = dayOfWeather;
        }
    }
}
