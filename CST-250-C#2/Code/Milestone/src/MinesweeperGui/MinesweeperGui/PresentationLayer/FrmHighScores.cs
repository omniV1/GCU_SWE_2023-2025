using MinesweeperGui.BusinessLayer;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace MinesweeperGui.PresentationLayer
{
    public partial class FrmHighScores : Form
    {
        private List<PlayerStats> highScores;

        public FrmHighScores()
        {
            InitializeComponent();
            LoadHighScores();
            DisplayHighScores();
        }

        private void LoadHighScores()
        {
            string filePath = @"C:\Users\Owenl\source\repos\250\Milestone\src\MinesweeperGui\MinesweeperGui\Utility\HighScores.txt";
            highScores = new List<PlayerStats>();

            try
            {
                var lines = File.ReadAllLines(filePath);
                foreach (var line in lines)
                {
                    highScores.Add(PlayerStats.FromString(line));
                }

                // Sort the list
                highScores.Sort();
            }
            catch (IOException ex)
            {
                MessageBox.Show("There was a problem reading the high scores file: " + ex.Message);
            }
        }

        private void DisplayHighScores()
        {
            // Assuming the path to the file is defined as a constant or accessible from configuration
            string filePath = @"C:\Users\Owenl\source\repos\250\Milestone\src\MinesweeperGui\MinesweeperGui\Utility\HighScores.txt";
            var highScores = HighScoresManager.LoadHighScores(filePath);

            // Sort the list based on scores using the implemented IComparable in PlayerStats
            var sortedScores = highScores.OrderByDescending(score => score.Score).ToList();

            // Displaying data in DataGridView
            dgvHighScores.DataSource = sortedScores.Select(score => new {
                Initials = score.PlayerInitials,
                Difficulty = score.Difficulty,
                Time = score.TimeElapsed.ToString(@"mm\:ss"),
                Score = score.Score
            }).ToList();

           // Set column headers 
            dgvHighScores.Columns["Initials"].HeaderText = "Player Initials";
            dgvHighScores.Columns["Difficulty"].HeaderText = "Difficulty Level";
            dgvHighScores.Columns["Time"].HeaderText = "Completion Time";
            dgvHighScores.Columns["Score"].HeaderText = "Score";
            dgvHighScores.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill; // Adjust columns to fill the grid

            dgvHighScores.ReadOnly = true;
            dgvHighScores.AllowUserToAddRows = false;
            dgvHighScores.RowHeadersVisible = false;
        }


    }
}
