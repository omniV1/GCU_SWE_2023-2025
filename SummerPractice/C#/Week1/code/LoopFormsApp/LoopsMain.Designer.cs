namespace LoopFormsApp
{
    partial class LoopsMain
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblPrompt = new Label();
            txtSentence = new TextBox();
            rbDisplayVowel = new RadioButton();
            rbDisplayCon = new RadioButton();
            btnResult = new Button();
            lblResults = new Label();
            SuspendLayout();
            // 
            // lblPrompt
            // 
            lblPrompt.AutoSize = true;
            lblPrompt.Location = new Point(177, 43);
            lblPrompt.Name = "lblPrompt";
            lblPrompt.Size = new Size(212, 21);
            lblPrompt.TabIndex = 0;
            lblPrompt.Text = "Enter text up to 100 chars. ";
            // 
            // txtSentence
            // 
            txtSentence.BackColor = Color.AliceBlue;
            txtSentence.Location = new Point(97, 87);
            txtSentence.Name = "txtSentence";
            txtSentence.Size = new Size(374, 29);
            txtSentence.TabIndex = 1;
            // 
            // rbDisplayVowel
            // 
            rbDisplayVowel.AutoSize = true;
            rbDisplayVowel.Location = new Point(98, 140);
            rbDisplayVowel.Name = "rbDisplayVowel";
            rbDisplayVowel.Size = new Size(138, 25);
            rbDisplayVowel.TabIndex = 2;
            rbDisplayVowel.TabStop = true;
            rbDisplayVowel.Text = "display vowels";
            rbDisplayVowel.UseVisualStyleBackColor = true;
            // 
            // rbDisplayCon
            // 
            rbDisplayCon.AutoSize = true;
            rbDisplayCon.Location = new Point(97, 192);
            rbDisplayCon.Name = "rbDisplayCon";
            rbDisplayCon.Size = new Size(176, 25);
            rbDisplayCon.TabIndex = 3;
            rbDisplayCon.TabStop = true;
            rbDisplayCon.Text = "display consonants ";
            rbDisplayCon.UseVisualStyleBackColor = true;
            // 
            // btnResult
            // 
            btnResult.BackColor = Color.AliceBlue;
            btnResult.Location = new Point(213, 270);
            btnResult.Name = "btnResult";
            btnResult.Size = new Size(75, 31);
            btnResult.TabIndex = 4;
            btnResult.Text = "Click";
            btnResult.UseVisualStyleBackColor = false;
            btnResult.Click += BtnResult_Click;
            // 
            // lblResults
            // 
            lblResults.Location = new Point(103, 304);
            lblResults.Name = "lblResults";
            lblResults.Size = new Size(286, 266);
            lblResults.TabIndex = 5;
            // 
            // LoopsMain
            // 
            AutoScaleDimensions = new SizeF(10F, 21F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.LavenderBlush;
            ClientSize = new Size(546, 579);
            Controls.Add(lblResults);
            Controls.Add(btnResult);
            Controls.Add(rbDisplayCon);
            Controls.Add(rbDisplayVowel);
            Controls.Add(txtSentence);
            Controls.Add(lblPrompt);
            Font = new Font("Times New Roman", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            Margin = new Padding(4);
            Name = "LoopsMain";
            Text = "Loops practice ";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblPrompt;
        private TextBox txtSentence;
        private RadioButton rbDisplayVowel;
        private RadioButton rbDisplayCon;
        private Button btnResult;
        private Label lblResults;
    }
}
