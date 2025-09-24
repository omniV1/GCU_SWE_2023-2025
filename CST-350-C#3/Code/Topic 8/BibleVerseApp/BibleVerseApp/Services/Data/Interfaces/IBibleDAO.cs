using BibleVerseApp.Models;

namespace BibleVerseApp.Services.Data.Interfaces
{
    public interface IBibleDAO
    {
        /// <summary>
        /// Gets a verse by its ID from specified version
        /// </summary>
        BibleVerse GetVerseById(string version, string verseId);

        /// <summary>
        /// Gets all verses for a specific book chapter from specified version
        /// </summary>
        List<BibleVerse> GetVersesByChapter(string version, int book, int chapter);

        /// <summary>
        /// Gets all available Bible versions
        /// </summary>
        List<BibleVersion> GetAllVersions();

        /// <summary>
        /// Gets all Bible books
        /// </summary>
        List<BibleBook> GetAllBooks();

        /// <summary>
        /// Gets all genre types
        /// </summary>
        List<BibleGenre> GetAllGenres();

        /// <summary>
        /// Gets cross references for a specific verse
        /// </summary>
        List<CrossReference> GetCrossReferences(string verseId);

        /// <summary>
        /// Gets the number of chapters in a specific book for a given version
        /// </summary>
        int GetChapterCount(string version, int bookId);
    }
}