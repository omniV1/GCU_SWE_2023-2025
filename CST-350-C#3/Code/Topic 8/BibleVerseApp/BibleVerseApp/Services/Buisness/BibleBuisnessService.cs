using BibleVerseApp.Models;
using BibleVerseApp.Services.Buisness.Interfaces;
using BibleVerseApp.Services.Data.Interfaces;

namespace BibleVerseApp.Services.Business
{
    /// <summary>
    /// Implementation of the Bible business service
    /// Manages business logic and communication between controllers and data access layer
    /// </summary>
    public class BibleBusinessService : IBibleBusinessService
    {
        /// <summary>
        /// Reference to the data access object
        /// </summary>
        private readonly IBibleDAO _bibleDAO;

        /// <summary>
        /// Constructor that initializes the data access dependency
        /// </summary>
        /// <param name="bibleDAO">The Bible data access object</param>
        public BibleBusinessService(IBibleDAO bibleDAO)
        {
            _bibleDAO = bibleDAO;
        }

        /// <summary>
        /// Gets a verse by its ID and version from the data access layer
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="verseId">The unique identifier of the verse</param>
        /// <returns>BibleVerse object if found, null if not found</returns>
        public BibleVerse GetVerseById(string version, string verseId)
        {
            try
            {
                return _bibleDAO.GetVerseById(version, verseId);
            }
            catch (Exception ex)
            {
                // Log the error if needed
                Console.WriteLine($"Error in GetVerseById: {ex.Message}");
                return null;
            }
        }

        /// <summary>
        /// Gets all verses for a specific chapter from the data access layer
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="book">Book number</param>
        /// <param name="chapter">Chapter number</param>
        /// <returns>List of BibleVerse objects</returns>
        public List<BibleVerse> GetVersesByChapter(string version, int book, int chapter)
        {
            try
            {
                return _bibleDAO.GetVersesByChapter(version, book, chapter);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in GetVersesByChapter: {ex.Message}");
                return new List<BibleVerse>();
            }
        }

        /// <summary>
        /// Gets all available Bible versions from the data access layer
        /// </summary>
        /// <returns>List of BibleVersion objects</returns>
        public List<BibleVersion> GetAllVersions()
        {
            try
            {
                return _bibleDAO.GetAllVersions();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in GetAllVersions: {ex.Message}");
                return new List<BibleVersion>();
            }
        }

        /// <summary>
        /// Gets all Bible books from the data access layer
        /// </summary>
        /// <returns>List of BibleBook objects</returns>
        public List<BibleBook> GetAllBooks()
        {
            try
            {
                return _bibleDAO.GetAllBooks();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in GetAllBooks: {ex.Message}");
                return new List<BibleBook>();
            }
        }

        /// <summary>
        /// Gets all Bible genres from the data access layer
        /// </summary>
        /// <returns>List of BibleGenre objects</returns>
        public List<BibleGenre> GetAllGenres()
        {
            try
            {
                return _bibleDAO.GetAllGenres();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in GetAllGenres: {ex.Message}");
                return new List<BibleGenre>();
            }
        }

        /// <summary>
        /// Gets cross references for a specific verse from the data access layer
        /// </summary>
        /// <param name="verseId">The verse ID to find cross references for</param>
        /// <returns>List of CrossReference objects</returns>
        public List<CrossReference> GetCrossReferences(string verseId)
        {
            try
            {
                return _bibleDAO.GetCrossReferences(verseId);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in GetCrossReferences: {ex.Message}");
                return new List<CrossReference>();
            }
        }

        public int GetChapterCount(string version, int bookId)
        {
            try
            {
                return _bibleDAO.GetChapterCount(version, bookId);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in GetChapterCount: {ex.Message}");
                return 0;
            }
        }
    }
}