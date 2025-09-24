namespace MinesweeperGui.PresentationLayer
{
    partial class FrmHighScores
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FrmHighScores));
            dgvHighScores = new DataGridView();
            lblHighScore = new Label();
            ((System.ComponentModel.ISupportInitialize)dgvHighScores).BeginInit();
            SuspendLayout();
            // 
            // dgvHighScores
            // 
            dgvHighScores.BackgroundColor = Color.Thistle;
            dgvHighScores.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dgvHighScores.Location = new Point(12, 96);
            dgvHighScores.Name = "dgvHighScores";
            dgvHighScores.Size = new Size(342, 342);
            dgvHighScores.TabIndex = 0;
            // 
            // lblHighScore
            // 
            lblHighScore.AutoSize = true;
            lblHighScore.Font = new Font("Palatino Linotype", 18F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblHighScore.Location = new Point(70, 33);
            lblHighScore.Name = "lblHighScore";
            lblHighScore.Size = new Size(205, 32);
            lblHighScore.TabIndex = 1;
            lblHighScore.Text = "Top 5 High Scores";
            // 
            // FrmHighScores
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.Honeydew;
            ClientSize = new Size(366, 450);
            Controls.Add(lblHighScore);
            Controls.Add(dgvHighScores);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "FrmHighScores";
            Text = "High Score";
            ((System.ComponentModel.ISupportInitialize)dgvHighScores).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DataGridView dgvHighScores;
        private Label lblHighScore;
    }
}