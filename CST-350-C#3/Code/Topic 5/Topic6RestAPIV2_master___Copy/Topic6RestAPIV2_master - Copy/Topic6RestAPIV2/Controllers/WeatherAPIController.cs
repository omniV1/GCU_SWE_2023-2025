// Owen Lindsey
// This work was done in class and suplemented with activity guides, and padlets. 
// CST-350 Activity 7
// 12/9/2024


using Microsoft.AspNetCore.Mvc;
using Topic6RestAPIV2.Models;
using Topic6RestAPIV2.Services.Business;

namespace Topic6RestAPIV2.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
   

    public class WeatherAPIController : ControllerBase
    {
        // Instantiate the Buisness Layer
        WeatherBAL weatherBusLayer = new WeatherBAL();

        // No route specified since this is the default
        // /api/weatherapi
        [HttpGet]
        public ActionResult<IEnumerable<WeatherModel>> Index()
        {
            // Get the list of Weather Data
            List<WeatherModel> allWeatherData = weatherBusLayer.GetAllWeatherData();

            // Get the average temp in the buisness layer
            // Put the results in a ViewBag to transport to view
            // ViewBag.averageTemp = weatherBusLayer.CalculateAverageTemp(allWeatherData);

            // Return the list
            return allWeatherData;
        }

        //HttpGet now defines the controller and Action method parameter
        [HttpGet("searchResults/{searchTerm}")]
        // Get /api/weatherapi/searchresults/xyz
        public ActionResult<IEnumerable<WeatherModel>> SearchResults(string searchTerm)
        {
            // Get the list of Weather Data
            List<WeatherModel> allWeatherData = weatherBusLayer.GetWeatherSearch(searchTerm);

            // Return the list
            return allWeatherData;
        }
    }
}
