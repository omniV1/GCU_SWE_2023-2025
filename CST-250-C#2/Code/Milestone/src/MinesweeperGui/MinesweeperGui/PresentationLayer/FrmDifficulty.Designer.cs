namespace MinesweeperGui.PresentationLayer
{
    partial class FrmDifficulty
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FrmDifficulty));
            btnPlayGame = new Button();
            rbEasy = new RadioButton();
            rbIntermediate = new RadioButton();
            rbHard = new RadioButton();
            textBox1 = new TextBox();
            btnHighScores = new Button();
            lblEnterName = new Label();
            gbInitials = new GroupBox();
            groupBox1 = new GroupBox();
            gbInitials.SuspendLayout();
            groupBox1.SuspendLayout();
            SuspendLayout();
            // 
            // btnPlayGame
            // 
            btnPlayGame.Location = new Point(190, 280);
            btnPlayGame.Name = "btnPlayGame";
            btnPlayGame.Size = new Size(102, 41);
            btnPlayGame.TabIndex = 1;
            btnPlayGame.Text = "Play Game";
            btnPlayGame.UseVisualStyleBackColor = true;
            btnPlayGame.Click += BtnStartGame_Click;
            // 
            // rbEasy
            // 
            rbEasy.AutoSize = true;
            rbEasy.Location = new Point(81, 69);
            rbEasy.Name = "rbEasy";
            rbEasy.Size = new Size(48, 19);
            rbEasy.TabIndex = 2;
            rbEasy.TabStop = true;
            rbEasy.Text = "Easy";
            rbEasy.UseVisualStyleBackColor = true;
            // 
            // rbIntermediate
            // 
            rbIntermediate.AutoSize = true;
            rbIntermediate.Location = new Point(81, 108);
            rbIntermediate.Name = "rbIntermediate";
            rbIntermediate.Size = new Size(92, 19);
            rbIntermediate.TabIndex = 3;
            rbIntermediate.TabStop = true;
            rbIntermediate.Text = "intermediate";
            rbIntermediate.UseVisualStyleBackColor = true;
            // 
            // rbHard
            // 
            rbHard.AutoSize = true;
            rbHard.Location = new Point(81, 153);
            rbHard.Name = "rbHard";
            rbHard.Size = new Size(51, 19);
            rbHard.TabIndex = 4;
            rbHard.TabStop = true;
            rbHard.Text = "Hard";
            rbHard.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(61, 88);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(100, 23);
            textBox1.TabIndex = 5;
            textBox1.TextAlign = HorizontalAlignment.Center;
            // 
            // btnHighScores
            // 
            btnHighScores.Location = new Point(46, 149);
            btnHighScores.Name = "btnHighScores";
            btnHighScores.Size = new Size(131, 23);
            btnHighScores.TabIndex = 6;
            btnHighScores.Text = "View high scores";
            btnHighScores.UseVisualStyleBackColor = true;
            // 
            // lblEnterName
            // 
            lblEnterName.AutoSize = true;
            lblEnterName.Location = new Point(61, 46);
            lblEnterName.Name = "lblEnterName";
            lblEnterName.Size = new Size(103, 15);
            lblEnterName.TabIndex = 7;
            lblEnterName.Text = "Enter Player Initals";
            // 
            // gbInitials
            // 
            gbInitials.Controls.Add(lblEnterName);
            gbInitials.Controls.Add(textBox1);
            gbInitials.Controls.Add(btnHighScores);
            gbInitials.Location = new Point(12, 12);
            gbInitials.Name = "gbInitials";
            gbInitials.Size = new Size(228, 228);
            gbInitials.TabIndex = 8;
            gbInitials.TabStop = false;
            gbInitials.Text = "Start";
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(rbEasy);
            groupBox1.Controls.Add(rbHard);
            groupBox1.Controls.Add(rbIntermediate);
            groupBox1.Location = new Point(246, 22);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(243, 218);
            groupBox1.TabIndex = 9;
            groupBox1.TabStop = false;
            groupBox1.Text = "Select Score Multiplier";
            // 
            // FrmDifficulty
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.Honeydew;
            ClientSize = new Size(494, 450);
            Controls.Add(groupBox1);
            Controls.Add(gbInitials);
            Controls.Add(btnPlayGame);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "FrmDifficulty";
            Text = "Select Difficulty";
            gbInitials.ResumeLayout(false);
            gbInitials.PerformLayout();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion
        private Button btnPlayGame;
        private RadioButton rbEasy;
        private RadioButton rbIntermediate;
        private RadioButton rbHard;
        private TextBox textBox1;
        private Button btnHighScores;
        private Label lblEnterName;
        private GroupBox gbInitials;
        private GroupBox groupBox1;
    }
}