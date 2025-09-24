namespace MongoDBMusicApp
{
    partial class FrmMain : Form
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
            btnShowallAlbums = new Button();
            dataGridView_albums = new DataGridView();
            BtnSearch = new Button();
            txtSearchAlbum = new TextBox();
            pbAlbumArt = new PictureBox();
            groupBox1 = new GroupBox();
            txtTitle = new TextBox();
            txtArtistName = new TextBox();
            txtYearMade = new TextBox();
            txtImage_Url = new TextBox();
            btnAddAlbum = new Button();
            lblImage_Url = new Label();
            lblDescription = new Label();
            lblYearMade = new Label();
            lblArtistName = new Label();
            txtDescription = new TextBox();
            lblTitle = new Label();
            dataGridView_tracks = new DataGridView();
            gbTracks = new GroupBox();
            btnAddTrack = new Button();
            txt_TrackVideoURL = new TextBox();
            txt_TrackTitle = new TextBox();
            lblVideoURL = new Label();
            label1 = new Label();
            btnShowAllTracks = new Button();
            txtSearchTracks = new TextBox();
            btnSearchTracks = new Button();
            btnDeleteSelectedAlbum = new Button();
            btnDeleteSelectedTrack = new Button();
            webView2 = new Microsoft.Web.WebView2.WinForms.WebView2();
            ((System.ComponentModel.ISupportInitialize)dataGridView_albums).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pbAlbumArt).BeginInit();
            groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridView_tracks).BeginInit();
            gbTracks.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)webView2).BeginInit();
            SuspendLayout();
            // 
            // btnShowallAlbums
            // 
            btnShowallAlbums.Location = new Point(244, 40);
            btnShowallAlbums.Name = "btnShowallAlbums";
            btnShowallAlbums.Size = new Size(121, 23);
            btnShowallAlbums.TabIndex = 0;
            btnShowallAlbums.Text = "Show all albums";
            btnShowallAlbums.UseVisualStyleBackColor = true;
            btnShowallAlbums.Click += BtnShowAllAlbums;
            // 
            // dataGridView_albums
            // 
            dataGridView_albums.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView_albums.Location = new Point(244, 69);
            dataGridView_albums.Name = "dataGridView_albums";
            dataGridView_albums.RowTemplate.Height = 25;
            dataGridView_albums.Size = new Size(610, 192);
            dataGridView_albums.TabIndex = 1;
            dataGridView_albums.CellContentClick += dataGridView_albums_CellClick;
            // 
            // BtnSearch
            // 
            BtnSearch.Location = new Point(684, 39);
            BtnSearch.Name = "BtnSearch";
            BtnSearch.Size = new Size(75, 23);
            BtnSearch.TabIndex = 2;
            BtnSearch.Text = "Search";
            BtnSearch.UseVisualStyleBackColor = true;
            BtnSearch.Click += BtnSearchAlbum_Click;
            // 
            // txtSearchAlbum
            // 
            txtSearchAlbum.Location = new Point(371, 40);
            txtSearchAlbum.Name = "txtSearchAlbum";
            txtSearchAlbum.Size = new Size(291, 21);
            txtSearchAlbum.TabIndex = 3;
            // 
            // pbAlbumArt
            // 
            pbAlbumArt.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            pbAlbumArt.Location = new Point(871, 69);
            pbAlbumArt.Name = "pbAlbumArt";
            pbAlbumArt.Size = new Size(244, 197);
            pbAlbumArt.SizeMode = PictureBoxSizeMode.Zoom;
            pbAlbumArt.TabIndex = 4;
            pbAlbumArt.TabStop = false;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(txtTitle);
            groupBox1.Controls.Add(txtArtistName);
            groupBox1.Controls.Add(txtYearMade);
            groupBox1.Controls.Add(txtImage_Url);
            groupBox1.Controls.Add(btnAddAlbum);
            groupBox1.Controls.Add(lblImage_Url);
            groupBox1.Controls.Add(lblDescription);
            groupBox1.Controls.Add(lblYearMade);
            groupBox1.Controls.Add(lblArtistName);
            groupBox1.Controls.Add(txtDescription);
            groupBox1.Controls.Add(lblTitle);
            groupBox1.Font = new Font("Times New Roman", 9F, FontStyle.Bold, GraphicsUnit.Point);
            groupBox1.Location = new Point(2, 46);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(236, 272);
            groupBox1.TabIndex = 5;
            groupBox1.TabStop = false;
            groupBox1.Text = "add albums";
            // 
            // txtTitle
            // 
            txtTitle.Location = new Point(6, 41);
            txtTitle.Name = "txtTitle";
            txtTitle.Size = new Size(216, 21);
            txtTitle.TabIndex = 12;
            // 
            // txtArtistName
            // 
            txtArtistName.Location = new Point(6, 83);
            txtArtistName.Name = "txtArtistName";
            txtArtistName.Size = new Size(216, 21);
            txtArtistName.TabIndex = 9;
            // 
            // txtYearMade
            // 
            txtYearMade.Location = new Point(6, 125);
            txtYearMade.Name = "txtYearMade";
            txtYearMade.Size = new Size(216, 21);
            txtYearMade.TabIndex = 10;
            // 
            // txtImage_Url
            // 
            txtImage_Url.Location = new Point(6, 167);
            txtImage_Url.Name = "txtImage_Url";
            txtImage_Url.Size = new Size(216, 21);
            txtImage_Url.TabIndex = 11;
            // 
            // btnAddAlbum
            // 
            btnAddAlbum.Location = new Point(70, 236);
            btnAddAlbum.Name = "btnAddAlbum";
            btnAddAlbum.Size = new Size(75, 23);
            btnAddAlbum.TabIndex = 5;
            btnAddAlbum.Text = "add album ";
            btnAddAlbum.UseVisualStyleBackColor = true;
            btnAddAlbum.Click += BtnAddAlbum_Click;
            // 
            // lblImage_Url
            // 
            lblImage_Url.AutoSize = true;
            lblImage_Url.Location = new Point(6, 149);
            lblImage_Url.Name = "lblImage_Url";
            lblImage_Url.Size = new Size(65, 15);
            lblImage_Url.TabIndex = 4;
            lblImage_Url.Text = "Image URL";
            // 
            // lblDescription
            // 
            lblDescription.AutoSize = true;
            lblDescription.Location = new Point(6, 191);
            lblDescription.Name = "lblDescription";
            lblDescription.Size = new Size(207, 15);
            lblDescription.TabIndex = 3;
            lblDescription.Text = "Description (less than 500 characters) ";
            // 
            // lblYearMade
            // 
            lblYearMade.AutoSize = true;
            lblYearMade.Location = new Point(6, 107);
            lblYearMade.Name = "lblYearMade";
            lblYearMade.Size = new Size(62, 15);
            lblYearMade.TabIndex = 2;
            lblYearMade.Text = "Year made";
            // 
            // lblArtistName
            // 
            lblArtistName.AutoSize = true;
            lblArtistName.Location = new Point(6, 65);
            lblArtistName.Name = "lblArtistName";
            lblArtistName.Size = new Size(37, 15);
            lblArtistName.TabIndex = 1;
            lblArtistName.Text = "Artist";
            // 
            // txtDescription
            // 
            txtDescription.Location = new Point(6, 209);
            txtDescription.Name = "txtDescription";
            txtDescription.Size = new Size(216, 21);
            txtDescription.TabIndex = 6;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Location = new Point(6, 23);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(33, 15);
            lblTitle.TabIndex = 0;
            lblTitle.Text = "Title";
            // 
            // dataGridView_tracks
            // 
            dataGridView_tracks.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView_tracks.Location = new Point(244, 305);
            dataGridView_tracks.Name = "dataGridView_tracks";
            dataGridView_tracks.RowTemplate.Height = 25;
            dataGridView_tracks.Size = new Size(610, 197);
            dataGridView_tracks.TabIndex = 6;
            dataGridView_tracks.CellClick += dgvTracks_CellClick;
            // 
            // gbTracks
            // 
            gbTracks.Controls.Add(btnAddTrack);
            gbTracks.Controls.Add(txt_TrackVideoURL);
            gbTracks.Controls.Add(txt_TrackTitle);
            gbTracks.Controls.Add(lblVideoURL);
            gbTracks.Controls.Add(label1);
            gbTracks.Location = new Point(2, 324);
            gbTracks.Name = "gbTracks";
            gbTracks.Size = new Size(236, 178);
            gbTracks.TabIndex = 7;
            gbTracks.TabStop = false;
            gbTracks.Text = "add Tracks";
            // 
            // btnAddTrack
            // 
            btnAddTrack.Location = new Point(70, 135);
            btnAddTrack.Name = "btnAddTrack";
            btnAddTrack.Size = new Size(69, 24);
            btnAddTrack.TabIndex = 13;
            btnAddTrack.Text = "add track";
            btnAddTrack.UseVisualStyleBackColor = true;
            btnAddTrack.Click += AddTrack_Click;
            // 
            // txt_TrackVideoURL
            // 
            txt_TrackVideoURL.Location = new Point(6, 91);
            txt_TrackVideoURL.Name = "txt_TrackVideoURL";
            txt_TrackVideoURL.Size = new Size(100, 21);
            txt_TrackVideoURL.TabIndex = 8;
            // 
            // txt_TrackTitle
            // 
            txt_TrackTitle.Location = new Point(6, 44);
            txt_TrackTitle.Name = "txt_TrackTitle";
            txt_TrackTitle.Size = new Size(100, 21);
            txt_TrackTitle.TabIndex = 8;
            // 
            // lblVideoURL
            // 
            lblVideoURL.AutoSize = true;
            lblVideoURL.Location = new Point(10, 73);
            lblVideoURL.Name = "lblVideoURL";
            lblVideoURL.Size = new Size(61, 15);
            lblVideoURL.TabIndex = 8;
            lblVideoURL.Text = "Video URL";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(10, 26);
            label1.Name = "label1";
            label1.Size = new Size(61, 15);
            label1.TabIndex = 0;
            label1.Text = "Track Title";
            // 
            // btnShowAllTracks
            // 
            btnShowAllTracks.Location = new Point(253, 278);
            btnShowAllTracks.Name = "btnShowAllTracks";
            btnShowAllTracks.Size = new Size(124, 21);
            btnShowAllTracks.TabIndex = 8;
            btnShowAllTracks.Text = "show all tracks";
            btnShowAllTracks.UseVisualStyleBackColor = true;
            // 
            // txtSearchTracks
            // 
            txtSearchTracks.Location = new Point(390, 277);
            txtSearchTracks.Name = "txtSearchTracks";
            txtSearchTracks.Size = new Size(272, 21);
            txtSearchTracks.TabIndex = 9;
            // 
            // btnSearchTracks
            // 
            btnSearchTracks.Location = new Point(684, 276);
            btnSearchTracks.Name = "btnSearchTracks";
            btnSearchTracks.Size = new Size(75, 23);
            btnSearchTracks.TabIndex = 10;
            btnSearchTracks.Text = "search";
            btnSearchTracks.UseVisualStyleBackColor = true;
            btnSearchTracks.Click += BtnSearchTracks_Click;
            // 
            // btnDeleteSelectedAlbum
            // 
            btnDeleteSelectedAlbum.Location = new Point(779, 39);
            btnDeleteSelectedAlbum.Name = "btnDeleteSelectedAlbum";
            btnDeleteSelectedAlbum.Size = new Size(75, 23);
            btnDeleteSelectedAlbum.TabIndex = 11;
            btnDeleteSelectedAlbum.Text = "delete";
            btnDeleteSelectedAlbum.UseVisualStyleBackColor = true;
            btnDeleteSelectedAlbum.Click += BtnDeleteAnAlbum;
            // 
            // btnDeleteSelectedTrack
            // 
            btnDeleteSelectedTrack.Location = new Point(779, 275);
            btnDeleteSelectedTrack.Name = "btnDeleteSelectedTrack";
            btnDeleteSelectedTrack.Size = new Size(75, 23);
            btnDeleteSelectedTrack.TabIndex = 12;
            btnDeleteSelectedTrack.Text = "delete";
            btnDeleteSelectedTrack.UseVisualStyleBackColor = true;
            btnDeleteSelectedTrack.Click += BtnDeleteSelectedTrack;
            // 
            // webView2
            // 
            webView2.AllowExternalDrop = true;
            webView2.CreationProperties = null;
            webView2.DefaultBackgroundColor = Color.White;
            webView2.Location = new Point(871, 305);
            webView2.Name = "webView2";
            webView2.Size = new Size(346, 293);
            webView2.TabIndex = 13;
            webView2.ZoomFactor = 1D;
            // 
            // FrmMain
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1229, 610);
            Controls.Add(webView2);
            Controls.Add(btnDeleteSelectedTrack);
            Controls.Add(btnDeleteSelectedAlbum);
            Controls.Add(btnSearchTracks);
            Controls.Add(txtSearchTracks);
            Controls.Add(btnShowAllTracks);
            Controls.Add(gbTracks);
            Controls.Add(dataGridView_tracks);
            Controls.Add(groupBox1);
            Controls.Add(pbAlbumArt);
            Controls.Add(txtSearchAlbum);
            Controls.Add(BtnSearch);
            Controls.Add(dataGridView_albums);
            Controls.Add(btnShowallAlbums);
            Font = new Font("Times New Roman", 9F, FontStyle.Regular, GraphicsUnit.Point);
            Name = "FrmMain";
            Text = "Music App";
            ((System.ComponentModel.ISupportInitialize)dataGridView_albums).EndInit();
            ((System.ComponentModel.ISupportInitialize)pbAlbumArt).EndInit();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridView_tracks).EndInit();
            gbTracks.ResumeLayout(false);
            gbTracks.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)webView2).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btnShowallAlbums;
        private DataGridView dataGridView_albums;
        private Button BtnSearch;
        private TextBox txtSearchAlbum;
        private PictureBox pbAlbumArt;
        private GroupBox groupBox1;
        private Label lblImage_Url;
        private Label lblDescription;
        private Label lblYearMade;
        private Label lblArtistName;
        private Label lblTitle;
        private TextBox txtTitle;
        private TextBox txtArtistName;
        private TextBox txtYearMade;
        private TextBox txtImage_Url;
        private Button btnAddAlbum;
        private TextBox txtDescription;
        private DataGridView dataGridView_tracks;
        private GroupBox gbTracks;
        private TextBox txt_TrackVideoURL;
        private TextBox txt_TrackTitle;
        private Label lblVideoURL;
        private Label label1;
        private Button btnShowAllTracks;
        private TextBox txtSearchTracks;
        private Button btnSearchTracks;
        private Button btnDeleteSelectedAlbum;
        private Button btnDeleteSelectedTrack;
        private Button btnAddTrack;
        private Microsoft.Web.WebView2.WinForms.WebView2 webView2;
    }
}