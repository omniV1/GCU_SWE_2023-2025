using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessBoardModel
{
   public class Cell
    {
        // row and col are the cell's location on the grid.
        public int RowNumber { get; set; }
        public int ColumnNumber { get; set; }

        // T/F is there a chess piece on this cell? 
        public bool CurrentlyOccupied { get; set; }

        // T/F is there a chess piece on this cell? 
        public bool CurrentlyOccupiedByOpponent { get; set; }

        //is this square a legal move for the chess piece on the board? 
        public bool LegalNextMove { get; set; }

        // constructor
        public Cell(int row, int col)
        {
            RowNumber = row;
            ColumnNumber = col;
            CurrentlyOccupied = false;
            CurrentlyOccupiedByOpponent = false;
            LegalNextMove = false;
        }
    }
}