using System;
using System.Diagnostics;

namespace MinesweeperGui.BusinessLayer
{
    /// <summary>
    /// Represents a single cell on a game board.
    /// </summary>
    public class Cell
    {
        // Properties of the cell, with default values
        public int Row { get; set; } = -1;
        public int Column { get; set; } = -1;
        public bool Visited { get; set; } = false;
        public bool Live { get; set; } = false;
        public int LiveNeighbors { get; set; } = 0;
        public bool Flagged { get; set; } = false; // Indicates if the cell is flagged


        /// <summary>
        /// Constructor for the Cell class.
        /// </summary>
        public Cell()
        {
            try
            {
                // If there was any code here, it would be inside the try block.
            }
            catch (Exception ex)
            {
                // Log the exception to the Debug output
                Debug.WriteLine("Exception in Cell constructor: " + ex.ToString());
                throw; // Re-throw the exception to maintain the stack trace.
            }
        }

        // Toggle the flag status of the cell
        public void ToggleFlag()
        {
            Flagged = !Flagged;
        }
    }
}