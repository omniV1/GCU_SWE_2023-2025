using Milestone.Models.GameModels;

/// <summary>
/// Manages the game board operations and game logic for Minesweeper
/// </summary>
public class GameBoardManager
{
    // Constant to indicate a cell contains a mine
    public const int BombIndicator = 9;
    private readonly ILogger<GameBoardManager> _logger;

    /// <summary>
    /// Initializes a new instance of GameBoardManager
    /// </summary>
    /// <param name="logger">Logger for tracking game operations</param>
    public GameBoardManager(ILogger<GameBoardManager> logger)
    {
        _logger = logger;
    }

    /// <summary>
    /// Initializes a new board with empty cells, setting up their initial state
    /// </summary>
    /// <param name="board">The game board to initialize</param>
    public void InitializeGrid(Board board)
    {
        for (int i = 0; i < board.Size; i++)
        {
            for (int j = 0; j < board.Size; j++)
            {
                board.Grid[i, j] = new Cell
                {
                    Row = i,
                    Column = j,
                    Visited = false,
                    Live = false,
                    LiveNeighbors = 0,
                    Flagged = false
                };
            }
        }
    }

    /// <summary>
    /// Places mines randomly on the board based on difficulty setting
    /// </summary>
    /// <param name="board">The game board to place mines on</param>
    public void SetupLiveNeighbors(Board board)
    {
        Random random = new Random();
        // Calculate number of mines based on board size and difficulty
        int totalMines = (int)(board.Size * board.Size * board.Difficulty);
        Console.WriteLine($"Setting up {totalMines} mines"); // Debug log

        // Place mines randomly
        int placedMines = 0;
        while (placedMines < totalMines)
        {
            int row = random.Next(board.Size);
            int col = random.Next(board.Size);

            // Only place mine if cell isn't already a mine
            if (!board.Grid[row, col].Live)
            {
                board.Grid[row, col].Live = true;
                placedMines++;
            }
        }

        // Calculate neighbor counts for all cells
        for (int row = 0; row < board.Size; row++)
        {
            for (int col = 0; col < board.Size; col++)
            {
                if (!board.Grid[row, col].Live)
                {
                    int mineCount = 0;
                    // Check all adjacent cells
                    for (int i = -1; i <= 1; i++)
                    {
                        for (int j = -1; j <= 1; j++)
                        {
                            int newRow = row + i;
                            int newCol = col + j;
                            // Skip if out of bounds
                            if (newRow >= 0 && newRow < board.Size &&
                                newCol >= 0 && newCol < board.Size)
                            {
                                if (board.Grid[newRow, newCol].Live)
                                {
                                    mineCount++;
                                }
                            }
                        }
                    }
                    board.Grid[row, col].LiveNeighbors = mineCount;
                }
                else
                {
                    // If cell is a mine, set LiveNeighbors to the bomb indicator
                    board.Grid[row, col].LiveNeighbors = Board.BombIndicator;
                }
            }
        }
    }

    /// <summary>
    /// Processes a cell reveal and returns the game state update
    /// </summary>
    /// <param name="board">The current game board</param>
    /// <param name="row">Row coordinate of the cell</param>
    /// <param name="col">Column coordinate of the cell</param>
    /// <returns>Response containing revealed cells and game state</returns>
    public CellUpdateResponse ProcessCellReveal(Board board, int row, int col)
    {
        var response = new CellUpdateResponse
        {
            IsGameOver = false,
            RevealedCells = new List<CellInfo>()
        };

        // Return if cell is invalid or flagged
        if (!IsValidCell(board, row, col) || board.Grid[row, col].Flagged)
            return response;

        // Handle mine reveal
        if (board.Grid[row, col].Live)
        {
            board.IsGameOver = true;
            response.IsGameOver = true;
            response.IsVictory = false;
            RevealAllMines(board, response.RevealedCells);
            return response;
        }

        FloodFill(board, row, col, response.RevealedCells);
        CheckVictory(board, response);

        return response;
    }

    /// <summary>
    /// Checks if given coordinates are within board boundaries
    /// </summary>
    private bool IsValidCell(Board board, int row, int col)
    {
        return row >= 0 && row < board.Size && col >= 0 && col < board.Size;
    }

    /// <summary>
    /// Recursively reveals empty cells and their neighbors
    /// </summary>
    private void FloodFill(Board board, int row, int col, List<CellInfo> revealedCells)
    {
        // Stop if cell is invalid, already visited, or is a mine
        if (!IsValidCell(board, row, col) ||
            board.Grid[row, col].Visited ||
            board.Grid[row, col].Live)
            return;

        // Mark cell as visited and add to revealed cells list
        board.Grid[row, col].Visited = true;
        revealedCells.Add(new CellInfo
        {
            Row = row,
            Column = col,
            IsRevealed = true,
            IsMine = false,
            NeighborCount = board.Grid[row, col].LiveNeighbors
        });

        // If cell has no adjacent mines, reveal all neighboring cells
        if (board.Grid[row, col].LiveNeighbors == 0)
        {
            for (int i = -1; i <= 1; i++)
            {
                for (int j = -1; j <= 1; j++)
                {
                    if (i == 0 && j == 0) continue;
                    FloodFill(board, row + i, col + j, revealedCells);
                }
            }
        }
    }

    /// <summary>
    /// Processes a chord reveal (revealing adjacent cells when number of adjacent flags matches the cell's number)
    /// </summary>
    public CellUpdateResponse ProcessChordReveal(Board board, int row, int col)
    {
        var response = new CellUpdateResponse
        {
            RevealedCells = new List<CellInfo>(),
            IsGameOver = false,
            IsVictory = false
        };

        // Count adjacent flagged cells and store non-flagged cells
        int flaggedCount = 0;
        var adjacentCells = new List<(int Row, int Col)>();

        // Check all adjacent cells
        for (int i = -1; i <= 1; i++)
        {
            for (int j = -1; j <= 1; j++)
            {
                if (i == 0 && j == 0) continue;

                int newRow = row + i;
                int newCol = col + j;

                if (IsValidCell(board, newRow, newCol))
                {
                    var adjacentCell = board.Grid[newRow, newCol];
                    if (adjacentCell.Flagged)
                    {
                        flaggedCount++;
                    }
                    else if (!adjacentCell.Visited)
                    {
                        adjacentCells.Add((newRow, newCol));
                    }
                }
            }
        }

        // If flags match the number, reveal non-flagged cells
        if (flaggedCount == board.Grid[row, col].LiveNeighbors)
        {
            foreach (var (newRow, newCol) in adjacentCells)
            {
                var revealResult = ProcessCellReveal(board, newRow, newCol);
                response.RevealedCells.AddRange(revealResult.RevealedCells);

                if (revealResult.IsGameOver)
                {
                    response.IsGameOver = true;
                    response.IsVictory = revealResult.IsVictory;
                    break;
                }
            }
        }

        return response;
    }

    /// <summary>
    /// Reveals all mines on the board when game is over
    /// </summary>
    private void RevealAllMines(Board board, List<CellInfo> revealedCells)
    {
        for (int i = 0; i < board.Size; i++)
        {
            for (int j = 0; j < board.Size; j++)
            {
                if (board.Grid[i, j].Live)
                {
                    board.Grid[i, j].Visited = true;
                    revealedCells.Add(new CellInfo
                    {
                        Row = i,
                        Column = j,
                        IsRevealed = true,
                        IsMine = true,
                        NeighborCount = BombIndicator
                    });
                }
            }
        }
    }

    /// <summary>
    /// Checks if victory condition is met (all non-mine cells revealed)
    /// </summary>
    private void CheckVictory(Board board, CellUpdateResponse response)
    {
        bool victory = true;
        // Victory only if all non-mine cells are revealed
        for (int i = 0; i < board.Size; i++)
        {
            for (int j = 0; j < board.Size; j++)
            {
                if (!board.Grid[i, j].Live && !board.Grid[i, j].Visited)
                {
                    victory = false;
                    break;
                }
            }
            if (!victory) break;
        }

        if (victory)
        {
            board.IsGameOver = true;
            board.IsVictory = true;
            response.IsGameOver = true;
            response.IsVictory = true;
        }
    }
}