using Microsoft.AspNetCore.Mvc;
using System.Drawing;
using System.Security.Cryptography.X509Certificates;

namespace ASPcoreExample.Controllers
{
    public class ProductsController : Controller
    {
        public IActionResult Index()
        {
            return View();

        }
       
        // Refactor to display an HTML view       
        public IActionResult Message()
        {

            return View(); 

        }

        //Passing params info from URL to the controller
       
        public IActionResult Details(string name, int room = 445)
        {
            // The optional param feature shows that room should default to 445 if the value is not passed into the method.
            ViewData["Name"] = name; 
            ViewData["Room"] = room;
            // Return this data to the Message csHTML view
            return View("Message"); 
        }

        //Return JSON data : Owen Lindsey
        public IActionResult Data(int orderNumber, decimal price, int quantity)
        {
            return Json(new {orderNumber, price, quantity });
        }

    }
}
