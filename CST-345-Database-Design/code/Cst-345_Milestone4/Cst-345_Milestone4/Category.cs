using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static Cst_345_Milestone4.product;

namespace Cst_345_Milestone4
{
    

        internal class Category
    {
        public int CategoryId { get; set; }
        public string CategoryName { get; set; }
        public string CategoryDesc { get; set; }
    

    public class CategoryDAO
    {
        private string connectionString = "server=localhost;port=3306;user=root;password=root;database=milestone1";

        /// <summary>
        /// Retrieves all categories from the database.
        /// </summary>
        /// <returns>A list of all categories.</returns>
        public List<Category> GetAllCategories()
        {
            var categories = new List<Category>();
            using (var connection = new MySqlConnection(connectionString))
            {
                var query = "SELECT categoryId, CategoryName, CategoryDesc FROM product_categories";
                using (var command = new MySqlCommand(query, connection))
                {
                    try
                    {
                        connection.Open();
                        using (var reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                var category = new Category
                                {
                                    CategoryId = reader.GetInt32("categoryId"),
                                    CategoryName = reader.GetString("CategoryName"),
                                    CategoryDesc = reader.GetString("CategoryDesc")
                                };
                                categories.Add(category);
                            }
                        }
                    }
                    catch (MySqlException ex)
                    {
                        
                    }
                    catch (Exception ex)
                    {
                        
                    }
                }
            }
            return categories;
        }

            /// <summary>
            /// Adds a new category to the database.
            /// </summary>
            /// <param name="category">The category to add.</param>
            /// <returns>True if the category was added successfully; otherwise, false.</returns>
            public bool AddCategory(Category category)
            {
                using (var connection = new MySqlConnection(connectionString))
                {
                    var query = "INSERT INTO product_categories (CategoryName, CategoryDesc) VALUES (@CategoryName, @CategoryDesc)";
                    using (var command = new MySqlCommand(query, connection))
                    {
                        command.Parameters.AddWithValue("@CategoryName", category.CategoryName);
                        command.Parameters.AddWithValue("@CategoryDesc", category.CategoryDesc);
                        try
                        {
                            connection.Open();
                            int result = command.ExecuteNonQuery();
                            return result > 0;
                        }
                        catch (MySqlException ex)
                        {
                            // MySQL-specific exception details
                            MessageBox.Show($"MySQL error: {ex.Message}", "Database Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            return false;
                        }
                        catch (Exception ex)
                        {
                            // General exception details
                            MessageBox.Show($"An error occurred: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            return false;
                        }
                    }
                }
            }


            /// <summary>
            /// Deletes a category from the database by its ID.
            /// </summary>
            /// <param name="categoryId">The ID of the category to delete.</param>
            /// <returns>True if the category was deleted successfully; otherwise, false.</returns>
            public bool DeleteCategory(int categoryId)
        {
            using (var connection = new MySqlConnection(connectionString))
            {
                var query = "DELETE FROM product_categories WHERE categoryId = @categoryId";
                using (var command = new MySqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@categoryId", categoryId);
                    try
                    {
                        connection.Open();
                        return command.ExecuteNonQuery() > 0;
                    }
                    catch (MySqlException ex)
                    {
                        // Log MySQL-specific exception details here using your preferred logging framework
                        return false;
                    }
                    catch (Exception ex)
                    {
                        // Log general exception details here using your preferred logging framework
                        return false;
                    }
                }
            }
        }

        /// <summary>
        /// Searches for categories by a search term in the category name or description.
        /// </summary>
        /// <param name="searchTerm">The search term to use.</param>
        /// <returns>A list of categories that match the search term.</returns>
        public List<Category> SearchCategories(string searchTerm)
        {
            var categories = new List<Category>();
            using (var connection = new MySqlConnection(connectionString))
            {
                var query = @"
                SELECT categoryId, CategoryName, CategoryDesc
                FROM product_categories
                WHERE CategoryName LIKE @SearchTerm OR CategoryDesc LIKE @SearchTerm";
                using (var command = new MySqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@SearchTerm", $"%{searchTerm}%");
                    try
                    {
                        connection.Open();
                        using (var reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                var category = new Category
                                {
                                    CategoryId = reader.GetInt32("categoryId"),
                                    CategoryName = reader.GetString("CategoryName"),
                                    CategoryDesc = reader.GetString("CategoryDesc")
                                };
                                categories.Add(category);
                            }
                        }
                    }
                    catch (MySqlException ex)
                    {
                        // Log MySQL-specific exception details here using your preferred logging framework
                        return categories; // Still return the list, which will be empty if an exception occurred
                    }
                    catch (Exception ex)
                    {
                        // Log general exception details here using your preferred logging framework
                        return categories; // Still return the list, which will be empty if an exception occurred
                    }
                }
            }
            return categories;
        }
    }

}
}

