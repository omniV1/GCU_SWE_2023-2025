using Milestone.Models.GameModels;
using Milestone.Services.Data.Interfaces;

public class GameDAO : IGameDAO
{
    private readonly GameBoardManager _boardManager;
    private readonly Dictionary<Guid, Board> _games;
    private readonly ILogger<GameDAO> _logger;


    /// <summary>
    /// Initializes a new instance of GameDAO with board manager dependency
    /// </summary>
    /// <param name="boardManager">Manager for game board operations</param>
    public GameDAO(GameBoardManager boardManager, ILogger<GameDAO> logger)
    {
        _boardManager = boardManager;
        _logger = logger;
        _games = new Dictionary<Guid, Board>();
    }

    /// <summary>
    /// Creates and stores a new game with specified difficulty
    /// </summary>
    /// <param name="difficulty">Difficulty level string (easy, medium, hard)</param>
    /// <returns>New game board instance</returns>
    public Board CreateGame(string difficulty)
    {
        var board = new Board();
        board.Difficulty = ParseDifficulty(difficulty);
        _boardManager.InitializeGrid(board);
        _boardManager.SetupLiveNeighbors(board);

        _games[board.GameId] = board;
        _logger.LogInformation($"Created new game. ID: {board.GameId}, Total games: {_games.Count}");

        return board;
    }

    /// <summary>
    /// Retrieves a game by its ID from the in-memory storage
    /// </summary>
    /// <param name="gameId">Unique identifier of the game</param>
    /// <returns>The requested game board, or null if not found</returns>
    public Board GetGame(Guid gameId)
    {
        _logger.LogInformation($"Attempting to get game {gameId}. Available games: {string.Join(", ", _games.Keys)}");
        if (_games.TryGetValue(gameId, out var board))
        {
            return board;
        }

        _logger.LogWarning($"Game {gameId} not found!");
        return null;
    }


    /// <summary>
    /// Processes a cell reveal action on the stored game
    /// </summary>
    /// <param name="row">Row coordinate of the cell</param>
    /// <param name="col">Column coordinate of the cell</param>
    /// <param name="gameId">ID of the game being played</param>
    /// <returns>Response containing revealed cells and game state</returns>
    /// <exception cref="InvalidOperationException">Thrown when game is not found</exception>
    public CellUpdateResponse RevealCell(int row, int col, Guid gameId)
    {
        _logger.LogInformation($"Revealing cell ({row},{col}) for game {gameId}");
        var board = GetGame(gameId);
        if (board == null)
        {
            throw new InvalidOperationException($"Game {gameId} not found");
        }
        return _boardManager.ProcessCellReveal(board, row, col);
    }

    /// <summary>
    /// Converts difficulty string to corresponding mine density percentage
    /// </summary>
    /// <param name="difficulty">Difficulty level (easy, medium, hard)</param>
    /// <returns>Float value representing mine density</returns>
    private float ParseDifficulty(string difficulty)
    {
        return difficulty?.ToLower() switch
        {
            "easy" => 0.1f,    // 10% mines
            "medium" => 0.15f, // 15% mines
            "hard" => 0.2f,    // 20% mines
            _ => 0.15f         // Default to medium
        };
    }
}