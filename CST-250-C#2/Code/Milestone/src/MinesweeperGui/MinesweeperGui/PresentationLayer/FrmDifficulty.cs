using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MinesweeperGui.PresentationLayer
{
    public partial class FrmDifficulty : Form
    {
        public string SelectedDifficulty { get; private set; }

        public FrmDifficulty()
        {
            InitializeComponent();

            InitializePlayer();
        }
        private void InitializePlayer()
        {
          
            btnHighScores.Click += BtnHighScores_OnClick;
            
        }

        private void BtnStartGame_Click(object sender, EventArgs e)
        {
            if (rbEasy.Checked)
            {
                SelectedDifficulty = "Easy";
            }
            else if (rbIntermediate.Checked)
            {
                SelectedDifficulty = "Intermediate";
            }
            else if (rbHard.Checked)
            {
                SelectedDifficulty = "Hard";
            }

            this.DialogResult = DialogResult.OK; // To close the difficulty selection form
        }

        private void BtnHighScores_OnClick(object sender, EventArgs e)
        {
            FrmHighScores frmHighScores = new FrmHighScores(); 
            frmHighScores.ShowDialog(); 

        }
    }
}
