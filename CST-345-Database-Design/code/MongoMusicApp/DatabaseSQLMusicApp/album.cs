using MongoDB.Bson.Serialization.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

      namespace MongoDBMusicApp
    {
        public class Album
        {
        [BsonId]
        [BsonRepresentation(MongoDB.Bson.BsonType.ObjectId)]
           
            public string Id { get; set; }
            public string Title {  get; set; }
            public string Artist { get; set; }
            public int Year { get; set; }
            public string ImageURL { get; set; }  
            public string Description { get; set; }

        public List<Track> Tracks { get; set; }

        public override string ToString()
        {
            return "Id: " + Id + "Title: " + Title + "Artist: " + Artist + "Year :" + Year; 
        }

        }

    }



