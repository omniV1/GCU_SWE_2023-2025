using System;
using System.Collections.Generic;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace Cst_345_Milestone4
{
    internal class product
    {
        public class Product
        {
            public int ProductId { get; set; }
            public int CategoryId { get; set; }
            public string ProductName { get; set; }
            public string Description { get; set; }
            public decimal RetailPrice { get; set; }
            public decimal WholesalePrice { get; set;}

        }
        public class ProductDAO
        {
            private string connectionString = "server=localhost;port=3306;user=root;password=root;database=milestone1";

            /// <summary>
            /// Retrieves all products from the database.
            /// </summary>
            /// <returns>A list of all products.</returns>
            public List<Product> GetAllProducts()
            {
                var products = new List<Product>();
                using (var connection = new MySqlConnection(connectionString))
                {
                    var query = "SELECT ProductId, CategoryId, ProductName, Description, RetailPrice, WholesalePrice FROM products";
                    using (var command = new MySqlCommand(query, connection))
                    {
                        try
                        {
                            connection.Open();
                            using (var reader = command.ExecuteReader())
                            {
                                while (reader.Read())
                                {
                                    var product = new Product
                                    {
                                        ProductId = reader.GetInt32("ProductId"),
                                        CategoryId = reader.GetInt32("CategoryId"),
                                        ProductName = reader.GetString("ProductName"),
                                        Description = reader.GetString("Description"),
                                        RetailPrice = reader.GetDecimal("RetailPrice"),
                                        WholesalePrice = reader.GetDecimal("WholesalePrice")
                                    };
                                    products.Add(product);
                                }
                            }
                        }
                        catch (MySqlException ex)
                        {
                            // Log MySQL-specific exception details here using your preferred logging framework
                        }
                        catch (Exception ex)
                        {
                            // Log general exception details here using your preferred logging framework
                        }
                    }
                }
                return products;
            }

            /// <summary>
            /// Retrieves a list of products by category.
            /// </summary>
            /// <param name="categoryId">The ID of the category for which to retrieve products.</param>
            /// <returns>A list of products that belong to the specified category.</returns>
            public List<Product> GetProductsByCategory(int categoryId)
            {
                var products = new List<Product>();

                // Use the connection string that you have set up for your database.
                using (var connection = new MySqlConnection(connectionString))
                {
                    // Use parameterized queries to prevent SQL injection.
                    var query = "SELECT ProductId, CategoryId, ProductName, Description, RetailPrice, WholesalePrice FROM products WHERE CategoryId = @CategoryId";
                    using (var command = new MySqlCommand(query, connection))
                    {
                        command.Parameters.AddWithValue("@CategoryId", categoryId);
                        connection.Open();
                        using (var reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                var product = new Product
                                {
                                    ProductId = reader.GetInt32("ProductId"),
                                    CategoryId = reader.GetInt32("CategoryId"),
                                    ProductName = reader.GetString("ProductName"),
                                    Description = reader.GetString("Description"),
                                    RetailPrice = reader.GetDecimal("RetailPrice"),
                                    WholesalePrice = reader.GetDecimal("WholesalePrice")
                                };
                                products.Add(product);
                            }
                        }
                    }
                }

                // If you are here in the debugger and 'products' is empty,
                // it means no products were found for the given 'categoryId'.
                return products;
            }


            /// <summary>
            /// Adds a new product to the database.
            /// </summary>
            /// <param name="product">The product to add.</param>
            /// <returns>True if the product was added successfully; otherwise, false.</returns>
            public bool AddProduct(Product product)
            {
                using (var connection = new MySqlConnection(connectionString))
                {
                    var query = @"
                        INSERT INTO products (CategoryId, ProductName, Description, WholesalePrice, RetailPrice)
                        VALUES (@CategoryId, @ProductName, @Description, @WholesalePrice, @RetailPrice)";

                    using (var command = new MySqlCommand(query, connection))
                    {
                        command.Parameters.AddWithValue("@CategoryId", product.CategoryId);
                        command.Parameters.AddWithValue("@ProductName", product.ProductName);
                        command.Parameters.AddWithValue("@Description", product.Description);
                        command.Parameters.AddWithValue("@WholesalePrice", product.WholesalePrice);
                        command.Parameters.AddWithValue("@RetailPrice", product.RetailPrice);

                        try
                        {
                            connection.Open();
                            int result = command.ExecuteNonQuery();
                            return result > 0;
                        }
                        catch (MySqlException ex)
                        {
                            MessageBox.Show($"MySQL error: {ex.Message}", "Database Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            // Optionally, log the error to a file or database
                            return false;
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show($"An error occurred: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            // Optionally, log the error to a file or database
                            return false;
                        }
                    }
                }
            }



            /// <summary>
            /// Deletes a product from the database by its ID.
            /// </summary>
            /// <param name="productId">The ID of the product to delete.</param>
            /// <returns>True if the product was deleted successfully; otherwise, false.</returns>
            public bool DeleteProduct(int productId)
              {
                using (var connection = new MySqlConnection(connectionString))
                {
                    var query = "DELETE FROM products WHERE ProductId = @ProductId";
                    using (var command = new MySqlCommand(query, connection))
                    {
                        command.Parameters.AddWithValue("@ProductId", productId);
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
            /// Searches for products by a search term in the product name or description.
            /// </summary>
            /// <param name="searchTerm">The search term to use.</param>
            /// <returns>A list of products that match the search term.</returns>
            public List<Product> SearchProducts(string searchTerm)
            {
                var products = new List<Product>();
                using (var connection = new MySqlConnection(connectionString))
                {
                    var query = @"
                        SELECT ProductId, CategoryId, ProductName, Description, RetailPrice, WholesalePrice
                        FROM products
                        WHERE ProductName LIKE @SearchTerm OR Description LIKE @SearchTerm";
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
                                    var product = new Product
                                    {
                                        ProductId = reader.GetInt32("ProductId"),
                                        CategoryId = reader.GetInt32("CategoryId"),
                                        ProductName = reader.GetString("ProductName"),
                                        Description = reader.GetString("Description"),
                                        RetailPrice = reader.GetDecimal("RetailPrice"),
                                        WholesalePrice = reader.GetDecimal("WholesalePrice")
                                    };
                                    products.Add(product);
                                }
                            }
                            return products;
                        }
                        catch (MySqlException ex)
                        {
                            // Log MySQL-specific exception details here using your preferred logging framework
                            Console.WriteLine("MySQL error: " + ex.Message); // Replace with your logging mechanism
                                                                             // Optionally, rethrow the exception to let the caller handle it
                            throw;
                        }
                        catch (Exception ex)
                        {
                            // Log general exception details here using your preferred logging framework
                            Console.WriteLine("An error occurred: " + ex.Message); // Replace with your logging mechanism
                                                                                   // Optionally, rethrow the exception to let the caller handle it
                            throw;
                        }
                    }
                }
            }

        }
    }
    }

