namespace MinesweeperGui
{ 
    partial class FrmMain
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FrmMain));
            MinesweeperTableLayout = new TableLayoutPanel();
            SuspendLayout();
            // 
            // MinesweeperTableLayout
            // 
            MinesweeperTableLayout.BackColor = Color.Lavender;
            MinesweeperTableLayout.BackgroundImageLayout = ImageLayout.None;
            MinesweeperTableLayout.CellBorderStyle = TableLayoutPanelCellBorderStyle.Single;
            MinesweeperTableLayout.ColumnCount = 10;
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10.125F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 9.875F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.Dock = DockStyle.Fill;
            MinesweeperTableLayout.Location = new Point(0, 0);
            MinesweeperTableLayout.Name = "MinesweeperTableLayout";
            MinesweeperTableLayout.RowCount = 10;
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 10F));
            MinesweeperTableLayout.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            MinesweeperTableLayout.Size = new Size(410, 474);
            MinesweeperTableLayout.TabIndex = 0;
            // 
            // FrmMain
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(410, 474);
            Controls.Add(MinesweeperTableLayout);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "FrmMain";
            Text = "Minesweeper";
            ResumeLayout(false);
        }

        #endregion
        private TableLayoutPanel MinesweeperTableLayout;
    }
}
