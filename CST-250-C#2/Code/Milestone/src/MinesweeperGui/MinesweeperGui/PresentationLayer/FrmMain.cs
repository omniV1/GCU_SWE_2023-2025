using MinesweeperGui.BusinessLayer;
using MinesweeperGui.PresentationLayer;
using System.Diagnostics;


namespace MinesweeperGui
{
    public partial class FrmMain : Form
    {
        private readonly Board _board = new(10); // Initialize the game board with size 10x10.
        private readonly Stopwatch _stopwatch = new Stopwatch(); // Stopwatch to track game duration.

        // Constructor that initializes the board based on the selected difficulty.
        public FrmMain(string difficulty)
        {
            InitializeComponent();

            // Reset Visited property after InitializeComponent
            foreach (Cell cell in _board.Grid)
            {
                cell.Visited = false;
            }

            InitializeBoard(difficulty);
        }

        // Sets the game's difficulty and initializes the game board.
        private void InitializeBoard(string difficulty)
        {
            SetDifficulty(difficulty); // Set the game difficulty.
            _board.SetupLiveNeighbors(); // Place mines on the board.
            _board.CalculateLiveNeighbors(); // Calculate the number of neighboring mines for each cell.
            _stopwatch.Restart(); // Restart the stopwatch at the beginning of a new game.
            CreateGridButtons(); // Dynamically create grid buttons based on board size.
        }

        // Adjusts the board's difficulty setting based on player selection.
        private void SetDifficulty(string difficulty)
        {
            switch (difficulty)
            {
                case "Easy":
                    _board.Difficulty = 0.1f;
                    break;
                case "Medium":
                    _board.Difficulty = 0.15f;
                    break;
                case "Hard":
                    _board.Difficulty = 0.2f;
                    break;
                default:
                    _board.Difficulty = 0.1f; // Default to easy if difficulty is not recognized.
                    break;
            }
        }

        // Creates buttons for each cell in the game board and adds them to the layout panel.
        private void CreateGridButtons()
        {
            for (int row = 0; row < _board.Size; row++)
            {
                for (int column = 0; column < _board.Size; column++)
                {
                    var button = new Button
                    {
                        Dock = DockStyle.Fill,
                        Margin = new Padding(0),
                        Name = $"ButtonRow{row}Column{column}",
                        Tag = _board.Grid[row, column] // Associate this button with its corresponding cell.
                    };

                    button.Click += BtnChangeCellState_click; // Click event for revealing cells.
                    button.MouseUp += BtnFlagged_MouseUp; // Right-click event for flagging cells.
                    MinesweeperTableLayout.Controls.Add(button, column, row); // Add the button to the table layout panel.
                    
                }
            }
        }

        private void BtnChangeCellState_click(object sender, EventArgs e)
        {
            if (sender is Button button && button.Tag is Cell cell)
            {
                if (!cell.Visited && !cell.Flagged)
                {
                    button.BackColor = Color.Gray; // Visual feedback for processing click.

                    if (cell.Live)
                    {
                        cell.Visited = true; // Mark this cell as visited
                        ShowAllBombs();
                        _stopwatch.Stop();
                        MessageBox.Show($"Game Over. Time: {_stopwatch.Elapsed.ToString(@"mm\:ss")}");
                    }
                    else if (cell.LiveNeighbors > 0)
                    {
                        cell.Visited = true; // Mark this cell as visited
                        button.Text = cell.LiveNeighbors.ToString();
                        button.BackColor = Color.LightGreen;
                    }
                    else
                    {
                        // Perform flood fill from this cell if there are no live neighbors
                        _board.FloodFill(cell.Row, cell.Column, UpdateButtonDisplay);
                    }
                    CheckForWin();
                }
                else
                {
                    Debug.WriteLine($"Attempt to interact with already visited or flagged cell: ({cell.Row}, {cell.Column}) - Visited: {cell.Visited}, Flagged: {cell.Flagged}");
                }
            }
        }




        // Checks if all non-mine cells have been revealed, indicating a win.
        private void CheckForWin()
        {
            bool won = true;
            foreach (Cell cell in _board.Grid)
            {
                if (!cell.Live && !cell.Visited)
                {
                    won = false;
                    break;
                }
            }

            if (won)
            {
                _stopwatch.Stop();
                MessageBox.Show($"Congratulations, you won! Time: {_stopwatch.Elapsed.ToString(@"mm\:ss")}");
                UpdateHighScores(true);  // true indicates a win
                ShowHighScoresForm();
            }
        }


        // Handles right-clicks for flagging potential mine cells.
        private void BtnFlagged_MouseUp(object sender, MouseEventArgs e)
        {
            if (sender is Button button && button.Tag is Cell cell && e.Button == MouseButtons.Right && !cell.Visited)
            {
                cell.Flagged = !cell.Flagged; // Toggle flag state.

                // Update button image based on flag state.
                if (cell.Flagged)
                {
                    if (button.BackgroundImage == null)  // Ensure we're not setting the image again if it's already set
                    {
                        button.BackgroundImage = GetFlagImage(); // GetFlagImage() should return the Image for a flagged state
                    }
                }
                else
                {
                    button.BackgroundImage = null; // Clear the background image if not flagged
                }

                button.BackgroundImageLayout = ImageLayout.Stretch;  // Ensures the image fits the button
                button.Invalidate(); // Forces the button to redraw, updating the visual state
            }
        }


        private void ShowAllBombs()
        {
            _board.RevealAllBombs(); // Reveal all bombs on the board.

            // Iterate through all buttons in the layout and update their appearance if they represent a bomb.
            foreach (Control control in MinesweeperTableLayout.Controls)
            {
                if (control is Button button && button.Tag is Cell cell && cell.Live)
                {
                    button.BackgroundImage = GetBombImage(); // Display bomb image.
                    button.BackgroundImageLayout = ImageLayout.Stretch; // Ensure the image fits the button.
                }
            }
            _stopwatch.Stop(); // Stop the stopwatch as the game is over.
            MessageBox.Show($"Game Over. Time: {_stopwatch.Elapsed.ToString(@"mm\:ss")}");
            UpdateHighScores(false);  // assuming false indicates a loss
            ShowHighScoresForm();
        }

        // Retrieves the image used to indicate a cell is flagged.
        private Image GetFlagImage()
        {
            // Adjust the path as necessary for your project structure.
            return Image.FromFile(@"C:\Users\Owenl\source\repos\250\Milestone\src\MinesweeperGui\MinesweeperGui\Images\flag-16.png");
        }

        // Retrieves the image used to indicate a cell contains a bomb.
        private Image GetBombImage()
        {
            // Adjust the path as necessary for your project structure.
            return Image.FromFile(@"C:\Users\Owenl\source\repos\250\Milestone\src\MinesweeperGui\MinesweeperGui\Images\bomb-3-16.png");
        }

        // Updates the display for a specific cell based on its state.
        private void UpdateButtonDisplay(Cell cell)
        {
            if (this.InvokeRequired)
            {
                this.Invoke(new Action(() => UpdateButtonDisplay(cell)));
            }
            else
            {
                Button button = MinesweeperTableLayout.Controls.OfType<Button>().FirstOrDefault(b => b.Tag == cell);
                if (button != null)
                {
                    button.Enabled = false; // Disable the button to prevent further interaction.
                    button.BackColor = Color.LightGreen; // Indicative of a safe cell
                    button.Text = cell.LiveNeighbors > 0 ? cell.LiveNeighbors.ToString() : "";
                }
            }
        }

        private void UpdateHighScores(bool won)
        {
            var playerStats = new PlayerStats
            {
                PlayerInitials = "ABC", // You might want to get this from the user
                Difficulty = "Easy", // Or however you track difficulty
                TimeElapsed = _stopwatch.Elapsed
            };

            var highScores = HighScoresManager.LoadHighScores("HighScores.txt");
            highScores.Add(playerStats);
            highScores = highScores.OrderBy(score => score).Take(5).ToList(); // Sort and take the top 5 scores
            HighScoresManager.SaveHighScores(highScores, "HighScores.txt");
        }

        private void ShowHighScoresForm()
        {
            FrmHighScores highScoresForm = new FrmHighScores();
            highScoresForm.ShowDialog();
        }


    }
}
    

