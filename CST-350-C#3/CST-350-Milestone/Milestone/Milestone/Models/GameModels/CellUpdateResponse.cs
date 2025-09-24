namespace Milestone.Models.GameModels
{
    /// <summary>
    /// Represents the response after a cell reveal action in the game
    /// Contains game state and information about revealed cells
    /// </summary>
    public class CellUpdateResponse
    {
        /// <summary>
        /// Indicates if the game has ended
        /// </summary>
        public bool IsGameOver { get; set; }

        /// <summary>
        /// Indicates if the game ended in victory
        /// Set to true when all non-mine cells are revealed
        /// </summary>
        public bool IsVictory { get; set; }

        /// <summary>
        /// List of cells that were revealed during this update
        /// Includes cells revealed through flood fill
        /// </summary>
        public List<CellInfo> RevealedCells { get; set; }
    }
}