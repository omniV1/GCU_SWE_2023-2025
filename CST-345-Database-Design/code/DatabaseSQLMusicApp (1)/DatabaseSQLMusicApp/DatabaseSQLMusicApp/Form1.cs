namespace DatabaseSQLMusicApp
{
    public partial class DatabaseSQLMusicApp : Form
    {
        BindingSource albumBindingSource = new BindingSource();

        public DatabaseSQLMusicApp()
        {
            InitializeComponent();
        }

        private void LoadAlbumOnClick(object sender, EventArgs e)
        {
            AlbumDAO albumDAO = new AlbumDAO();

            // connect grid control to the list of albums
            albumBindingSource.DataSource = albumDAO.GetAllAlbums();
            dataGridView1.DataSource = albumBindingSource; // Make sure you have the correct DataGridView name

            pictureBox1.Load("https://f4.bcbits.com/img/a3153812078_16.jpg");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            AlbumDAO albumDAO = new AlbumDAO();

            // Depending on whether the textBox1 contains any text, fetch all albums or search specific ones
            if (string.IsNullOrEmpty(textBox1.Text))
            {
                albumBindingSource.DataSource = albumDAO.GetAllAlbums();
            }
            else
            {
                albumBindingSource.DataSource = albumDAO.SearchTitles(textBox1.Text);
            }

            dataGridView1.DataSource = albumBindingSource;
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            MessageBox.Show("youve clicked me");

            DataGridView dataGridView = (DataGridView)sender;

            // get the row number clicked 


            int rowClicked = dataGridView.CurrentRow.Index;
            MessageBox.Show("Youve clicked row" + rowClicked);

            String imageURL = dataGridView.Rows[rowClicked].Cells[4].Value.ToString();
            pictureBox1.Load(imageURL);

        }

        private void btnAddAlbum_Click(object sender, EventArgs e)
        {
            // add a new item to the database
            Album album = new Album
            {
                AlbumName = txtAlbumName.Text,
                ArtistName = txtArtistName.Text,
                Year = Int32.Parse(txtYearMade.Text),
                ImageURL = txtImage_Url.Text,
                Description = txtDescription.Text
            };

            AlbumDAO albumDAO = new AlbumDAO();
            int result = albumDAO.addOneAlbum(album);

            MessageBox.Show(result + " new row(s) inserted");
        }

    }
}




