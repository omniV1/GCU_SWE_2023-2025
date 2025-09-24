namespace DatabaseSQLMusicApp
{
    partial class DatabaseSQLMusicApp : Form
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
            button1 = new Button();
            dataGridView1 = new DataGridView();
            button2 = new Button();
            textBox1 = new TextBox();
            pictureBox1 = new PictureBox();
            groupBox1 = new GroupBox();
            txtAlbumName = new TextBox();
            txtArtistName = new TextBox();
            txtYearMade = new TextBox();
            txtImage_Url = new TextBox();
            lblImage_Url = new Label();
            lblDescription = new Label();
            lblYearMade = new Label();
            lblArtistName = new Label();
            txtDescription = new TextBox();
            lblAlbumName = new Label();
            btnAddAlbum = new Button();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            groupBox1.SuspendLayout();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(181, 33);
            button1.Name = "button1";
            button1.Size = new Size(83, 23);
            button1.TabIndex = 0;
            button1.Text = "Load albums";
            button1.UseVisualStyleBackColor = true;
            button1.Click += LoadAlbumOnClick;
            // 
            // dataGridView1
            // 
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Location = new Point(178, 62);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowTemplate.Height = 25;
            dataGridView1.Size = new Size(610, 192);
            dataGridView1.TabIndex = 1;
            dataGridView1.CellClick += dataGridView1_CellClick;
            // 
            // button2
            // 
            button2.Location = new Point(567, 35);
            button2.Name = "button2";
            button2.Size = new Size(75, 23);
            button2.TabIndex = 2;
            button2.Text = "Search";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(270, 35);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(291, 21);
            textBox1.TabIndex = 3;
            // 
            // pictureBox1
            // 
            pictureBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            pictureBox1.Location = new Point(12, 62);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(160, 192);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.TabIndex = 4;
            pictureBox1.TabStop = false;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(txtAlbumName);
            groupBox1.Controls.Add(txtArtistName);
            groupBox1.Controls.Add(txtYearMade);
            groupBox1.Controls.Add(txtImage_Url);
            groupBox1.Controls.Add(lblImage_Url);
            groupBox1.Controls.Add(lblDescription);
            groupBox1.Controls.Add(lblYearMade);
            groupBox1.Controls.Add(lblArtistName);
            groupBox1.Controls.Add(txtDescription);
            groupBox1.Controls.Add(lblAlbumName);
            groupBox1.Font = new Font("Times New Roman", 9F, FontStyle.Bold, GraphicsUnit.Point);
            groupBox1.Location = new Point(12, 260);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(344, 168);
            groupBox1.TabIndex = 5;
            groupBox1.TabStop = false;
            groupBox1.Text = "add albums";
            // 
            // txtAlbumName
            // 
            txtAlbumName.Location = new Point(201, 14);
            txtAlbumName.Name = "txtAlbumName";
            txtAlbumName.Size = new Size(100, 21);
            txtAlbumName.TabIndex = 12;
            // 
            // txtArtistName
            // 
            txtArtistName.Location = new Point(201, 39);
            txtArtistName.Name = "txtArtistName";
            txtArtistName.Size = new Size(100, 21);
            txtArtistName.TabIndex = 9;
            // 
            // txtYearMade
            // 
            txtYearMade.Location = new Point(201, 66);
            txtYearMade.Name = "txtYearMade";
            txtYearMade.Size = new Size(100, 21);
            txtYearMade.TabIndex = 10;
            // 
            // txtImage_Url
            // 
            txtImage_Url.Location = new Point(201, 90);
            txtImage_Url.Name = "txtImage_Url";
            txtImage_Url.Size = new Size(100, 21);
            txtImage_Url.TabIndex = 11;
            // 
            // lblImage_Url
            // 
            lblImage_Url.AutoSize = true;
            lblImage_Url.Location = new Point(3, 93);
            lblImage_Url.Name = "lblImage_Url";
            lblImage_Url.Size = new Size(65, 15);
            lblImage_Url.TabIndex = 4;
            lblImage_Url.Text = "Image URL";
            // 
            // lblDescription
            // 
            lblDescription.AutoSize = true;
            lblDescription.Location = new Point(3, 117);
            lblDescription.Name = "lblDescription";
            lblDescription.Size = new Size(207, 15);
            lblDescription.TabIndex = 3;
            lblDescription.Text = "Description (less than 500 characters) ";
            // 
            // lblYearMade
            // 
            lblYearMade.AutoSize = true;
            lblYearMade.Location = new Point(3, 69);
            lblYearMade.Name = "lblYearMade";
            lblYearMade.Size = new Size(62, 15);
            lblYearMade.TabIndex = 2;
            lblYearMade.Text = "Year made";
            // 
            // lblArtistName
            // 
            lblArtistName.AutoSize = true;
            lblArtistName.Location = new Point(3, 42);
            lblArtistName.Name = "lblArtistName";
            lblArtistName.Size = new Size(37, 15);
            lblArtistName.TabIndex = 1;
            lblArtistName.Text = "Artist";
            // 
            // txtDescription
            // 
            txtDescription.Location = new Point(201, 117);
            txtDescription.Name = "txtDescription";
            txtDescription.Size = new Size(100, 21);
            txtDescription.TabIndex = 6;
            // 
            // lblAlbumName
            // 
            lblAlbumName.AutoSize = true;
            lblAlbumName.Location = new Point(3, 17);
            lblAlbumName.Name = "lblAlbumName";
            lblAlbumName.Size = new Size(74, 15);
            lblAlbumName.TabIndex = 0;
            lblAlbumName.Text = "Album name";
            // 
            // btnAddAlbum
            // 
            btnAddAlbum.Location = new Point(132, 434);
            btnAddAlbum.Name = "btnAddAlbum";
            btnAddAlbum.Size = new Size(75, 23);
            btnAddAlbum.TabIndex = 5;
            btnAddAlbum.Text = "add album ";
            btnAddAlbum.UseVisualStyleBackColor = true;
            btnAddAlbum.Click += btnAddAlbum_Click;
            // 
            // DatabaseSQLMusicApp
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 495);
            Controls.Add(groupBox1);
            Controls.Add(pictureBox1);
            Controls.Add(textBox1);
            Controls.Add(button2);
            Controls.Add(btnAddAlbum);
            Controls.Add(dataGridView1);
            Controls.Add(button1);
            Font = new Font("Times New Roman", 9F, FontStyle.Regular, GraphicsUnit.Point);
            Name = "DatabaseSQLMusicApp";
            Text = "Music App";
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private DataGridView dataGridView1;
        private Button button2;
        private TextBox textBox1;
        private PictureBox pictureBox1;
        private GroupBox groupBox1;
        private Label lblImage_Url;
        private Label lblDescription;
        private Label lblYearMade;
        private Label lblArtistName;
        private Label lblAlbumName;
        private TextBox txtAlbumName;
        private TextBox txtArtistName;
        private TextBox txtYearMade;
        private TextBox txtImage_Url;
        private Button btnAddAlbum;
        private TextBox txtDescription;
    }
}