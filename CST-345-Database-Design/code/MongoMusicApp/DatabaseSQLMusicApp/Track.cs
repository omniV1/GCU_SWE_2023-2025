using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MongoDBMusicApp
{
     public class Track
    {
        [BsonId]
        [BsonRepresentation(MongoDB.Bson.BsonType.ObjectId)]
        public string Id { get; set; }

        public string TrackTitle { get; set; }

        public string VideoURL { get; set; }

        public Track()
        {
            Id = ObjectId.GenerateNewId().ToString();
        }
    }
}
