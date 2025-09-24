namespace BibleVerseApp.Models
{
    public class CrossReference
    {
        public string VerseId { get; set; }  

        public int Relation { get; set; }     

        public string SourceVerse { get; set; }

        public int Edition { get; set; }      
    }
}

