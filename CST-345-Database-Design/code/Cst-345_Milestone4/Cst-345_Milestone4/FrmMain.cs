using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static Cst_345_Milestone4.Category;
using static Cst_345_Milestone4.product;

namespace Cst_345_Milestone4
{
    public partial class FrmMain : Form
    {
        private CategoryDAO categoryDao = new CategoryDAO();
        private ProductDAO productDao = new ProductDAO();

        public FrmMain()
        {


            InitializeComponent();
            // Load initial data.
            LoadAllCategories();
            LoadAllProducts();

        }
        public int selectedCategoryId = -1;

        private void LoadAllCategories()
        {
            try
            {
                var categories = categoryDao.GetAllCategories();
                gvCategories.DataSource = new BindingList<Category>(categories); // Binding the list to the DataGridView.
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred while loading categories: " + ex.Message);
            }
        }

        private void LoadAllProducts()
        {
            {
                try
                {
                    var products = productDao.GetAllProducts();
                    gvProducts.DataSource = new BindingList<Product>(products); // Binding the list to the DataGridView.
                }
                catch (Exception ex)
                {
                    MessageBox.Show("An error occurred while loading categories: " + ex.Message);
                }
            }
        }



        private void BtnShowAllCategories_ClickEvent(object sender, EventArgs e)
        {

            LoadAllCategories();

        }


        private void BtnSearchCategories_ClickEvent(object sender, EventArgs e)
        {
            try
            {
                var searchTerm = txtSearchCategories.Text; // Assuming you have a textbox for category search
                var categories = categoryDao.SearchCategories(searchTerm);
                gvCategories.DataSource = categories;
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred while searching for categories: " + ex.Message);
            }
        }


        private void BtnAddCategories_ClickEvent(object sender, EventArgs e)
        {
            // Create a new instance of the Category class and assign the values from the form controls
            var category = new Category
            {
                CategoryName = txtCategoryName.Text,
                CategoryDesc = txtCategoryDescription.Text
            };

            // Call AddCategory method of CategoryDAO which encapsulates the database logic
            bool isAdded = categoryDao.AddCategory(category);
            if (isAdded)
            {
                MessageBox.Show("Category added successfully.");
                LoadAllCategories(); // Refresh the categories list
            }
            else
            {
                MessageBox.Show("Category could not be added.");
            }
        }


        private void BtnDeleteSelectedCategory_ClickEvent(object sender, EventArgs e)
        {
            try
            {
                if (gvCategories.SelectedRows.Count > 0)
                {
                    int categoryId = Convert.ToInt32(gvCategories.SelectedRows[0].Cells["CategoryId"].Value);
                    if (categoryDao.DeleteCategory(categoryId))
                    {
                        MessageBox.Show("Category deleted successfully.");
                        LoadAllCategories();
                    }
                    else
                    {
                        MessageBox.Show("Category could not be deleted.");
                    }
                }
                else
                {
                    MessageBox.Show("Please select a category to delete.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred: " + ex.Message);
            }
        }


        private void BtnShowAllProducts_ClickEvent(object sender, EventArgs e)
        {
            LoadAllProducts();
        }

        private void BtnSearchProducts_ClickEvent(object sender, EventArgs e)
        {
            try
            {
                var searchTerm = txtSearchProducts.Text; // Assuming you have a textbox for product search
                var products = productDao.SearchProducts(searchTerm);
                gvProducts.DataSource = products;
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred while searching for products: " + ex.Message);
            }
        }


        private void BtnDeleteSelectedProduct_ClickEvent(object sender, EventArgs e)
        {
            try
            {
                if (gvProducts.SelectedRows.Count > 0)
                {
                    int productId = Convert.ToInt32(gvProducts.SelectedRows[0].Cells["ProductId"].Value);
                    if (productDao.DeleteProduct(productId))
                    {
                        MessageBox.Show("Product deleted successfully.");
                        LoadAllProducts();
                    }
                    else
                    {
                        MessageBox.Show("Product could not be deleted.");
                    }
                }
                else
                {
                    MessageBox.Show("Please select a product to delete.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred: " + ex.Message);
            }
        }


        private void BtnAddProduct_ClickEvent(object sender, EventArgs e)
        {
            if (selectedCategoryId == -1)
            {
                MessageBox.Show("Please select a category for the product.");
                return;
            }

            // No need to re-declare selectedCategoryId here, just use the class member directly

            var product = new Product
            {
                CategoryId = selectedCategoryId,
                ProductName = txtProductName.Text,
                Description = txtProductDescription.Text,
                WholesalePrice = decimal.Parse(txtWholesalePrice.Text),
                RetailPrice = decimal.Parse(txtRetailPrice.Text)
            };

            bool isAdded = productDao.AddProduct(product);
            if (isAdded)
            {
                MessageBox.Show("Product added successfully.");
                LoadAllProducts(); // Refresh the products list
            }
            else
            {
                MessageBox.Show("Product could not be added.");
            }
        }



        // Event handler for the DataGridView CellClick event
        private void gvCategories_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex != -1) // Check that the header row is not clicked
            {
                int categoryId = Convert.ToInt32(gvCategories.Rows[e.RowIndex].Cells["CategoryId"].Value);
                LoadProductsByCategory(categoryId);
            }
            if (e.RowIndex >= 0)
            {
                // Assuming the first column contains the CategoryId
                selectedCategoryId = Convert.ToInt32(gvCategories.Rows[e.RowIndex].Cells["CategoryId"].Value);
            }
        }



        private void LoadProductsByCategory(int categoryId)
        {
            try
            {
                var products = productDao.GetProductsByCategory(categoryId);
                if (products != null && products.Any())
                {
                    gvProducts.DataSource = new BindingList<Product>(products);
                }
                else
                {
                    gvProducts.DataSource = null; // Clear the data grid if no products found
                    MessageBox.Show("No products found for the selected category.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred while loading products: " + ex.Message);
            }
        }
    }
}

