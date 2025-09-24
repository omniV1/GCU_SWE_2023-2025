using ChessBoardModel;
using System.ComponentModel.DataAnnotations.Schema;

namespace ChessBoardGuiApp
{
    public partial class ChessBoardForm : Form
    {
        private string selectedPiece;
        static public Board myBoard = new Board(8);
        public Button[,] btnGrid = new Button[myBoard.Size, myBoard.Size];

        public ChessBoardForm()
        {
            InitializeComponent();
            PopulateGrid();
        }
        public void PopulateGrid()
        {
            //This function will fill the pnlChessBoard control w buttons
            // cal the button width of each button on the Grid 
            int buttonSize = pnlChessBoard.Width / myBoard.Size;
            // set the grid to be square
            pnlChessBoard.Height = pnlChessBoard.Width;

            // nested loop. create buttons and place them in the panel
            for (int r = 0; r < myBoard.Size; r++)
            {
                for (int c = 0; c < myBoard.Size; c++)
                {
                    btnGrid[r, c] = new Button();

                    //Make each button square
                    btnGrid[r, c].Width = buttonSize;
                    btnGrid[r, c].Height = buttonSize;

                    // add same click event to each button 
                    btnGrid[r, c].Click += Grid_Button_Click;

                    //place the button on the panel
                    pnlChessBoard.Controls.Add(btnGrid[r, c]);

                    //postition it in x,y
                    btnGrid[r, c].Location = new Point(buttonSize * r, buttonSize * c);

                    //for testing purposes remove later
                    btnGrid[r, c].Text = r.ToString() + "|" + c.ToString();

                    // the Tag attribute will hold the row and column number in a string 
                    btnGrid[r, c].Tag = r.ToString() + "|" + c.ToString();
                }

            }
        }

        // This method is called when a grid button is clicked.
        private void Grid_Button_Click(object sender, EventArgs e)
        {
            Button clickedButton = (Button)sender;
            string[] position = clickedButton.Tag.ToString().Split('|');
            int row = int.Parse(position[0]);
            int col = int.Parse(position[1]);

            // Reset all cells to not occupied before setting the new piece
            ResetBoardOccupation();

            // Set the current cell to occupied
            myBoard.theGrid[row, col].CurrentlyOccupied = true;

            // Run the helper function to mark legal moves
            myBoard.MarkNextLegalMoves(myBoard.theGrid[row, col], selectedPiece);

            // Update the button labels to reflect the changes
            UpdateButtonLabels(selectedPiece);
        }

        // This resets the CurrentlyOccupied property for all cells on the board.
        private void ResetBoardOccupation()
        {
            foreach (Cell cell in myBoard.theGrid)
            {
                cell.CurrentlyOccupied = false;
            }
        }

        // This method updates the text of the buttons on the grid.
        public void UpdateButtonLabels(string chessPiece)
        {
            for (int r = 0; r < myBoard.Size; r++)
            {
                for (int c = 0; c < myBoard.Size; c++)
                {
                    btnGrid[r, c].Text = "";
                    if (myBoard.theGrid[r, c].CurrentlyOccupied)
                        btnGrid[r, c].Text = chessPiece;
                    else if (myBoard.theGrid[r, c].LegalNextMove)
                        btnGrid[r, c].Text = "Legal";
                }
            }
        }

        // This method is called when the selected item in the ComboBox changes.
        private void CmbSelectPieces_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Update the selectedPiece variable with the selected item from the ComboBox
            selectedPiece = cmbSelectPieces.SelectedItem.ToString();

            // Assuming you want to reset the board each time you change the selection
            ResetBoardOccupation();

            // Refresh the board
            UpdateButtonLabels(selectedPiece);
        }

    }
}
