using Microsoft.AspNetCore.Mvc;
using BibleVerseApp.Models;
using BibleVerseApp.Services.Buisness.Interfaces;

namespace BibleVerseApp.Controllers
{
    /// <summary>
    /// Controller for handling Bible-related HTTP requests
    /// Manages the interaction between views and business services
    /// </summary>
    public class BibleController : Controller
    {
        /// <summary>
        /// Reference to the business service
        /// </summary>
        private readonly IBibleBusinessService _bibleBusinessService;

        /// <summary>
        /// Constructor that initializes the business service dependency
        /// </summary>
        /// <param name="bibleBusinessService">The Bible business service</param>
        public BibleController(IBibleBusinessService bibleBusinessService)
        {
            _bibleBusinessService = bibleBusinessService;
        }

        /// <summary>
        /// Displays the main page with a list of all Bible versions
        /// GET: /Bible/Index
        /// </summary>
        /// <returns>View with list of Bible versions</returns>
        public IActionResult Index()
        {
            var versions = _bibleBusinessService.GetAllVersions();
            return View(versions);
        }

        /// <summary>
        /// Displays a list of all Bible books
        /// GET: /Bible/Books
        /// </summary>
        /// <returns>View with list of Bible books</returns>
        public IActionResult Books()
        {
            var books = _bibleBusinessService.GetAllBooks();
            return View(books);
        }

        /// <summary>
        /// Displays a specific chapter with all its verses
        /// GET: /Bible/Chapter/{version}/{book}/{chapter}
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="book">Book number</param>
        /// <param name="chapter">Chapter number</param>
        /// <returns>View with list of verses in the chapter</returns>
        public IActionResult Chapter(string version, int book, int chapter)
        {
            var verses = _bibleBusinessService.GetVersesByChapter(version, book, chapter);
            if (!verses.Any())
            {
                return NotFound();
            }
            return View(verses);
        }

        /// <summary>
        /// Displays a specific verse with its cross references
        /// GET: /Bible/Verse/{version}/{verseId}
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="verseId">The unique identifier of the verse</param>
        /// <returns>View with verse details and cross references</returns>
        public IActionResult Verse(string version, string verseId)
        {
            var verse = _bibleBusinessService.GetVerseById(version, verseId);
            if (verse == null)
            {
                return NotFound();
            }

            // Get cross references for the verse
            var crossReferences = _bibleBusinessService.GetCrossReferences(verseId);

            // Create a view model to hold both the verse and its cross references
            var viewModel = new Dictionary<string, object>
            {
                { "Verse", verse },
                { "CrossReferences", crossReferences }
            };

            return View(viewModel);
        }

        /// <summary>
        /// Displays all Bible genres
        /// GET: /Bible/Genres
        /// </summary>
        /// <returns>View with list of Bible genres</returns>
        public IActionResult Genres()
        {
            var genres = _bibleBusinessService.GetAllGenres();
            return View(genres);
        }

        /// <summary>
        /// Returns verse data in JSON format for AJAX requests
        /// GET: /Bible/GetVerseJson/{version}/{verseId}
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="verseId">The unique identifier of the verse</param>
        /// <returns>JSON result containing verse data</returns>
        [HttpGet]
        public IActionResult GetVerseJson(string version, string verseId)
        {
            var verse = _bibleBusinessService.GetVerseById(version, verseId);
            if (verse == null)
            {
                return NotFound();
            }
            return Json(verse);
        }

        /// <summary>
        /// Returns chapter count in JSON format for AJAX requests
        /// GET: /Bible/GetChapterCountJson/{version}/{bookId}
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="bookId">Book number</param>
        /// <returns>JSON result containing chapter count</returns>
        [HttpGet]
        public IActionResult GetChapterCountJson(string version, int bookId)
        {
            var chapterCount = _bibleBusinessService.GetChapterCount(version, bookId);
            return Json(new { count = chapterCount });
        }
    }
}