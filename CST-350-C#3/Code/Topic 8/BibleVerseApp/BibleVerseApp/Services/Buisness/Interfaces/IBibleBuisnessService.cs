using BibleVerseApp.Models;

namespace BibleVerseApp.Services.Buisness.Interfaces
{
    /// <summary>
    /// Interface for business logic operations related to Bible data
    /// Handles the communication between controllers and data access layer
    /// </summary>
    public interface IBibleBusinessService
    {
        /// <summary>
        /// Gets a specific verse from a specified Bible version
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="verseId">The unique identifier of the verse</param>
        /// <returns>BibleVerse object if found, null if not found</returns>
        BibleVerse GetVerseById(string version, string verseId);

        /// <summary>
        /// Gets all verses from a specific chapter in a given Bible version
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="book">Book number</param>
        /// <param name="chapter">Chapter number</param>
        /// <returns>List of BibleVerse objects</returns>
        List<BibleVerse> GetVersesByChapter(string version, int book, int chapter);

        /// <summary>
        /// Gets all available Bible versions
        /// </summary>
        /// <returns>List of BibleVersion objects</returns>
        List<BibleVersion> GetAllVersions();

        /// <summary>
        /// Gets all Bible books
        /// </summary>
        /// <returns>List of BibleBook objects</returns>
        List<BibleBook> GetAllBooks();

        /// <summary>
        /// Gets all Bible genres
        /// </summary>
        /// <returns>List of BibleGenre objects</returns>
        List<BibleGenre> GetAllGenres();

        /// <summary>
        /// Gets all cross references for a specific verse
        /// </summary>
        /// <param name="verseId">The verse ID to find cross references for</param>
        /// <returns>List of CrossReference objects</returns>
        List<CrossReference> GetCrossReferences(string verseId);

        /// <summary>
        /// Gets the number of chapters in a specific book for a given version
        /// </summary>
        int GetChapterCount(string version, int bookId);
    }
}