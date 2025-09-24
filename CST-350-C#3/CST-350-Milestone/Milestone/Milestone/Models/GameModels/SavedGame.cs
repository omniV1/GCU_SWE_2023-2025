using System.Text.Json;

namespace Milestone.Models.GameModels
{
    public class SavedGameCellState
    {
        public int Row { get; set; }
        public int Column { get; set; }
        public bool IsRevealed { get; set; }
        public bool IsMine { get; set; }
        public bool IsFlagged { get; set; }
        public int NeighborCount { get; set; }
    }

    public class SavedGame
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public DateTime DateSaved { get; set; }
        public string GameData { get; set; }

        public static string SerializeGameState(Board board, UserModel user)
        {
            var cellStates = new List<SavedGameCellState>();

            // Capture state of each cell
            for (int i = 0; i < board.Size; i++)
            {
                for (int j = 0; j < board.Size; j++)
                {
                    var cell = board.Grid[i, j];
                    cellStates.Add(new SavedGameCellState
                    {
                        Row = i,
                        Column = j,
                        IsRevealed = cell.Visited,
                        IsMine = cell.Live,
                        IsFlagged = cell.Flagged,
                        NeighborCount = cell.LiveNeighbors
                    });
                }
            }

            var gameState = new
            {
                board.GameId,
                board.Size,
                board.Difficulty,
                board.StartTime,
                board.IsGameOver,
                board.IsVictory,
                CellStates = cellStates,
                User = new
                {
                    user.Id,
                    user.Username
                }
            };

            return JsonSerializer.Serialize(gameState);
        }

        public static (Board Board, UserModel User) DeserializeGameState(string gameData)
        {
            var state = JsonSerializer.Deserialize<dynamic>(gameData);

            // Create new board with saved properties
            var board = new Board((int)state.Size)
            {
                GameId = Guid.Parse(state.GameId.ToString()),
                Difficulty = (float)state.Difficulty,
                StartTime = DateTime.Parse(state.StartTime.ToString()),
                IsGameOver = (bool)state.IsGameOver,
                IsVictory = (bool)state.IsVictory
            };

            // Reconstruct cell states
            foreach (var cellState in state.CellStates.EnumerateArray())
            {
                var row = (int)cellState.Row;
                var col = (int)cellState.Column;
                board.Grid[row, col] = new Cell
                {
                    Row = row,
                    Column = col,
                    Visited = (bool)cellState.IsRevealed,
                    Live = (bool)cellState.IsMine,
                    LiveNeighbors = (int)cellState.NeighborCount,
                    Flagged = (bool)cellState.IsFlagged
                };
            }

            // Reconstruct user
            var user = new UserModel
            {
                Id = (int)state.User.Id,
                Username = state.User.Username.ToString()
            };

            return (board, user);
        }
    }
}