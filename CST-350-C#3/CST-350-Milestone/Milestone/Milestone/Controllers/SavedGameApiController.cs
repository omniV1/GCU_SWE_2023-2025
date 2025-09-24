using Microsoft.AspNetCore.Mvc;
using Milestone.Models.GameModels;
using Milestone.Services.Data;

namespace Milestone.Controllers
{
    /// <summary>
    /// API Controller for managing saved games through RESTful endpoints.
    /// Provides functionality for retrieving and deleting saved games.
    /// </summary>
    [Route("api")]
    [ApiController]
    public class SavedGamesApiController : ControllerBase
    {
        private readonly SavedGameDAO _savedGameDAO;
        private readonly ILogger<SavedGamesApiController> _logger;

        /// <summary>
        /// Initializes a new instance of the SavedGamesApiController.
        /// </summary>
        /// <param name="savedGameDAO">Data access object for saved games operations</param>
        /// <param name="logger">Logger for recording API operations and errors</param>
        public SavedGamesApiController(SavedGameDAO savedGameDAO, ILogger<SavedGamesApiController> logger)
        {
            _savedGameDAO = savedGameDAO;
            _logger = logger;
        }

        /// <summary>
        /// Retrieves all saved games for demo user (ID: 1).
        /// GET: api/showSavedGames
        /// </summary>
        /// <returns>
        /// - 200 OK with list of saved games if successful
        /// - 500 Internal Server Error if operation fails
        /// </returns>
        [HttpGet("showSavedGames")]
        public async Task<ActionResult<IEnumerable<SavedGame>>> GetSavedGames()
        {
            try
            {
                var games = await _savedGameDAO.GetSavedGames(1); // Default to user 1 for demo
                return Ok(games);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error getting saved games: {ex.Message}");
                return StatusCode(500, "Internal server error");
            }
        }

        /// <summary>
        /// Retrieves a specific saved game by its ID.
        /// GET: api/showSavedGames/5
        /// </summary>
        /// <param name="id">The ID of the saved game to retrieve</param>
        /// <returns>
        /// - 200 OK with saved game if found
        /// - 404 Not Found if game doesn't exist
        /// - 500 Internal Server Error if operation fails
        /// </returns>
        [HttpGet("showSavedGames/{id}")]
        public async Task<ActionResult<SavedGame>> GetSavedGame(int id)
        {
            try
            {
                var game = await _savedGameDAO.GetSavedGame(id);
                if (game == null)
                {
                    return NotFound();
                }
                return Ok(game);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error getting saved game {id}: {ex.Message}");
                return StatusCode(500, "Internal server error");
            }
        }

        /// <summary>
        /// Deletes a specific saved game by its ID.
        /// DELETE: api/deleteOneGame/5
        /// </summary>
        /// <param name="id">The ID of the saved game to delete</param>
        /// <returns>
        /// - 200 OK if deletion successful
        /// - 500 Internal Server Error if deletion fails
        /// </returns>
        [HttpDelete("deleteOneGame/{id}")]
        public async Task<IActionResult> DeleteSavedGame(int id)
        {
            try
            {
                await _savedGameDAO.DeleteSavedGame(id);
                return Ok();
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error deleting game {id}: {ex.Message}");
                return StatusCode(500, "Internal server error");
            }
        }
    }
}