// Owen Lindsey
// This work was done in class and suplemented with activity guides, and padlets. 
// CST-350 Activity 7
// 12/9/2024


using Microsoft.AspNetCore.Mvc;
using Topic6RestAPIV2.Models;
using Topic6RestAPIV2.Services.Business;

namespace Topic6RestAPIV2.Controllers
{
    public class WeatherController : Controller
    {
        public IActionResult Index()
        {
            // Instantiate the Business Layer
            WeatherBAL weatherBusLayer = new WeatherBAL();

            // Get the list of Weather Data
            List<WeatherModel> allWeatherData = weatherBusLayer.GetAllWeatherData();

            // Get the average temp in the businss layer.
            // Put the results in a ViewBag to transport to view
            ViewBag.averageTemp = weatherBusLayer.CalculateAverageTemp(allWeatherData);

            // Return the list
            return View(allWeatherData);
        }
    }
}
