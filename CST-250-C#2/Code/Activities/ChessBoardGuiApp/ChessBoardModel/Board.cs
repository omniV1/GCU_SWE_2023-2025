using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessBoardModel
{
   public class Board
    {
        // the board is always square. Usually 8x8
        public int Size { get; set; }

        // 2d array of Cell object 
        public Cell[,] theGrid;


        // constructor
        public Board(int s)
        {
            Size = s;
            // we must initialize the array to avoid Null Exception Error
            theGrid = new Cell[Size, Size];
            for (int i = 0; i < Size; i++)
            {
                for (int j = 0; j < Size; j++)
                {
                    theGrid[i, j] = new Cell(i, j);
                }
            }
        }
        public void MarkNextLegalMoves(Cell currentCell, string chessPiece)
        {
            // slep 1 - clear all LegalMoves from previous turn.
            for (int r = 0; r < Size; r++)
            {
                for (int c = 0; c < Size; c++)
                {
                    theGrid[r, c].LegalNextMove = false;
                }

            }

            //step 2 - find all legal moces and mark the square. 
            switch (chessPiece)
            {
                case "Knight":
                    // Validate each move individually to ensure it's within the board
                    if (currentCell.RowNumber - 2 >= 0 && currentCell.ColumnNumber - 1 >= 0)
                        theGrid[currentCell.RowNumber - 2, currentCell.ColumnNumber - 1].LegalNextMove = true;
                    if (currentCell.RowNumber - 2 >= 0 && currentCell.ColumnNumber + 1 < Size)
                        theGrid[currentCell.RowNumber - 2, currentCell.ColumnNumber + 1].LegalNextMove = true;
                    if (currentCell.RowNumber - 1 >= 0 && currentCell.ColumnNumber + 2 < Size)
                        theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber + 2].LegalNextMove = true;
                    if (currentCell.RowNumber + 1 < Size && currentCell.ColumnNumber + 2 < Size)
                        theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber + 2].LegalNextMove = true;
                    if (currentCell.RowNumber + 2 < Size && currentCell.ColumnNumber + 1 < Size)
                        theGrid[currentCell.RowNumber + 2, currentCell.ColumnNumber + 1].LegalNextMove = true;
                    if (currentCell.RowNumber + 2 < Size && currentCell.ColumnNumber - 1 >= 0)
                        theGrid[currentCell.RowNumber + 2, currentCell.ColumnNumber - 1].LegalNextMove = true;
                    if (currentCell.RowNumber + 1 < Size && currentCell.ColumnNumber - 2 >= 0)
                        theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber - 2].LegalNextMove = true;
                    if (currentCell.RowNumber - 1 >= 0 && currentCell.ColumnNumber - 2 >= 0)
                        theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber - 2].LegalNextMove = true;

                    break;

                case "Rook":
                    // Horizontal and vertical moves
                    for (int i = 0; i < Size; i++)
                    {

                        // Horizontal moves
                        // Skip the rook's current column
                        if (i != currentCell.ColumnNumber)
                            theGrid[currentCell.RowNumber, i].LegalNextMove = true;

                        // Vertical moves
                        // Skip the rook's current row
                        if (i != currentCell.RowNumber)
                            theGrid[i, currentCell.ColumnNumber].LegalNextMove = true;
                    }
                    break;

                case "Bishop":

                    // Diagonal moves
                    for (int i = 1; i < Size; i++)
                    {
                        // Top-left diagonal
                        if (currentCell.RowNumber - i >= 0 && currentCell.ColumnNumber - i >= 0)
                            theGrid[currentCell.RowNumber - i, currentCell.ColumnNumber - i].LegalNextMove = true;

                        // Top-right diagonal
                        if (currentCell.RowNumber - i >= 0 && currentCell.ColumnNumber + i < Size)
                            theGrid[currentCell.RowNumber - i, currentCell.ColumnNumber + i].LegalNextMove = true;

                        // Bottom-right diagonal
                        if (currentCell.RowNumber + i < Size && currentCell.ColumnNumber + i < Size)
                            theGrid[currentCell.RowNumber + i, currentCell.ColumnNumber + i].LegalNextMove = true;

                        // Bottom-left diagonal
                        if (currentCell.RowNumber + i < Size && currentCell.ColumnNumber - i >= 0)
                            theGrid[currentCell.RowNumber + i, currentCell.ColumnNumber - i].LegalNextMove = true;
                    }
                    break;

                case "Pawn_White":
                    // Move forward
                    if (currentCell.RowNumber - 1 >= 0 && !theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber].CurrentlyOccupied)
                        theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber].LegalNextMove = true;

                    // Capture diagonally left
                    if (currentCell.RowNumber - 1 >= 0 && currentCell.ColumnNumber - 1 >= 0 && theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber - 1].CurrentlyOccupiedByOpponent)
                        theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber - 1].LegalNextMove = true;

                    // Capture diagonally right
                    if (currentCell.RowNumber - 1 >= 0 && currentCell.ColumnNumber + 1 < Size && theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber + 1].CurrentlyOccupiedByOpponent)
                        theGrid[currentCell.RowNumber - 1, currentCell.ColumnNumber + 1].LegalNextMove = true;
                    break;

                case "Pawn_Black":
                    // Move forward
                    if (currentCell.RowNumber + 1 < Size && !theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber].CurrentlyOccupied)
                        theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber].LegalNextMove = true;

                    // Capture diagonally left
                    if (currentCell.RowNumber + 1 < Size && currentCell.ColumnNumber - 1 >= 0 && theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber - 1].CurrentlyOccupiedByOpponent)
                        theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber - 1].LegalNextMove = true;

                    // Capture diagonally right
                    if (currentCell.RowNumber + 1 < Size && currentCell.ColumnNumber + 1 < Size && theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber + 1].CurrentlyOccupiedByOpponent)
                        theGrid[currentCell.RowNumber + 1, currentCell.ColumnNumber + 1].LegalNextMove = true;
                    break;

                case "King":
                    // One square in any direction
                    for (int rowOffset = -1; rowOffset <= 1; rowOffset++)
                    {
                        for (int colOffset = -1; colOffset <= 1; colOffset++)
                        {
                            // Skip the current cell
                            if (rowOffset == 0 && colOffset == 0) continue;
                            int newRow = currentCell.RowNumber + rowOffset;
                            int newCol = currentCell.ColumnNumber + colOffset;
                            if (newRow >= 0 && newRow < Size && newCol >= 0 && newCol < Size)
                            {
                                theGrid[newRow, newCol].LegalNextMove = true;
                            }
                        }
                    }
                    break;
            }
        }

      
    }
}
