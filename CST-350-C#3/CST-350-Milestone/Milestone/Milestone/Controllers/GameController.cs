using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Milestone.Models;
using Milestone.Filters;
using Milestone.Models.GameModels;
using Milestone.Services.Business.Interfaces;
using Milestone.Services.Data;

namespace Milestone.Controllers
{
    /// <summary>
    /// Controller responsible for handling Minesweeper game actions
    /// Requires an active session to access endpoints
    /// </summary>
    [SessionCheckFilter]
    public class GameController : Controller
    {
        private readonly IGameService _gameService;

        private readonly ILogger<GameController> _logger;

        private readonly SavedGameDAO _savedGameDAO;

        /// <summary>
        /// Initializes a new instance of GameController
        /// </summary>
        /// <param name="gameService">Service for managing game operations</param>
        public GameController(
             IGameService gameService,
             ILogger<GameController> logger,
             SavedGameDAO savedGameDAO)
        {
            _gameService = gameService;
            _logger = logger;
            _savedGameDAO = savedGameDAO;
        }


        /// <summary>
        /// Displays the initial game setup page
        /// </summary>
        /// <returns>View for starting a new game</returns>
        public IActionResult Index()
        {
            return View();
        }

        /// <summary>
        /// Processes a cell reveal action from the client
        /// </summary>
        /// <param name="request">Contains cell coordinates and game ID</param>
        /// <returns>JSON result containing revealed cells and game state</returns>
        [HttpPost]
        public IActionResult StartGame(string difficulty)
        {
            var board = _gameService.CreateGame(difficulty);
            return View("Game", board);
        }

        /// <summary>
        /// Processes a cell reveal action from the client
        /// </summary>
        /// <param name="request">Contains cell coordinates and game ID</param>
        /// <returns>JSON result containing revealed cells and game state</returns>
        [HttpPost]
        public IActionResult RevealCell([FromBody] CellRevealRequest request)
        {
            try
            {
                _logger.LogInformation($"Received cell reveal request: Row={request.Row}, Col={request.Col}, GameId={request.GameId}");

                if (request == null)
                {
                    return BadRequest("Invalid request data");
                }

                var result = _gameService.RevealCell(request.Row, request.Col, request.GameId);
                return Json(new
                {
                    revealedCells = result.RevealedCells,
                    isGameOver = result.IsGameOver,
                    isVictory = result.IsVictory
                });
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error in RevealCell: {ex.Message}");
                return BadRequest(ex.Message);
            }
        }

        /// <summary>
        /// Displays a win or loss message 
        /// </summary>
        /// <param name="gameId"></param>
        /// <param name="isVictory"></param>
        /// <param name="score"></param>
        /// <returns></returns>
        /// <summary>
        /// Displays a win or loss message 
        /// </summary>
        [HttpPost("/Game/EndGame")]
        [HttpGet("/Game/EndGame")]
        public IActionResult EndGame([FromQuery] Guid gameId, [FromQuery] bool isVictory, [FromQuery] int score, [FromQuery] string time)
        {
            try
            {
                _logger.LogInformation($"EndGame called - Method: {Request.Method}");
                _logger.LogInformation($"Parameters - GameId: {gameId}, IsVictory: {isVictory}, Score: {score}, Time: {time}");

                // Validate game ID
                if (gameId == Guid.Empty)
                {
                    _logger.LogError("Invalid GameId provided");
                    return BadRequest("Invalid GameId");
                }

                var game = _gameService.GetGame(gameId);
                _logger.LogInformation($"Game lookup result: {(game != null ? "Found" : "Not Found")}");

                if (game == null)
                {
                    _logger.LogError($"Game not found for ID: {gameId}");
                    return NotFound($"Game {gameId} not found");
                }

                // Pass data to view
                ViewBag.FinalTime = time;
                _logger.LogInformation($"Rendering view for victory: {isVictory}");

                // Double check view exists
                var viewName = isVictory ? "Win" : "Loss";
                _logger.LogInformation($"Attempting to render view: {viewName}");

                try
                {
                    return View(viewName, game);
                }
                catch (Exception viewEx)
                {
                    _logger.LogError($"Error rendering view {viewName}: {viewEx.Message}");
                    throw;
                }
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error in EndGame: {ex.Message}");
                _logger.LogError($"Stack trace: {ex.StackTrace}");
                throw; // Let the error handler catch this so we can see the full error
            }
        }

        private UserModel GetCurrentUser()
        {
            try
            {
                var userJson = HttpContext.Session.GetString("User");
                if (string.IsNullOrEmpty(userJson))
                {
                    _logger.LogError("No user found in session");
                    throw new InvalidOperationException("User not found in session");
                }

                var user = ServiceStack.Text.JsonSerializer.DeserializeFromString<UserModel>(userJson);
                _logger.LogInformation($"Retrieved user from session - ID: {user.Id}, Username: {user.Username}");

                if (user.Id == 0) // Add check for invalid ID
                {
                    _logger.LogError($"Invalid user ID: {user.Id}");
                    throw new InvalidOperationException("Invalid user ID");
                }

                return user;
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error getting current user: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Model for cell reveal request data from client
        /// </summary>
        public class CellRevealRequest
        {
            public int Row { get; set; }
            public int Col { get; set; }
            public Guid GameId { get; set; }
        }

        [HttpPost]
        public async Task<IActionResult> SaveGame()
        {
            try
            {
                _logger.LogInformation("SaveGame method called - Starting save process");

                // Detailed session check
                var userJson = HttpContext.Session.GetString("User");
                _logger.LogInformation($"Session data found: {!string.IsNullOrEmpty(userJson)}");
                _logger.LogInformation($"Raw session data: {userJson}");

                if (string.IsNullOrEmpty(userJson))
                {
                    _logger.LogError("No user session found");
                    return BadRequest("No user session found - please log in again");
                }

                // Deserialize and validate user
                var user = ServiceStack.Text.JsonSerializer.DeserializeFromString<UserModel>(userJson);
                _logger.LogInformation($"Deserialized user data - ID: {user?.Id}, Username: {user?.Username}");

                if (user == null || user.Id <= 0)
                {
                    _logger.LogError($"Invalid user data - User null: {user == null}, User ID: {user?.Id}");
                    return BadRequest("Invalid user data");
                }

                // Log form data
                var formKeys = Request.Form.Keys;
                _logger.LogInformation($"Form keys present: {string.Join(", ", formKeys)}");
                var gameIdString = Request.Form["gameId"].ToString();
                _logger.LogInformation($"Received gameId: {gameIdString}");

                if (!Guid.TryParse(gameIdString, out Guid gameId))
                {
                    _logger.LogError($"Failed to parse game ID: {gameIdString}");
                    return BadRequest("Invalid game ID format");
                }

                var board = _gameService.GetGame(gameId);
                if (board == null)
                {
                    _logger.LogError($"Game board not found for ID: {gameId}");
                    return BadRequest("Game not found");
                }

                _logger.LogInformation($"Retrieved game board - GameId: {board.GameId}, Size: {board.Size}");
                _logger.LogInformation($"Attempting to save game for User ID: {user.Id}");

                var savedGameId = await _savedGameDAO.SaveGame(user.Id, board, user);
                _logger.LogInformation($"Game saved successfully - Saved game ID: {savedGameId}");

                return Json(new { success = true, gameId = savedGameId });
            }
            catch (Exception ex)
            {
                _logger.LogError($"Save game error - Message: {ex.Message}");
                _logger.LogError($"Stack trace: {ex.StackTrace}");
                return BadRequest($"Failed to save game: {ex.Message}");
            }
        }



        [HttpGet]
        public async Task<IActionResult> LoadGame(int id)
        {
            try
            {
                var savedGame = await _savedGameDAO.GetSavedGame(id);
                if (savedGame == null)
                {
                    return NotFound();
                }

                var (board, user) = SavedGame.DeserializeGameState(savedGame.GameData);

                // Add the board state to TempData to be accessed by JavaScript
                TempData["LoadedGameState"] = true;
                TempData["RevealedCells"] = ServiceStack.Text.JsonSerializer.SerializeToString(
                    board.Grid.Cast<Cell>()
                        .Where(c => c.Visited)
                        .Select(c => new
                        {
                            row = c.Row,
                            column = c.Column,
                            isMine = c.Live,
                            neighborCount = c.LiveNeighbors,
                            isFlagged = c.Flagged
                        })
                );

                return View("Game", board);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error loading game: {ex.Message}");
                return RedirectToAction("Index", "Game");
            }
        }

        // Add this class inside your GameController class
        public class SaveGameRequest
        {
            public Guid GameId { get; set; }
        }
    }
}