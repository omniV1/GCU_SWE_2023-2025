namespace ChessBoardGuiApp
{
    partial class ChessBoardForm
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
            lblInstructions = new Label();
            cmbSelectPieces = new ComboBox();
            pnlChessBoard = new Panel();
            SuspendLayout();
            // 
            // lblInstructions
            // 
            lblInstructions.AutoSize = true;
            lblInstructions.Font = new Font("Times New Roman", 12F, FontStyle.Bold, GraphicsUnit.Point);
            lblInstructions.Location = new Point(28, 23);
            lblInstructions.Name = "lblInstructions";
            lblInstructions.Size = new Size(380, 19);
            lblInstructions.TabIndex = 0;
            lblInstructions.Text = "select a piece to play and I will show you all legal moves";
            // 
            // cmbSelectPieces
            // 
            cmbSelectPieces.DropDownStyle = ComboBoxStyle.DropDownList;
            cmbSelectPieces.Font = new Font("Times New Roman", 12F, FontStyle.Regular, GraphicsUnit.Point);
            cmbSelectPieces.FormattingEnabled = true;
            cmbSelectPieces.Items.AddRange(new object[] { "Bishop", "King ", "Queen", "Rook", "Knight", "Pawn_White", "Pawn_Black" });
            cmbSelectPieces.Location = new Point(451, 20);
            cmbSelectPieces.Name = "cmbSelectPieces";
            cmbSelectPieces.Size = new Size(121, 27);
            cmbSelectPieces.TabIndex = 1;
            cmbSelectPieces.SelectedIndexChanged += CmbSelectPieces_SelectedIndexChanged;
            // 
            // pnlChessBoard
            // 
            pnlChessBoard.Location = new Point(12, 64);
            pnlChessBoard.Name = "pnlChessBoard";
            pnlChessBoard.Size = new Size(560, 482);
            pnlChessBoard.TabIndex = 2;
            // 
            // ChessBoardForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(587, 558);
            Controls.Add(pnlChessBoard);
            Controls.Add(cmbSelectPieces);
            Controls.Add(lblInstructions);
            Name = "ChessBoardForm";
            Text = "Chess";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblInstructions;
        private ComboBox cmbSelectPieces;
        private Panel pnlChessBoard;
    }
}