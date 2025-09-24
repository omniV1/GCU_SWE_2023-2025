namespace BibleVerseApp.Models
{
    public class BookAbbreviation
    {
        public int Id { get; set; }

        public string Abbreviation { get; set; }

        public int BookId { get; set; }

        public bool IsPrimary { get; set; }
    }
}
