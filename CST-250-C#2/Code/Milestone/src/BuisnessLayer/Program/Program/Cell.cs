using System;


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

    /// <summary>
    /// Constructor for the Cell class.
    /// </summary>
    public Cell()
    {
        
    }
}

