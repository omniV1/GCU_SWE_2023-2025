

using System;
using System.Diagnostics;


namespace MinesweeperGui.BusinessLayer
{
    /// <summary>
    /// Represents the game board, which is a square grid of cells.
    /// </summary>
    public class Board
    {
        // The size of the board (number of cells in each row and column).
        public int Size { get; private set; }

        // The grid of cells, represented as a 2D array.
        public Cell[,] Grid { get; private set; }

        // The difficulty level, represented as a percentage of cells that will be "live".
        public float Difficulty { get; set; }

        // A constant value to indicate a cell is a bomb.
        public const int BombIndicator = 9;

        public void ResetBoard()
        {
            for (int i = 0; i < Size; i++)
            {
                for (int j = 0; j < Size; j++)
                {
                    Grid[i, j].Visited = false;
                    Grid[i, j].Live = false;
                    Grid[i, j].Flagged = false;
                    Grid[i, j].LiveNeighbors = 0;
                }
            }

            // After resetting, you may want to re-setup the live neighbors and calculate live neighbors again.
            SetupLiveNeighbors();
            CalculateLiveNeighbors();
        }

        /// <summary>
        /// Constructor for the Board class. Initializes a square grid of Cell objects.
        /// </summary>
        /// <param name="size">The size of the sides of the square grid.</param>
        public Board(int size)
        {
            Size = size;
            Difficulty = 0.1f; // Default difficulty, can be adjusted externally.
            Grid = new Cell[size, size];

            // Initialize each cell in the grid.
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    Grid[i, j] = new Cell
                    {
                        Row = i,
                        Column = j,
                        Visited = false
                    };
                }
            }
        }

        /// <summary>
        /// Populates the grid with live bombs based on the difficulty level.
        /// </summary>
        public void SetupLiveNeighbors()
        {
            Random random = new();
            // Calculate the number of live bombs to place based on difficulty.
            int liveCellsCount = (int)(Size * Size * Difficulty);

            while (liveCellsCount > 0)
            {
                int row = random.Next(Size);
                int column = random.Next(Size);

                // Place a live bomb in a random cell if it's not already live.
                if (!Grid[row, column].Live)
                {
                    Grid[row, column].Live = true;
                    liveCellsCount--;
                }
            }
        }
        /// <summary>
        /// Calculates the live neighbors for each cell in the grid.
        /// </summary>
        public void CalculateLiveNeighbors()
        {
            for (int i = 0; i < Size; i++)
            {
                for (int j = 0; j < Size; j++)
                {
                    // If the cell is a bomb, set its neighbor count to the bomb indicator.
                    if (Grid[i, j].Live)
                    {
                        Grid[i, j].LiveNeighbors = BombIndicator;
                        continue;
                    }

                    // Check all neighboring cells.
                    int liveNeighbors = 0;
                    for (int x = Math.Max(i - 1, 0); x <= Math.Min(i + 1, Size - 1); x++)
                    {
                        for (int y = Math.Max(j - 1, 0); y <= Math.Min(j + 1, Size - 1); y++)
                        {
                            if (Grid[x, y].Live && !(x == i && y == j))
                            {
                                liveNeighbors++;
                            }
                        }
                    }

                    // Update the live neighbor count for the cell.
                    Grid[i, j].LiveNeighbors = liveNeighbors;
                }
            }
        }

        public void FloodFill(int row, int col, Action<Cell> updateButtonDisplayForFloodFill)
        {
            // Log the current cell being processed.
            Debug.WriteLine($"FloodFill called on cell: ({row}, {col})");

            // Check boundary conditions
            if (row < 0 || row >= Size || col < 0 || col >= Size)
            {
                Debug.WriteLine($"Out of bounds: ({row}, {col})");
                return;
            }

            Cell currentCell = Grid[row, col];

            // If the cell has already been visited or contains a mine, stop recursion
            if (currentCell.Visited || currentCell.Live)
            {
                Debug.WriteLine($"Already visited or a mine: ({row}, {col}) - Visited: {currentCell.Visited}, Live: {currentCell.Live}");
                return;
            }

            // Log the cell's live neighbors count.
            Debug.WriteLine($"Live neighbors: ({row}, {col}) - {currentCell.LiveNeighbors}");

            // Mark the cell as visited
            currentCell.Visited = true;

            // Perform the update using the passed action
            updateButtonDisplayForFloodFill(currentCell);

            // If the cell has live neighbors, do not continue the flood fill
            if (currentCell.LiveNeighbors > 0) return;

            // Log that flood fill is continuing from this cell.
            Debug.WriteLine($"Continuing flood fill from: ({row}, {col})");

            // Recursively call FloodFill on adjacent cells, passing along the action for updates
            FloodFill(row - 1, col, updateButtonDisplayForFloodFill); // North
            FloodFill(row + 1, col, updateButtonDisplayForFloodFill); // South
            FloodFill(row, col - 1, updateButtonDisplayForFloodFill); // West
            FloodFill(row, col + 1, updateButtonDisplayForFloodFill); // East
            FloodFill(row - 1, col - 1, updateButtonDisplayForFloodFill); // Northwest
            FloodFill(row - 1, col + 1, updateButtonDisplayForFloodFill); // Northeast
            FloodFill(row + 1, col - 1, updateButtonDisplayForFloodFill); // Southwest
            FloodFill(row + 1, col + 1, updateButtonDisplayForFloodFill); // Southeast
        }






        public void RevealAllBombs()
        {
            for (int i = 0; i < Size; i++)
            {
                for (int j = 0; j < Size; j++)
                {
                    if (Grid[i, j].Live) // If the cell contains a bomb
                    {
                        Grid[i, j].Visited = true; // Mark as visited to reveal it
                    }
                }
            }
        }

    }

}

