using Milestone.Models.GameModels;

namespace Milestone.Services.Data.Interfaces
{
    /// <summary>
    /// Interface for game data access operations
    /// Defines contract for managing game state persistence
    /// </summary>
    public interface IGameDAO
    {
        /// <summary>
        /// Creates a new game with specified difficulty level
        /// </summary>
        /// <param name="difficulty">Difficulty level of the game</param>
        /// <returns>Initialized game board</returns>
        Board CreateGame(string difficulty);

        /// <summary>
        /// Processes a cell reveal action for a specific game
        /// </summary>
        /// <param name="row">Row coordinate of the cell</param>
        /// <param name="col">Column coordinate of the cell</param>
        /// <param name="gameId">ID of the game being played</param>
        /// <returns>Response containing revealed cells and game state</returns>
        /// <exception cref="InvalidOperationException">Thrown when game is not found</exception>
        CellUpdateResponse RevealCell(int row, int col, Guid gameId);

        /// <summary>
        /// Retrieves an existing game by its ID
        /// </summary>
        /// <param name="gameId">Unique identifier of the game</param>
        /// <returns>The requested game board, or null if not found</returns>
        Board GetGame(Guid gameId);
    }
}