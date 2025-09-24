using Microsoft.AspNetCore.Mvc;
using Milestone.Models.GameModels;
using Milestone.Services.Data;
using Milestone.Filters;
using Milestone.Models;

namespace Milestone.Controllers
{
    /// <summary>
    /// Controller responsible for managing saved game operations.
    /// Requires an active session to access (enforced by SessionCheckFilter).
    /// </summary>
    [SessionCheckFilter]
    public class SavedGamesController : Controller
    {
        private readonly SavedGameDAO _savedGameDAO;
        private readonly ILogger<SavedGamesController> _logger;

        /// <summary>
        /// Initializes a new instance of the SavedGamesController.
        /// </summary>
        /// <param name="savedGameDAO">Data access object for saved games operations</param>
        /// <param name="logger">Logger for recording controller actions and errors</param>
        public SavedGamesController(SavedGameDAO savedGameDAO, ILogger<SavedGamesController> logger)
        {
            _savedGameDAO = savedGameDAO;
            _logger = logger;
        }

        /// <summary>
        /// Displays a list of all saved games for the currently logged-in user.
        /// </summary>
        /// <returns>
        /// - View containing list of saved games if successful
        /// - Redirects to Error page if an exception occurs
        /// </returns>
        public async Task<IActionResult> Index()
        {
            try
            {
                var userJson = HttpContext.Session.GetString("User");
                var userData = ServiceStack.Text.JsonSerializer.DeserializeFromString<UserModel>(userJson);
                var games = await _savedGameDAO.GetSavedGames(userData.Id);
                return View(games);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error loading saved games: {ex.Message}");
                return RedirectToAction("Error", "Home");
            }
        }

        /// <summary>
        /// Deletes a specific saved game.
        /// </summary>
        /// <param name="id">The ID of the saved game to delete</param>
        /// <returns>
        /// - Redirects to Index with success message if deletion successful
        /// - Redirects to Index with error message if deletion fails
        /// </returns>
        [HttpPost]
        public async Task<IActionResult> Delete(int id)
        {
            try
            {
                await _savedGameDAO.DeleteSavedGame(id);
                TempData["Message"] = "Game deleted successfully.";
                return RedirectToAction(nameof(Index));
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error deleting saved game: {ex.Message}");
                TempData["Error"] = "Error deleting game.";
                return RedirectToAction(nameof(Index));
            }
        }
    }
}