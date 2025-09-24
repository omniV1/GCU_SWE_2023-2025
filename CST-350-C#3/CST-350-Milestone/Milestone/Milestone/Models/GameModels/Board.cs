using System.Dynamic;

namespace Milestone.Models.GameModels
{
    /// <summary>
    /// Represents the game board data structure
    /// Contains the complete state of a Minesweeper game
    /// </summary>
    public class Board
    {
        /// <summary>
        /// Size of the game board (creates a Size x Size grid)
        /// </summary>
        public int Size { get; set; }

        /// <summary>
        /// Two-dimensional array representing the game grid
        /// Each cell contains its own state information
        /// </summary>
        public Cell[,] Grid { get; set; }

        /// <summary>
        /// Difficulty level affecting mine density (0.1 = 10% mines)
        /// </summary>
        public float Difficulty { get; set; }

        /// <summary>
        /// Unique identifier for this game instance
        /// </summary>
        public Guid GameId { get; set; }

        /// <summary>
        /// Timestamp when the game was created
        /// </summary>
        public DateTime StartTime { get; set; }

        /// <summary>
        /// Indicates if the game has ended (either victory or hitting a mine)
        /// </summary>
        public bool IsGameOver { get; set; }

        /// <summary>
        /// Indicates if the game ended in victory (all non-mine cells revealed)
        /// </summary>
        public bool IsVictory { get; set; }

        /// <summary>
        /// Constant indicating a cell contains a mine
        /// </summary>
        public const int BombIndicator = 9;
        /// <summary>
        /// Creates a new game board with specified dimensions
        /// </summary>
        /// <param name="size">The dimensions of the board (default 10x10)</param>
        public Board(int size = 10)
        {
            Size = size;
            Grid = new Cell[size, size];
            GameId = Guid.NewGuid();
            StartTime = DateTime.Now;
        }
    }
}