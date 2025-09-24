using MongoDB.Driver;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MongoDBMusicApp
{
    internal class AlbumDAO
    {
        private const string CONNECTION = "mongodb+srv://OwenLindsey:Owen@myAtlasClusterEDU.bjgbnzk.mongodb.net/";
        private const string DATABASE_NAME = "musicDatabase";
        private const string ALBUM_COLLECTION = "albums";
        private MongoClient client;
        private IMongoDatabase database;
        private IMongoCollection<Album> albumCollection;

        public AlbumDAO()
        {
            client = new MongoClient(CONNECTION);
            database = client.GetDatabase(DATABASE_NAME);
            albumCollection = database.GetCollection<Album>(ALBUM_COLLECTION);
        }



        public List<Album> getAll()
        {
            var results = albumCollection.Find(x => true).ToList();
            return results;
        }

        public Album getOne(string id)
        {
            Album result = albumCollection.Find(x => x.Id == id).First();
            return result;
        }

        public void addOne(Album album)
        {
            albumCollection.InsertOne(album);
        }

        internal List<Album> search(string searchTerm)
        {
            var results = albumCollection.Find(x => x.Title.ToLower().Contains(searchTerm.ToLower())).ToList();
            return results;
        }

        internal int deleteOne(string itemId)
        {
            long results = albumCollection.DeleteOne(x => x.Id == itemId).DeletedCount;
            return (int)results;
        }


        internal Album addTrackToAlbum(Album albumWhoGetsNewTrack, Track newTrack)
        {
            // Check if the Tracks list is null and initialize if necessary
            if (albumWhoGetsNewTrack.Tracks == null)
            {
                albumWhoGetsNewTrack.Tracks = new List<Track>();
            }

            // Add the new track to the album
            albumWhoGetsNewTrack.Tracks.Add(newTrack);

            // Update the album document in the collection
            albumCollection.FindOneAndReplace(a => a.Id == albumWhoGetsNewTrack.Id, albumWhoGetsNewTrack);

            // Return the updated album
            return albumWhoGetsNewTrack;
        }

        internal bool deleteOneTrack(Album selectedAlbum, string trackId)
        {
            // Find the track and remove it
            Track foundTrack = selectedAlbum.Tracks.Find(t => t.Id == trackId);
            if (foundTrack != null)
            {
                bool result = selectedAlbum.Tracks.Remove(foundTrack);
                if (result)
                {
                    // Update the album document in the collection
                    albumCollection.FindOneAndReplace(a => a.Id == selectedAlbum.Id, selectedAlbum);
                }
                return result;
            }
            return false;
        }
    }
}


