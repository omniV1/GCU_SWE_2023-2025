using ChessBoardModel;
using System.Runtime.InteropServices;

namespace ChessBoardConsoleApp 
{ 

class Program
{
    static Board myBoard = new Board(8);

        static public void PrintGrid(Board myBoard)
        {
            // Top border
            Console.WriteLine("  +---+---+---+---+---+---+---+---+");

            for (int i = 0; i < myBoard.Size; i++)
            {
                // Print the row number at the start of the row
                Console.Write((i + 1) + " |");

                for (int j = 0; j < myBoard.Size; j++)
                {
                    // Choose the appropriate character
                    char symbol = myBoard.theGrid[i, j].CurrentlyOccupied ? 'X' :
                                  myBoard.theGrid[i, j].LegalNextMove ? '+' : ' ';

                    // Print the cell with borders
                    Console.Write(" " + symbol + " |");
                }

                // End of row
                Console.WriteLine();

                // Print the row separator
                Console.WriteLine("  +---+---+---+---+---+---+---+---+");
            }

            // Print the column letters at the bottom
            Console.WriteLine("    1   2   3   4   5   6   7   8");
            Console.WriteLine("===================================");
        }


        static public Cell SetCurrentCell()
        {
            int currentRow, currentCol;
            Console.Out.Write("Enter your current row number: ");
            while (!int.TryParse(Console.ReadLine(), out currentRow) || currentRow < 1 || currentRow > 8)
            {
                Console.Out.Write("Invalid input. Please enter a row number between 1 and 8: ");
            }

            Console.Out.Write("Enter your current column number: ");
            while (!int.TryParse(Console.ReadLine(), out currentCol) || currentCol < 1 || currentCol > 8)
            {
                Console.Out.Write("Invalid input. Please enter a column number between 1 and 8: ");
            }

            // Subtract 1 from user input to convert to 0-based index
            currentRow--;
            currentCol--;

            myBoard.theGrid[currentRow, currentCol].CurrentlyOccupied = true;

            return myBoard.theGrid[currentRow, currentCol];
        }


        static void Main(string[] args)
        {
            // show the empty chess board
            PrintGrid(myBoard);

            // Ask user for the type of chess piece
            Console.WriteLine("Select a chess piece (Knight, Rook, Bishop, Queen, King, Pawn): ");
            string chessPiece = Console.ReadLine();

            // Validate user input for chess piece
            while (!IsValidPiece(chessPiece))
            {
                Console.WriteLine("Invalid piece. Please select a valid chess piece (Knight, Rook, Bishop, Queen, King, Pawn): ");
                chessPiece = Console.ReadLine();
            }

            // get the location of the chess piece
            Cell currentCell = SetCurrentCell();

            // calculate and mark the cells where legal moves are possible
            myBoard.MarkNextLegalMoves(currentCell, chessPiece);

            // show the chess board with the piece placed and possible moves
            PrintGrid(myBoard);

            // wait for another return key to end the program
            Console.ReadLine();
        }

        static bool IsValidPiece(string piece)
        {
            string[] validPieces = { "Knight", "Rook", "Bishop", "Queen", "King", "Pawn" };
            return validPieces.Contains(piece, StringComparer.OrdinalIgnoreCase);
        }

    }


}
