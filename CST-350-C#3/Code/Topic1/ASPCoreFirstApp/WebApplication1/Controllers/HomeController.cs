using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        /// <summary>
        /// This is the constructor
        /// </summary>
        /// <param name="logger"></param>
        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public IActionResult Index()
        {
            return View();
        }
        //Privacy page
        public IActionResult Privacy()
        {
            // use dictionary object provided by ASP.NET MVC
            // passes data from controller to view
            ViewData["Message"] = "This is going to be a great day.";
            return View();
        }
        //About me page
        public IActionResult About()
        {
            ViewData["Message"] = "This is going to be a great day.";
            return View("AboutMe");
        }
        //contacts page
        public IActionResult Contact()
        {
           
            return View("ContactUs");
        }
        //schedule page
        public IActionResult Schedule()
        {
           
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
