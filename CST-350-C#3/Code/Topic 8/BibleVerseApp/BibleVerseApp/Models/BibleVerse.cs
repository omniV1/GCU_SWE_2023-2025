namespace BibleVerseApp.Models
{
    public class BibleVerse
    {
        public string Id { get; set; }        

        public int Book { get; set; }         

        public int Chapter { get; set; }      

        public int Verse { get; set; }        

        public string Text { get; set; }      
    }
}
