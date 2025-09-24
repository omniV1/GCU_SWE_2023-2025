using Microsoft.AspNetCore.Mvc;
using RegisterAndLoginApp.Models;

namespace RegisterAndLoginApp.Controllers
{
    public class ButtonController : Controller
    {
        static List<ButtonModel> buttons = new List<ButtonModel>();

        Random random = new Random();

        // Constant for gridsize 
        const int GridSize = 25;

        public IActionResult Index()
        {
            // Empty the list  when page loads
            buttons = new List<ButtonModel>();

            // Generate new buttons 
            // Randomly chosen button color values
            for (int i = 0; i < GridSize; i++)
            {
                // Add to list of buttons
                buttons.Add(new ButtonModel(i, random.Next(4)));
            }
            // Send the button list to our index.cshtml
            return View("Index", buttons);
        }
    }
}
