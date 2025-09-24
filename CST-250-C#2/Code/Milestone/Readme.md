##### Owen Lindsey
##### CST-250
##### 2/11/2024 
##### this was done with the help of 
##### 

#####  online resource: King, J. C# Jagged Array vs Multidemensional Array : Youtube./ https://www.youtube.com/watch?v=3UcJGikWJxs
#####  online resource: Sluiter, S. C# Chess Board 05 print board squares : Youtube./ https://www.youtube.com/watch?v=U9dsYjKaEAo&list=PLhPyEFL5u-i0YDRW6FLMd1PavZp9RcYdF&index=5
#####  online resource: Sluiter, S. C# Chess Board 07 challenges : Youtube./ https://www.youtube.com/watch?v=xYdhGa3ZF1I&list=PLhPyEFL5u-i0YDRW6FLMd1PavZp9RcYdF&index=7
---

# Minesweeper Game - Milestone 2 

### Key Features
- **Board Initialization**: The game begins by creating a 10x10 board, where bombs are placed randomly based on the difficulty level.
- **Gameplay Loop**: Players enter coordinates for the row and column they wish to reveal. The game continues until a bomb is hit or all safe cells are revealed.
- **Victory Check**: After each move, the game checks if the player has won by revealing all non-bomb cells.
- **User Interface**: The board is displayed in the console with clear demarcation of cells, using `.` for unvisited cells, `B` for bombs, and numbers representing the count of adjacent bombs.

### Classes and Methods
- `Program`
  - Contains the `Main` method, which drives the game by initializing the board and entering the gameplay loop.
  - `PrintBoard` method for displaying the board in a user-friendly format.
- `Board`
  - Manages the board size, the grid of cells, and the overall difficulty.
  - Methods for setting up bombs (`SetupLiveNeighbors`) and calculating adjacent live cells (`CalculateLiveNeighbors`).
- `Cell`
  - Represents each cell on the board with properties such as row, column, visited, live, and the count of live neighbors.
  - Includes methods to access and mutate its state, like `SetVisited` and `SetLive`.

### Enhancements in Milestone 2
- Improved `PrintBoard` method for enhanced readability and aesthetics in the console.
-  User input handling to check for zero-based array indexing, which corrects the previous off-by-one error.
-  Check for victory conditions.
  
# logic flowchart 

### Gameplay Mechanics
1. The board is printed to the console with initial hidden cells.
2. The user inputs their desired cell to reveal.
3. Input is validated and checked against the board's state.
4. If a bomb is revealed, the game ends with a loss. Otherwise, gameplay continues.
5. If all safe cells are revealed, the game ends with a win.


![flowchart](https://github.com/omniV1/250/blob/main/Milestone/screenshots/milestone_flowchart.drawio.png)

# UML Diagrams 

## Board class UML; 

### Properites 
- `Size`: Length of the board's sides, indicating the number of cells horizontally and vertically.
- `Grid`: A two-dimensional array holding `Cell` objects that make up the game board.
- `Difficulty`: Determines the density of bombs on the board.
- `BombIndicator`: A special constant to mark cells containing bombs.

### Methods
- `SetupLiveNeighbors`: Randomly places bombs on the board according to the difficulty.
- `CalculateLiveNeighbors`: Determines the number of adjacent bombs for each cell, marking bomb cells with the bomb indicator.


![Board Uml](https://github.com/omniV1/250/blob/main/Milestone/UML-diagrams/CST-250-Board-class.drawio%20.png)

## Cell class UML: 

### Properties
- `row`: The row index of the cell in the grid.
- `column`: The column index of the cell in the grid.
- `visited`: A boolean indicating whether the cell has been revealed.
- `live`: A boolean indicating whether the cell is a bomb.
- `liveNeighbors`: An integer count of adjacent bombs.

### Constructor
- `Cell(row: int, column: int)`: Initializes a new instance of the `Cell` class with specified row and column indices.

### Methods
- `getRow()`: Returns the row index.
- `getColumn()`: Returns the column index.
- `isVisited()`: Returns whether the cell has been visited.
- `setVisited(visited: boolean)`: Sets the cell as visited or unvisited.
- `isLive()`: Returns whether the cell is a bomb.
- `setLive(live: boolean)`: Sets the cell as containing a bomb or not.
- `getLiveNeighbors()`: Returns the count of live neighbors.
- `setLiveNeighbors(liveNeighbors: int)`: Sets the count of live neighbors.


![Cell uml](https://github.com/omniV1/250/blob/main/Milestone/UML-diagrams/CST-250-Cell-Class.drawio%20.png) 

## Program class UML: 

### Properties 
 `Main Method`: 
- Sets up a 10x10 game board with bombs.
- Enters a loop, clearing the console and displaying the board.
- Requests and validates user input for row and column selection.
- Checks for bombs and victory conditions, ending the game appropriately.

#### Methods
- `PrintBoard` Method Prints the current state of the board, using `.` for hidden cells, `B` for bombs, and numbers for neighbor bomb counts
- `CheckVictory` Method Determines if all non-bomb cells are revealed, returning true if the player wins.
 

![Program-uml](https://github.com/omniV1/250/blob/main/Milestone/UML-diagrams/CST-250-Program-class.drawio%20.png) 

---

### Src code 

 - This code reprsents the game board, which is a square grid of cells.

   

``` C#


using System;

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
                Grid[i, j] = new Cell();
                Grid[i, j].Row = i;
                Grid[i, j].Column = j;
            }
        }
    }

    /// <summary>
    /// Populates the grid with live bombs based on the difficulty level.
    /// </summary>
    public void SetupLiveNeighbors()
    {
        Random random = new Random();
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
}




```



- This class src code represents a single cell on the game board

  

``` C#
{
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



```



- This is the main entry point for our minesweeper application.



  

```C# 
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

            //  Ask the user for a row and column number.
            Console.WriteLine("Enter the row number:");

            // Subtract 1 to convert to zero-based index
            int row = Convert.ToInt32(Console.ReadLine()) - 1; 
            Console.WriteLine("Enter the column number:");

            // Subtract 1 to convert to zero-based index
            int column = Convert.ToInt32(Console.ReadLine()) - 1; 


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

            // Mark the cell as visited
            board.Grid[row, column].Visited = true;

            // Check if all non-bomb cells have been revealed.
            board.Grid[row, column].Visited = true; // Mark the cell as visited

            // Check for victory after each move
            if (CheckVictory(board))
            {
                gameOver = true;
                Console.Clear(); // Clear the console for a final display of the board
                PrintBoard(board); // Print the final state of the board
                Console.WriteLine("Congratulations! You've cleared all non-bomb cells!");
                break;
            }

            // Print the grid.
            PrintBoard(board);
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
        // Top border
        Console.Write("   "); // Space for row numbers
        for (int k = 0; k < board.Size; k++)
        {
            Console.Write("+---");
        }
        Console.WriteLine("+"); // Rightmost border

        for (int i = 0; i < board.Size; i++)
        {
            // Print the row number at the start of the row with padding for single digit numbers
            Console.Write((i < 9 ? " " : "") + (i + 1) + " |");

            for (int j = 0; j < board.Size; j++)
            {
                // Directly access the Cell properties
                Cell cell = board.Grid[i, j];
                char symbol;
                if (cell.Visited)
                {
                    // Display the number of live neighbors or an empty square
                    symbol = cell.LiveNeighbors > 0 ? cell.LiveNeighbors.ToString()[0] : ' ';
                }
                else
                {
                    // Unvisited cells are represented with a question mark
                    symbol = '?';
                }

                // Print the cell with borders
                Console.Write(" " + symbol + " |");
            }

            // End of row
            Console.WriteLine();

            // Print the row separator
            Console.Write("   "); // Space for row numbers
            for (int k = 0; k < board.Size; k++)
            {
                Console.Write("+---");
            }
            Console.WriteLine("+"); // Rightmost border
        }

        // Print the column numbers at the bottom
        Console.Write("    "); // Align with the column
        for (int i = 0; i < board.Size; i++)
        {
            // Adjusted for single digit numbers with proper spacing
            Console.Write(" " + (i + 1) + "  ");
        }
        Console.WriteLine();
        Console.WriteLine("    " + new string('=', 4 * board.Size)); // Adjusted the bottom line
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
```

--- 

### Running program 

- This image shows our current console.out to the terminal when we run program.cs.

  ![Running program](https://github.com/omniV1/250/blob/main/Milestone/screenshots/Screenshot%202024-02-11%20125409.png)


