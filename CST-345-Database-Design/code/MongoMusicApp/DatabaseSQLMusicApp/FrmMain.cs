using System.Security.Policy;

namespace MongoDBMusicApp
{
    public partial class FrmMain : Form
    {
        BindingSource albumBindingSource = new BindingSource();

        public FrmMain()
        {
            InitializeComponent();
        }
        // one service to get mongoDB data
        AlbumDAO albumDAO = new AlbumDAO();

        BindingSource albumSource = new BindingSource();
        BindingSource trackSource = new BindingSource();

        private void UpdateAlbumGrid()
        {
            //This method connects the datagrid control to the data source 

            //fetch all records from the database 
            albumSource.DataSource = albumDAO.getAll();

            //Associate the binding source to the data grid control
            dataGridView_albums.DataSource = albumSource;
        }

        private void BtnShowAllAlbums(object sender, EventArgs e)
        {
            UpdateAlbumGrid();
        }


        private void updateTrackGrid()
        {
            dataGridView_tracks.DataSource = trackSource;
        }

        private void BtnAddAlbum_Click(object sender, EventArgs e)
        {
            try
            {
                Album a = new Album
                {
                    Title = txtTitle.Text,
                    Artist = txtArtistName.Text,
                    Year = Int32.Parse(txtYearMade.Text),
                    ImageURL = txtImage_Url.Text,
                    Description = txtDescription.Text,
                    Tracks = new List<Track>()
                };
                albumDAO.addOne(a);

                //refresh the grid display
                UpdateAlbumGrid();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void dataGridView_albums_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            // Check if the click is on the header or a valid row
            if (e.RowIndex >= 0 && e.ColumnIndex >= 0)
            {
                DataGridView dataGridView = (DataGridView)sender;

                // Assume that the first column contains the album's Id
                string albumId = dataGridView.Rows[e.RowIndex].Cells[0].Value.ToString();

                // Now, use this albumId to update the tracks grid
                UpdateTrackGridForAlbum(albumId);

                // Load picture
                try
                {
                    string imageUrl = dataGridView.Rows[e.RowIndex].Cells["ImageURL"].Value.ToString(); // Use the column name if possible for clarity
                    pbAlbumArt.Load(imageUrl);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error loading image: " + ex.Message);
                }
            }
        }


        private void UpdateTrackGridForAlbum(string itemNumber)
        {
            Album album = albumDAO.getOne(itemNumber);

            //Get all the tracks stored in the album
            trackSource.DataSource = album.Tracks;

            //associate the binding source to the data grid control
            dataGridView_tracks.DataSource = trackSource;
        }

        private void BtnSearchAlbum_Click(object sender, EventArgs e)
        {
            //get the search phrase from the input 
            String searchTerm = txtSearchAlbum.Text;


            List<Album> searchResults = albumDAO.search(searchTerm);

            //get matching items that contain the search term
            dataGridView_albums.DataSource = albumSource;
            albumSource.DataSource = searchResults;

        }

        private void BtnSearchTracks_Click(object sender, EventArgs e)
        {
            //get the search phrase from the input 
            String searchTerm = txtSearchTracks.Text;

            //get selected album
            //rowNumber refers to the position in the table 
            int rownumber = dataGridView_albums.CurrentCell.RowIndex;

            //itemnumber is the id value of the album object 
            String itemNumber = (String)dataGridView_albums.Rows[rownumber].Cells[0].Value;

            Album selectedAlbum = albumDAO.getOne(itemNumber);

            List<Track> searchTrackResults = selectedAlbum.Tracks.FindAll(x => x.TrackTitle.Contains(searchTerm));

            //reset the table of data
            trackSource.DataSource = searchTrackResults;

            trackSource.ResetBindings(false);
        }

        private void BtnDeleteAnAlbum(object sender, EventArgs e)
        {
            //rownumber refers to the position in the table 
            int rownumber = dataGridView_albums.CurrentCell.RowIndex;

            //itemnumber is the id value of the album object
            string itemnumber = (string)dataGridView_albums.Rows[rownumber].Cells[0].Value;
            //confirm delete
            DialogResult result = MessageBox.Show("Do you want to delete album number " + itemnumber + "?", "warning", MessageBoxButtons.YesNo);

            if (result == DialogResult.Yes)
            {
                int deleteResult = albumDAO.deleteOne(itemnumber);
                UpdateAlbumGrid();
                if (deleteResult < 0)
                {
                    MessageBox.Show("Error deleting");

                }
            }
        }

        private void AddTrack_Click(object sender, EventArgs e)
        {
            //rownumber refers to the position in the table
            int rownumber = dataGridView_albums.CurrentCell.RowIndex;

            //itemnumber is the id value of the album object 
            string itemNumber = (string)dataGridView_albums.Rows[rownumber].Cells[0].Value;
            Album selectedAlbum = albumDAO.getOne(itemNumber);

            //create new track based on the text fields in the data entry form. 
            Track newTrack = new Track
            {
                TrackTitle = txt_TrackTitle.Text,
                VideoURL = txt_TrackVideoURL.Text
            };
            albumDAO.addTrackToAlbum(selectedAlbum, newTrack);
        }

        private void BtnDeleteSelectedTrack(object sender, EventArgs e)
        {
            //rownumber refers to the position in the table 
            int albumRowNumber = dataGridView_albums.CurrentCell.RowIndex;

            //itemnumber is the id value of the album object 
            string albumIdNumber = (string)dataGridView_albums.Rows[albumRowNumber].Cells[0].Value;

            Album selectedAlbum = albumDAO.getOne(albumIdNumber);

            int trackRowNumber = dataGridView_tracks.CurrentRow.Index;
            string trackIdNumber = (string)dataGridView_tracks.Rows[trackRowNumber].Cells[0].Value;

            //configure delete
            DialogResult result = MessageBox.Show("Do you want to delete this track? " + trackIdNumber + "?", "Warning", MessageBoxButtons.YesNo);

            if (result == DialogResult.Yes)
            {
                bool deleteResult = albumDAO.deleteOneTrack(selectedAlbum, trackIdNumber);

                if (deleteResult == false)
                {
                    MessageBox.Show("Error deleting");

                }
                UpdateTrackGridForAlbum(albumIdNumber);
            }

        }

        private void dgvTracks_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            //delete a record when its row is clicked 
            DataGridView dataGridView = (DataGridView)sender;

            //rowNumber refers to the position in the table 
            int rownumber = dataGridView.CurrentCell.RowIndex;

            String videoURL = dataGridView.Rows[rownumber].Cells[2].Value.ToString();

            //LOAD VIDEO
            try
            {
                webView2.Source = new Uri(videoURL);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}

