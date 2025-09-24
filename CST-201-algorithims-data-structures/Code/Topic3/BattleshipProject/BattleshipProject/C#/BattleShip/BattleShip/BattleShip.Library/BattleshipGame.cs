
using System.Diagnostics;

namespace BattleShip.Library
{
    public class BattleshipGame
    {
        public const int BoardSize = 10;
        public const char OpenCellChar = '.';
        public const char ShipCellTaken = 'O';
        public const char MissCell = 'M';
        public const char HitCell = 'X';

        public char[,]? PlayerBoard { get; set; }
        public char[,]? ComputerBoard { get; set; }
        public List<Ship>? PlayerShips { get; set; }
        public List<Ship>? ComputerShips { get; set; }

        public BattleshipGame()
        {
            InitGame();
            SetComputerShips();
        }

        public BattleshipGame(bool doComputerShips)
        {
            InitGame();
            if (doComputerShips)
            {
                SetComputerShips();
            }
        }

        public void SetComputerShips()
        {
            var random = new Random();
            for (var shipIdx = 0; shipIdx < 3; shipIdx ++)
            {
                var ship = ComputerShips[shipIdx];
                while (true)
                {
                    var row = random.Next(BoardSize);
                    var col = random.Next(BoardSize);

                    if (PlaceShip(ComputerBoard, row, col, ship))
                    {
                        break;
                    }
                }
            }
        }

        public bool PlaceShip(char[,] board, int row, int col, Ship ship)
        {
            return ship.Type switch
            {
                Ship.ShipTypes.Cruiser => PlaceCruiser(board, row, col, (Cruiser)ship, true) &&
                                          PlaceCruiser(board, row, col, (Cruiser)ship),
                Ship.ShipTypes.Destroyer => PlaceDestroyer(board, row, col, (Destroyer)ship, true) &&
                                            PlaceDestroyer(board, row, col, (Destroyer)ship),
                Ship.ShipTypes.Submarine => PlaceSubmarine(board, row, col, (Submarine)ship, true) &&
                                            PlaceSubmarine(board, row, col, (Submarine)ship),
                _ => false
            };
        }

        public bool CheckGameOver(bool checkPlayer)
        {
            if (checkPlayer)
            {
                return !StillHaveShips(PlayerBoard);
            }

            return !StillHaveShips(ComputerBoard);
        }

        public bool AlreadyFired(bool playerBoard, int row, int column)
        {
            if (!playerBoard)
            {
                return ComputerBoard[row, column] is HitCell or MissCell;
            }

            return PlayerBoard[row, column] is HitCell or MissCell;
        }

        public bool IsHit(bool playerBoard, int row, int column)
        {
            var retVal = false;

            if (playerBoard)
            {
                retVal = ComputerBoard[row, column] is ShipCellTaken;
                if (PlayerBoard[row, column] is ShipCellTaken)
                {
                    PlayerBoard[row, column] = HitCell;
                }
                else
                {
                    PlayerBoard[row, column] = MissCell;
                }

                return retVal;
            }

            retVal = ComputerBoard[row, column] is ShipCellTaken;
            if (ComputerBoard[row, column] is ShipCellTaken)
            {
                ComputerBoard[row, column] = HitCell;
                PlayerBoard[row, column] = HitCell;
            }
            else
            {
                ComputerBoard[row, column] = MissCell;
                PlayerBoard[row, column] = MissCell;
            }

            return retVal;
        }

        /// <summary>
        /// Attempts to place a Cruiser ship on the game board.
        /// </summary>
        /// <param name="board">The game board to place the ship on.</param>
        /// <param name="row">The starting row coordinate for ship placement.</param>
        /// <param name="column">The starting column coordinate for ship placement.</param>
        /// <param name="ship">The Cruiser ship object to be placed.</param>
        /// <param name="checkOnly">If true, only checks if placement is valid without actually placing the ship.</param>
        /// <returns>
        /// True if the ship can be placed (or is placed successfully), false otherwise.
        /// </returns>
        /// <remarks>
        /// The Cruiser occupies 3 cells in a straight line, either vertically or horizontally,
        /// depending on the ship's orientation properties (Vertical, Upwards, Left).
        /// </remarks>
        public bool PlaceCruiser(char[,] board, int row, int column, Cruiser ship, bool checkOnly = false)
        {
       

            Debug.WriteLine($"Attempting to place Cruiser at ({row}, {column})");
            Debug.WriteLine($"Orientation: Vertical = {ship.Vertical}, Upwards = {ship.Upwards}, Left = {ship.Left}");

            // Define the shape of the cruiser based on its orientation
            // The cruiser occupies 3 cells in a straight line, either vertically or horizontally
            int[][] offsets;
            if (ship.Vertical)
            {
                // Vertical orientation: ship extends up or down from the starting point
                offsets = ship.Upwards
                    ? new int[][] { new int[] { 0, 0 }, new int[] { -1, 0 }, new int[] { -2, 0 } }  // Extends upwards
                    : new int[][] { new int[] { 0, 0 }, new int[] { 1, 0 }, new int[] { 2, 0 } };   // Extends downwards
            }
            else
            {
                // Horizontal orientation: ship extends left or right from the starting point
                offsets = ship.Left
                    ? new int[][] { new int[] { 0, 0 }, new int[] { 0, -1 }, new int[] { 0, -2 } }  // Extends to the left
                    : new int[][] { new int[] { 0, 0 }, new int[] { 0, 1 }, new int[] { 0, 2 } };   // Extends to the right
            }

            Debug.WriteLine($"Cruiser shape: {string.Join(", ", offsets.Select(o => $"({o[0]}, {o[1]})"))}");

            // Validate the placement: check if all required cells are within the board and empty
            foreach (var offset in offsets)
            {
                int newRow = row + offset[0];
                int newCol = column + offset[1];
                // Check for out of bounds placement or cell occupation
                if (newRow < 0 || newRow >= BoardSize || newCol < 0 || newCol >= BoardSize || board[newRow, newCol] != OpenCellChar)
                {
                    Debug.WriteLine($"Invalid placement at ({newRow}, {newCol}). Reason: " +
                        (newRow < 0 || newRow >= BoardSize || newCol < 0 || newCol >= BoardSize ? "Out of bounds" : "Cell occupied"));
                    return false;  // Placement is invalid
                }
            }

            // If only checking for valid placement, return true at this point
            if (checkOnly)
            {
                Debug.WriteLine("Check only, returning true");
                return true;
            }

            // Place the ship on the board
            foreach (var offset in offsets)
            {
                int newRow = row + offset[0];
                int newCol = column + offset[1];
                board[newRow, newCol] = ShipCellTaken;  // Mark the cell as occupied by a ship
                Debug.WriteLine($"Placed Cruiser part at ({newRow}, {newCol})");
            }

            Debug.WriteLine("Cruiser placed successfully");
            return true;  // Placement successful
        }


        /// <summary>
        /// Attempts to place a Destroyer ship on the game board.
        /// </summary>
        /// <param name="board">The game board to place the ship on.</param>
        /// <param name="row">The starting row coordinate for ship placement.</param>
        /// <param name="column">The starting column coordinate for ship placement.</param>
        /// <param name="ship">The Destroyer ship object to be placed.</param>
        /// <param name="checkOnly">If true, only checks if placement is valid without actually placing the ship.</param>
        /// <returns>
        /// True if the ship can be placed (or is placed successfully), false otherwise.
        /// </returns>
        /// <remarks>
        /// The Destroyer occupies a 2x2 square on the board. Its shape can be modified
        /// based on the ship's orientation properties (Upwards, Left).
        /// A special case prevents left-oriented placement at column 0.
        /// </remarks>
        public bool PlaceDestroyer(char[,] board, int row, int column, Destroyer ship, bool checkOnly = false)
        {
            Debug.WriteLine($"Attempting to place Destroyer at ({row}, {column})");
            Debug.WriteLine($"Orientation: Upwards = {ship.Upwards}, Left = {ship.Left}");

            // Initial validation: check if the starting position is valid
            // Also checks for the case where a left-oriented ship can't be placed at column 0
            if (row < 0 || row >= BoardSize || column < 0 || column >= BoardSize || (ship.Left && column == 0))
            {
                Debug.WriteLine($"Invalid placement. Reason: " +
                    (row < 0 || row >= BoardSize || column < 0 || column >= BoardSize ? "Out of bounds" : "Left-oriented at column 0"));
                return false;  // Placement is invalid
            }

            // Define the 2x2 square shape of the destroyer
            int[][] offsets = new int[][]
            {
        new int[] { 0, 0 },  // Top-left corner
        new int[] { 0, 1 },  // Top-right corner
        new int[] { 1, 0 },  // Bottom-left corner
        new int[] { 1, 1 }   // Bottom-right corner
            };

            // Adjust the shape based on the ship's orientation
            if (ship.Upwards)
            {
                // Flip the shape vertically if the ship is oriented upwards
                offsets[2][0] = -1;
                offsets[3][0] = -1;
            }
            if (ship.Left)
            {
                // Flip the shape horizontally if the ship is oriented to the left
                offsets[1][1] = -1;
                offsets[3][1] = -1;
            }

            Debug.WriteLine($"Destroyer shape: {string.Join(", ", offsets.Select(o => $"({o[0]}, {o[1]})"))}");

            // If only checking for valid placement, return true at this point
            if (checkOnly)
            {
                Debug.WriteLine("Check only, returning true");
                return true;
            }

            // Attempt to place the ship parts
            foreach (var offset in offsets)
            {
                int newRow = row + offset[0];
                int newCol = column + offset[1];
                if (newRow >= 0 && newRow < BoardSize && newCol >= 0 && newCol < BoardSize)
                {
                    board[newRow, newCol] = ShipCellTaken;  // Mark the cell as occupied by a ship
                    Debug.WriteLine($"Placed Destroyer part at ({newRow}, {newCol})");
                }
                else
                {
                    Debug.WriteLine($"Could not place Destroyer part at ({newRow}, {newCol}). Out of bounds.");
                }
            }

            Debug.WriteLine("Destroyer placement attempt complete");
            return true;  // Placement successful (even if some parts couldn't be placed due to being out of bounds)
        }


        /// <summary>
        /// Attempts to place a Submarine ship on the game board.
        /// </summary>
        /// <param name="board">The game board to place the ship on.</param>
        /// <param name="row">The starting row coordinate for ship placement.</param>
        /// <param name="column">The starting column coordinate for ship placement.</param>
        /// <param name="ship">The Submarine ship object to be placed.</param>
        /// <param name="checkOnly">If true, only checks if placement is valid without actually placing the ship.</param>
        /// <returns>
        /// True if the ship can be placed (or is placed successfully), false otherwise.
        /// </returns>
        /// <remarks>
        /// The Submarine occupies 3 cells in a diagonal pattern. Its shape can be modified
        /// based on the ship's orientation properties (Upwards, Left).
        /// </remarks>
        public bool PlaceSubmarine(char[,] board, int row, int column, Submarine ship, bool checkOnly = false)
        {
            Debug.WriteLine($"Attempting to place Submarine at ({row}, {column})");
            Debug.WriteLine($"Orientation: Upwards = {ship.Upwards}, Left = {ship.Left}");

            // Define the shape of the submarine (diagonal pattern)
            // The submarine occupies 3 cells in a diagonal line
            int[][] offsets = new int[][]
            {
        new int[] { 0, 0 },  // Starting point
        new int[] { 1, 1 },  // Diagonal down and right
        new int[] { 2, 2 }   // Further diagonal down and right
            };

            // Adjust the shape based on the ship's orientation
            if (ship.Upwards)
            {
                // Flip the shape vertically if the ship is oriented upwards
                for (int i = 0; i < offsets.Length; i++)
                {
                    offsets[i][0] = -offsets[i][0];
                }
            }
            if (ship.Left)
            {
                // Flip the shape horizontally if the ship is oriented to the left
                for (int i = 0; i < offsets.Length; i++)
                {
                    offsets[i][1] = -offsets[i][1];
                }
            }

            Debug.WriteLine($"Submarine shape: {string.Join(", ", offsets.Select(o => $"({o[0]}, {o[1]})"))}");

            // Validate the placement: check if all required cells are within the board and empty
            foreach (var offset in offsets)
            {
                int newRow = row + offset[0];
                int newCol = column + offset[1];
                // Check for out of bounds placement or cell occupation
                if (newRow < 0 || newRow >= BoardSize || newCol < 0 || newCol >= BoardSize || board[newRow, newCol] != OpenCellChar)
                {
                    Debug.WriteLine($"Invalid placement at ({newRow}, {newCol}). Reason: " +
                        (newRow < 0 || newRow >= BoardSize || newCol < 0 || newCol >= BoardSize ? "Out of bounds" : "Cell occupied"));
                    return false;  // Placement is invalid
                }
            }

            // If only checking for valid placement, return true at this point
            if (checkOnly)
            {
                Debug.WriteLine("Check only, returning true");
                return true;
            }

            // Place the ship on the board
            foreach (var offset in offsets)
            {
                int newRow = row + offset[0];
                int newCol = column + offset[1];
                board[newRow, newCol] = ShipCellTaken;  // Mark the cell as occupied by a ship
                Debug.WriteLine($"Placed Submarine part at ({newRow}, {newCol})");
            }

            Debug.WriteLine("Submarine placed successfully");
            return true;  // Placement successful
        }

        private void InitGame()
        {
            PlayerBoard = new char[BoardSize, BoardSize];
            ComputerBoard = new char[BoardSize, BoardSize];

            PlayerShips = new List<Ship>
            {
                new Destroyer("USS Destroyer", 'D'),
                new Submarine("USS Submarine", 'S'),
                new Cruiser("USS Cruiser", 'C')
            };

            ComputerShips = new List<Ship>
            {
                new Destroyer("NCC Destroyer", 'D'),
                new Submarine("NCC Submarine", 'S'),
                new Cruiser("NCC Cruiser", 'C')
            };

            InitializeBoards();
        }

        private void InitializeBoards()
        {
            for (var row = 0; row < BoardSize; row ++)
            {
                for (var column = 0; column < BoardSize; column ++)
                {
                    PlayerBoard[row, column] = OpenCellChar;
                    ComputerBoard[row, column] = OpenCellChar;
                }
            }
        }

        private bool StillHaveShips(char[,] board)
        {
            for (var row = 0; row < BoardSize; row++)
            {
                for (var column = 0; column < BoardSize; column++)
                {
                    if (board[row, column] == ShipCellTaken)
                    {
                        return true;
                    }
                }
            }

            return false;
        }
    }
}
