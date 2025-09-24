using System.Data.SqlClient;
using Milestone.Models;
using Milestone.Models.GameModels;

namespace Milestone.Services.Data
{
    /// <summary>
    /// Data Access Object for managing saved games in the database.
    /// Handles CRUD operations for game states including saving, retrieving, and deleting saved games.
    /// </summary>
    public class SavedGameDAO
    {
        private static readonly string conn = @"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=UserAuth;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False";
        private readonly ILogger<SavedGameDAO> _logger;

        /// <summary>
        /// Initializes a new instance of the SavedGameDAO class.
        /// </summary>
        /// <param name="logger">Logger instance for recording operational logs</param>
        public SavedGameDAO(ILogger<SavedGameDAO> logger)
        {
            _logger = logger;
        }

        /// <summary>
        /// Saves a game state to the database for a specific user.
        /// </summary>
        /// <param name="userId">The ID of the user saving the game</param>
        /// <param name="board">The current game board state</param>
        /// <param name="user">The user model associated with the save</param>
        /// <returns>The ID of the newly saved game</returns>
        /// <exception cref="InvalidOperationException">Thrown when the specified user doesn't exist</exception>
        /// <exception cref="Exception">Thrown when there's an error saving the game</exception>
        public async Task<int> SaveGame(int userId, Board board, UserModel user)
        {
            try
            {
                using var connection = new SqlConnection(conn);
                await connection.OpenAsync();

                var verifyUserQuery = "SELECT COUNT(1) FROM UserAccount WHERE Id = @UserId";
                using var verifyCommand = new SqlCommand(verifyUserQuery, connection);
                verifyCommand.Parameters.AddWithValue("@UserId", userId);

                var userExists = (int)await verifyCommand.ExecuteScalarAsync() > 0;
                if (!userExists)
                {
                    throw new InvalidOperationException($"User with ID {userId} does not exist.");
                }

                var gameData = SavedGame.SerializeGameState(board, user);

                var query = @"INSERT INTO Games (UserId, DateSaved, GameData) 
                            VALUES (@UserId, @DateSaved, @GameData);
                            SELECT SCOPE_IDENTITY();";

                using var command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@UserId", userId);
                command.Parameters.AddWithValue("@DateSaved", DateTime.UtcNow);
                command.Parameters.AddWithValue("@GameData", gameData);

                var result = await command.ExecuteScalarAsync();
                return Convert.ToInt32(result);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error saving game: {ex.Message}");
                throw new Exception($"Error saving game: {ex.Message}", ex);
            }
        }

        /// <summary>
        /// Retrieves all saved games for a specific user.
        /// </summary>
        /// <param name="userId">The ID of the user whose games to retrieve</param>
        /// <returns>A list of saved games ordered by save date descending</returns>
        /// <exception cref="Exception">Thrown when there's an error retrieving the saved games</exception>
        public async Task<List<SavedGame>> GetSavedGames(int userId)
        {
            var games = new List<SavedGame>();

            try
            {
                using var connection = new SqlConnection(conn);
                await connection.OpenAsync();

                var query = @"SELECT Id, UserId, DateSaved, GameData 
                            FROM Games 
                            WHERE UserId = @UserId 
                            ORDER BY DateSaved DESC";

                using var command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@UserId", userId);

                using var reader = await command.ExecuteReaderAsync();
                while (await reader.ReadAsync())
                {
                    games.Add(new SavedGame
                    {
                        Id = reader.GetInt32(0),
                        UserId = reader.GetInt32(1),
                        DateSaved = reader.GetDateTime(2),
                        GameData = reader.GetString(3)
                    });
                }
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error getting saved games: {ex.Message}");
                throw;
            }

            return games;
        }

        /// <summary>
        /// Retrieves a specific saved game by its ID.
        /// </summary>
        /// <param name="gameId">The ID of the saved game to retrieve</param>
        /// <returns>The saved game if found, null otherwise</returns>
        /// <exception cref="Exception">Thrown when there's an error retrieving the saved game</exception>
        public async Task<SavedGame> GetSavedGame(int gameId)
        {
            try
            {
                using var connection = new SqlConnection(conn);
                await connection.OpenAsync();

                var query = @"SELECT Id, UserId, DateSaved, GameData 
                            FROM Games 
                            WHERE Id = @Id";

                using var command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@Id", gameId);

                using var reader = await command.ExecuteReaderAsync();
                if (await reader.ReadAsync())
                {
                    return new SavedGame
                    {
                        Id = reader.GetInt32(0),
                        UserId = reader.GetInt32(1),
                        DateSaved = reader.GetDateTime(2),
                        GameData = reader.GetString(3)
                    };
                }

                return null;
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error getting saved game: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Deletes a specific saved game from the database.
        /// </summary>
        /// <param name="gameId">The ID of the saved game to delete</param>
        /// <exception cref="Exception">Thrown when there's an error deleting the saved game</exception>
        public async Task DeleteSavedGame(int gameId)
        {
            try
            {
                using var connection = new SqlConnection(conn);
                await connection.OpenAsync();

                var query = "DELETE FROM Games WHERE Id = @Id";

                using var command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@Id", gameId);

                await command.ExecuteNonQueryAsync();
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error deleting saved game: {ex.Message}");
                throw;
            }
        }
    }
}