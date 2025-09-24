using Milestone.Models.GameModels;
using Milestone.Services.Business.Interfaces;
using Milestone.Services.Data.Interfaces;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using Milestone.Services.Buisness;

namespace Milestone.Services.Business
{
    /// <summary>
    /// Service layer for managing Minesweeper game operations
    /// Acts as intermediary between the controller and data access layer
    /// </summary>
    public class GameService : IGameService
    {
        private readonly IGameDAO _gameDAO;
        private readonly ILogger<GameService> _logger;
        private readonly GameBoardManager _boardManager;

        /// <summary>
        /// Initializes a new instance of GameService with required dependencies
        /// </summary>
        /// <param name="gameDAO">Data access object for game operations</param>
        /// <param name="logger">Logger for tracking service operations</param>
        /// <param name="boardManager">Manager for game board operations</param>
        public GameService(
            IGameDAO gameDAO,
            ILogger<GameService> logger,
            GameBoardManager boardManager)
        {
            _gameDAO = gameDAO;
            _logger = logger;
            _boardManager = boardManager;
        }

        /// <summary>
        /// Creates a new game with specified difficulty and initializes the board
        /// </summary>
        /// <param name="difficulty">Difficulty level of the game</param>
        /// <returns>Initialized game board</returns>
        public Board CreateGame(string difficulty)
        {
            _logger.LogInformation($"Creating new game with difficulty: {difficulty}");
            var board = _gameDAO.CreateGame(difficulty);
            _boardManager.InitializeGrid(board);
            _boardManager.SetupLiveNeighbors(board);
            return board;
        }

        /// <summary>
        /// Retrieves an existing game by its ID
        /// </summary>
        /// <param name="gameId">Unique identifier of the game</param>
        /// <returns>The requested game board, or null if not found</returns>
        public Board GetGame(Guid gameId)
        {
            _logger.LogInformation($"Retrieving game with ID: {gameId}");
            return _gameDAO.GetGame(gameId);
        }

        /// <summary>
        /// Processes a cell reveal action and handles both normal reveals and chord reveals
        /// </summary>
        /// <param name="row">Row coordinate of the cell</param>
        /// <param name="col">Column coordinate of the cell</param>
        /// <param name="gameId">ID of the game being played</param>
        /// <returns>Response containing revealed cells and game state</returns>
        /// <exception cref="InvalidOperationException">Thrown when game is not found</exception>
        public CellUpdateResponse RevealCell(int row, int col, Guid gameId)
        {
            try
            {
                // Log the reveal attempt
                _logger.LogInformation($"Revealing cell at ({row}, {col}) for game {gameId}");

                // Get the current game state
                var game = _gameDAO.GetGame(gameId);
                if (game == null)
                {
                    throw new InvalidOperationException("Game not found");
                }

                // Get the cell to be revealed
                var cell = game.Grid[row, col];

                // Handle chord reveal if cell is already revealed and has adjacent mines
                if (cell.Visited && cell.LiveNeighbors > 0)
                {
                    return _boardManager.ProcessChordReveal(game, row, col);
                }

                // Process normal cell reveal
                var result = _boardManager.ProcessCellReveal(game, row, col);
                _logger.LogInformation($"Cell reveal result: {JsonSerializer.Serialize(result)}");
                return result;
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error revealing cell: {ex}");
                throw;
            }
        }
    }
}