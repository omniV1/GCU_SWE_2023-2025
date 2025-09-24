using Microsoft.AspNetCore.Mvc;
using ActivityRightClick.Models;

// Owen Lindsey
// This work was done in class and suplemented with activity guides, and padlets. 
// CST-350 Activity 7
// 12/9/2024

namespace ActivityRightClick.Controllers

{
    public class ButtonController : Controller
    { 
        // Static class scoped member variables named 'buttons'
        // Static means the 'buttons' object we create 
        // Will have the same value through out all instances of the object
        // Create a list of buttons
        static List<ButtonModel> buttons = new List<ButtonModel>(); 
    
        // We will use the random number generator to select the button image
        Random random = new Random();

        // Constant for the GridSize
        const int GridSize = 25; 

        public IActionResult Index()
        {
            // Empty the list when page loads
            buttons = new List<ButtonModel>();

            // Generate new buttons
            // Randomly chosen button color values
            for (int i = 0; i < GridSize; i++)
            {
                // Add to our list of buttons
                buttons.Add(new ButtonModel(i, random.Next(4)));
            }
            // Send the button list to Index.cshtml page
            return View("Index", buttons);
        }

        // Action method to process right mouse clicks
        public IActionResult RightClickShowOneButton(int buttonNumber)
        {
            // Right click always turn the button to whatever color is in index 0
            buttons.ElementAt(buttonNumber).ButtonState = 0;
            return PartialView("ShowOneButton", buttons.ElementAt(buttonNumber));
        }

        public IActionResult ShowOneButton(int buttonNumber)
        {
            // add one to the button state
            // if > 4 -> 0
            buttons.ElementAt(buttonNumber).ButtonState = (buttons.ElementAt(buttonNumber).ButtonState + 1) % 4;
            return PartialView("ShowOneButton", buttons.ElementAt(buttonNumber));
        }

        public IActionResult HandleButtonClick(string buttonNumber)
        {
            if (int.TryParse(buttonNumber, out int buttonValue))
            {
                buttons.ElementAt(buttonValue).ButtonState = (buttons.ElementAt(buttonValue).ButtonState + 1) % 4;
            }
            return View("Index", buttons);
        }
    }
}