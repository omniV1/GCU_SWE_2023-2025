namespace Milestone.Models.GameModels
{
    /// <summary>
    /// Represents a single cell in the Minesweeper game board
    /// Contains all state information for a cell during gameplay
    /// </summary>
    public class Cell
    {
        /// <summary>
        /// Row position of the cell in the grid
        /// </summary>
        public int Row { get; set; }

        /// <summary>
        /// Column position of the cell in the grid
        /// </summary>
        public int Column { get; set; }

        /// <summary>
        /// Indicates if the cell has been revealed during gameplay
        /// </summary>
        public bool Visited { get; set; }

        /// <summary>
        /// Indicates if the cell contains a mine
        /// </summary>
        public bool Live { get; set; }

        /// <summary>
        /// Number of adjacent cells containing mines
        /// </summary>
        public int LiveNeighbors { get; set; }

        /// <summary>
        /// Indicates if the player has flagged this cell as potentially containing a mine
        /// </summary>
        public bool Flagged { get; set; }

        // Web-specific properties with more intuitive names
        /// <summary>
        /// Web-friendly alias for Visited property
        /// </summary>
        public bool IsRevealed => Visited;

        /// <summary>
        /// Web-friendly alias for Live property
        /// </summary>
        public bool IsMine => Live;

        /// <summary>
        /// Web-friendly alias for LiveNeighbors property
        /// </summary>
        public int AdjacentMines => LiveNeighbors;
    }
}