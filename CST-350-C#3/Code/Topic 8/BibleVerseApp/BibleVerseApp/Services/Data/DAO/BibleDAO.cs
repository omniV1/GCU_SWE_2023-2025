using System.Data.SqlClient;
using BibleVerseApp.Models;
using BibleVerseApp.Services.Data.Interfaces;

namespace BibleVerseApp.Services.Data.DAO
{
    /// <summary>
    /// Data Access Object for Bible database operations
    /// </summary>
    public class BibleDAO : IBibleDAO
    {
        /// <summary>
        /// Define connection string for MSSQL
        /// </summary>
        static string conn = @"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=Bible;Integrated Security=True;Connect Timeout=30;Encrypt=False;Trust Server Certificate=False;Application Intent=ReadWrite;Multi Subnet Failover=False";

        /// <summary>
        /// This method retrieves a specific Bible verse by its ID and version
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="verseId">The unique identifier of the verse</param>
        /// <returns>BibleVerse object if found, null if not found</returns>
        public BibleVerse GetVerseById(string version, string verseId)
        {
            string query = "";

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                query = $"SELECT * FROM dbo.t_{version.ToLower()} WHERE id = @id";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@id", verseId);

                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        if (reader.Read())
                        {
                            BibleVerse verse = new BibleVerse
                            {
                                Id = reader.GetString(reader.GetOrdinal("id")),
                                Book = reader.GetInt32(reader.GetOrdinal("b")),
                                Chapter = reader.GetInt32(reader.GetOrdinal("c")),
                                Verse = reader.GetInt32(reader.GetOrdinal("v")),
                                Text = reader.GetString(reader.GetOrdinal("t"))
                            };
                            return verse;
                        }
                        return null;
                    }
                }
            }
        }

        /// <summary>
        /// This method retrieves all verses from a specific chapter in a given Bible version
        /// </summary>
        /// <param name="version">Bible version (asv, kjv, web, ylt)</param>
        /// <param name="book">Book number</param>
        /// <param name="chapter">Chapter number</param>
        /// <returns>List of BibleVerse objects</returns>
        public List<BibleVerse> GetVersesByChapter(string version, int book, int chapter)
        {
            string query = "";
            List<BibleVerse> verses = new List<BibleVerse>();

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                query = $"SELECT * FROM dbo.t_{version.ToLower()} WHERE b = @book AND c = @chapter ORDER BY v";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@book", book);
                    command.Parameters.AddWithValue("@chapter", chapter);

                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            verses.Add(new BibleVerse
                            {
                                Id = reader.GetString(reader.GetOrdinal("id")),
                                Book = reader.GetInt32(reader.GetOrdinal("b")),
                                Chapter = reader.GetInt32(reader.GetOrdinal("c")),
                                Verse = reader.GetInt32(reader.GetOrdinal("v")),
                                Text = reader.GetString(reader.GetOrdinal("t"))
                            });
                        }
                    }
                }
            }
            return verses;
        }

        /// <summary>
        /// This method retrieves all available Bible versions from the database
        /// </summary>
        /// <returns>List of BibleVersion objects</returns>
        public List<BibleVersion> GetAllVersions()
        {
            string query = "";
            List<BibleVersion> versions = new List<BibleVersion>();

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                query = "SELECT * FROM dbo.bible_version_key";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            versions.Add(new BibleVersion
                            {
                                Id = reader.GetInt32(reader.GetOrdinal("id")),
                                Table = reader.GetString(reader.GetOrdinal("table")),
                                Abbreviation = reader.GetString(reader.GetOrdinal("abbreviation")),
                                Language = reader.GetString(reader.GetOrdinal("language")),
                                Version = reader.GetString(reader.GetOrdinal("version")),
                                InfoText = reader.GetString(reader.GetOrdinal("info_text")),
                                InfoUrl = reader.GetString(reader.GetOrdinal("info_url")),
                                Publisher = reader.GetString(reader.GetOrdinal("publisher")),
                                Copyright = reader.GetString(reader.GetOrdinal("copyright")),
                                CopyrightInfo = reader.GetString(reader.GetOrdinal("copyright_info"))
                            });
                        }
                    }
                }
            }
            return versions;
        }

        /// <summary>
        /// This method retrieves all Bible books from the database
        /// </summary>
        /// <returns>List of BibleBook objects</returns>
        public List<BibleBook> GetAllBooks()
        {
            string query = "";
            List<BibleBook> books = new List<BibleBook>();

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                query = "SELECT * FROM dbo.key_english ORDER BY b";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            books.Add(new BibleBook
                            {
                                Id = reader.GetInt32(reader.GetOrdinal("b")),
                                Name = reader.GetString(reader.GetOrdinal("n")),
                                Testament = reader.GetString(reader.GetOrdinal("t")),
                                GenreId = reader.GetInt32(reader.GetOrdinal("g"))
                            });
                        }
                    }
                }
            }
            return books;
        }

        /// <summary>
        /// This method retrieves all Bible genres from the database
        /// </summary>
        /// <returns>List of BibleGenre objects</returns>
        public List<BibleGenre> GetAllGenres()
        {
            string query = "";
            List<BibleGenre> genres = new List<BibleGenre>();

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                query = "SELECT * FROM dbo.key_genre_english";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            genres.Add(new BibleGenre
                            {
                                Id = reader.GetInt32(reader.GetOrdinal("g")),
                                Name = reader.GetString(reader.GetOrdinal("n"))
                            });
                        }
                    }
                }
            }
            return genres;
        }

        /// <summary>
        /// This method retrieves all cross references for a specific verse
        /// </summary>
        /// <param name="verseId">The verse ID to find cross references for</param>
        /// <returns>List of CrossReference objects</returns>
        public List<CrossReference> GetCrossReferences(string verseId)
        {
            string query = "";
            List<CrossReference> references = new List<CrossReference>();

            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();

                query = "SELECT * FROM dbo.cross_reference WHERE vid = @verseId";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@verseId", verseId);

                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            references.Add(new CrossReference
                            {
                                VerseId = reader.GetString(reader.GetOrdinal("vid")),
                                Relation = reader.GetInt32(reader.GetOrdinal("r")),
                                SourceVerse = reader.GetString(reader.GetOrdinal("sv")),
                                Edition = reader.GetInt32(reader.GetOrdinal("ev"))
                            });
                        }
                    }
                }
            }
            return references;
        }

        public int GetChapterCount(string version, int bookId)
        {
            using (SqlConnection connection = new SqlConnection(conn))
            {
                connection.Open();
                string query = $"SELECT MAX(c) FROM dbo.t_{version.ToLower()} WHERE b = @bookId";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@bookId", bookId);
                    var result = command.ExecuteScalar();
                    return result == DBNull.Value ? 0 : Convert.ToInt32(result);
                }
            }
        }
    }
}