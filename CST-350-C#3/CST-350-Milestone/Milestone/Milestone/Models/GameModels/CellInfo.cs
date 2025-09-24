namespace Milestone.Models.GameModels
{
    /// <summary>
    /// Represents information about a cell on the Minesweeper board
    /// Used to communicate cell state changes to the client
    /// </summary>
    public class CellInfo
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
        /// Indicates if the cell has been revealed to the player
        /// </summary>
        public bool IsRevealed { get; set; }

        /// <summary>
        /// Indicates if the cell contains a mine
        /// </summary>
        public bool IsMine { get; set; }

        /// <summary>
        /// Number of adjacent cells containing mines
        /// Zero indicates no adjacent mines
        /// </summary>
        public int NeighborCount { get; set; }
    }
}