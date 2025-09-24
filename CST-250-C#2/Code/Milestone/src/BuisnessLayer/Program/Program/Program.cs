using System.Net.NetworkInformation;

/// Owen Lindsey
/// Milestone 2
/// 2/11/2024
/// This was done with the help of 
/// online resource: King, J. C# Jagged Array vs Multidemensional Array : Youtube./ https://www.youtube.com/watch?v=3UcJGikWJxs
///online resource: Sluiter, S. C# Chess Board 05 print board squares : Youtube./ https://www.youtube.com/watch?v=U9dsYjKaEAo&list=PLhPyEFL5u-i0YDRW6FLMd1PavZp9RcYdF&index=5
///online resource: Sluiter, S. C# Chess Board 07 challenges : Youtube./ https://www.youtube.com/watch?v=xYdhGa3ZF1I&list=PLhPyEFL5u-i0YDRW6FLMd1PavZp9RcYdF&index=7

/// <summary>
/// The main entry point for the console application.
/// </summary>
class Program
{
    /// <summary>
    /// The Main method that drives the application.
    /// </summary>
    static void Main(string[] args)
    {
        // Initialize the board and game state
        Board board = new(10); // Assume a 10x10 board for this example.
        board.SetupLiveNeighbors(); // Place live bombs on the board.
        board.CalculateLiveNeighbors(); // Calculate live neighbors for all cells.

        bool gameOver = false;
        while (!gameOver)
        {
            Console.Clear(); // Optional: Clear the console for a clean game board display.
            PrintBoard(board); // Print the current state of the board.

            // Ask the user for a row and column number.
            Console.WriteLine("Enter the row number:");
            int row = Convert.ToInt32(Console.ReadLine()) - 1; // Subtract 1 to convert to zero-based index
            Console.WriteLine("Enter the column number:");
            int column = Convert.ToInt32(Console.ReadLine()) - 1; // Subtract 1 to convert to zero-based index

            // Validate the input
            if (row < 0 || row >= board.Size || column < 0 || column >= board.Size)
            {
                Console.WriteLine("Invalid coordinates. Please try again.");
                continue;
            }

            // Check if the chosen cell contains a bomb.
            if (board.Grid[row, column].Live)
            {
                gameOver = true;
                Console.WriteLine("Boom! You hit a bomb! Game Over.");
                break;
            }
            else if (board.Grid[row, column].LiveNeighbors == 0)
            {
                board.FloodFill(row, column); // Call the flood fill method
            }
            else
            {
                board.Grid[row, column].Visited = true; // Reveal the current cell
            }

            // Check for victory after each move
            if (CheckVictory(board))
            {
                gameOver = true;
                Console.Clear(); // Clear the console for a final display of the board
                PrintBoard(board); // Print the final state of the board
                Console.WriteLine("Congratulations! You've cleared all non-bomb cells!");
                break;
            }
        }
    }

    /// <summary>
    /// Prints the board to the console. Each cell is represented by a character:
    /// '.' for an unvisited cell, 'B' for a live bomb, or the number of live neighbors.
    /// </summary>
    /// <param name="board">The game board to print.</param>
    // New method to display the board during the game
    public static void PrintBoard(Board board)
    {
        // Print column numbers on the top
        Console.Write("     "); // Adjust spacing to align with the grid
        for (int col = 0; col < board.Size; col++)
        {
            Console.Write("{0,2}  ", col + 1); // Adjusted for single digit numbers with proper spacing
        }
        Console.WriteLine();

        // Top border
        Console.Write("   +");
        for (int k = 0; k < board.Size; k++)
        {
            Console.Write("---+");
        }
        Console.WriteLine();

        for (int i = 0; i < board.Size; i++)
        {
            // Print the row number at the start of the row with padding for single-digit numbers
            Console.Write("{0,2} |", i + 1);

            for (int j = 0; j < board.Size; j++)
            {
                Cell cell = board.Grid[i, j];
                if (cell.Visited)
                {
                    if (cell.LiveNeighbors > 0)
                    {
                        Console.Write(" {0} |", cell.LiveNeighbors); // Pad single digits for alignment
                    }
                    else
                    {
                        Console.Write(" ~ |"); // Empty space for cells with no neighbors
                    }
                }
                else
                {
                    Console.Write(" ? |"); // Question mark for unvisited cells
                }
            }

            Console.WriteLine();

            // Print the row separator
            Console.Write("   +");
            for (int k = 0; k < board.Size; k++)
            {
                Console.Write("---+");
            }
            Console.WriteLine();
        }

        // Print column numbers on the bottom
        Console.Write("     "); // Adjust spacing to align with the grid
        for (int col = 0; col < board.Size; col++)
        {
            Console.Write("{0,2}  ", col + 1); // Adjusted for single digit numbers with proper spacing
        }
        Console.WriteLine();
    }




    /// <summary>
    /// Checks if the player has won the game by revealing all non-bomb cells.
    /// </summary>
    /// <param name="board">The game board containing all cells.</param>
    /// <returns>
    /// A boolean value that is true if all non-bomb cells have been revealed and false otherwise.
    /// This indicates whether the player has successfully completed the game without hitting a bomb.
    /// </returns>
    private static bool CheckVictory(Board board)
        {
            for (int i = 0; i < board.Size; i++)
            {
                for (int j = 0; j < board.Size; j++)
                {
                    Cell cell = board.Grid[i, j];
                    // If there's a cell that is not a bomb and has not been visited, the player hasn't won yet.
                    if (!cell.Live && !cell.Visited)
                    {
                        return false;
                    }
                }
            }
            // If all non-bomb cells have been visited, the player wins.
            return true;
        }


    }







