namespace Cst_345_Milestone4
{
    partial class FrmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblCategories = new System.Windows.Forms.Label();
            this.lblDescription = new System.Windows.Forms.Label();
            this.lblCategoryName = new System.Windows.Forms.Label();
            this.btnAddCategories = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txtCategoryDescription = new System.Windows.Forms.TextBox();
            this.txtCategoryName = new System.Windows.Forms.TextBox();
            this.btnShowAllCategories = new System.Windows.Forms.Button();
            this.txtSearchCategories = new System.Windows.Forms.TextBox();
            this.btnSearchCategories = new System.Windows.Forms.Button();
            this.btnDeleteSelectedCategory = new System.Windows.Forms.Button();
            this.gvCategories = new System.Windows.Forms.DataGridView();
            this.btnDeleteSelectedProduct = new System.Windows.Forms.Button();
            this.btnSearchProducts = new System.Windows.Forms.Button();
            this.txtSearchProducts = new System.Windows.Forms.TextBox();
            this.btnShowAllProducts = new System.Windows.Forms.Button();
            this.lblProducts = new System.Windows.Forms.Label();
            this.gvProducts = new System.Windows.Forms.DataGridView();
            this.lblProductName = new System.Windows.Forms.Label();
            this.lblProductsDescription = new System.Windows.Forms.Label();
            this.lblWholesalePrice = new System.Windows.Forms.Label();
            this.lblRetailPrice = new System.Windows.Forms.Label();
            this.txtProductName = new System.Windows.Forms.TextBox();
            this.txtProductDescription = new System.Windows.Forms.TextBox();
            this.txtWholesalePrice = new System.Windows.Forms.TextBox();
            this.txtRetailPrice = new System.Windows.Forms.TextBox();
            this.btnAddProduct = new System.Windows.Forms.Button();
            this.gbProducts = new System.Windows.Forms.GroupBox();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.gvCategories)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.gvProducts)).BeginInit();
            this.gbProducts.SuspendLayout();
            this.SuspendLayout();
            // 
            // lblCategories
            // 
            this.lblCategories.AutoSize = true;
            this.lblCategories.Location = new System.Drawing.Point(289, 27);
            this.lblCategories.Name = "lblCategories";
            this.lblCategories.Size = new System.Drawing.Size(57, 13);
            this.lblCategories.TabIndex = 0;
            this.lblCategories.Text = "Categories";
            // 
            // lblDescription
            // 
            this.lblDescription.AutoSize = true;
            this.lblDescription.Location = new System.Drawing.Point(6, 66);
            this.lblDescription.Name = "lblDescription";
            this.lblDescription.Size = new System.Drawing.Size(60, 13);
            this.lblDescription.TabIndex = 1;
            this.lblDescription.Text = "Description";
            // 
            // lblCategoryName
            // 
            this.lblCategoryName.AutoSize = true;
            this.lblCategoryName.Location = new System.Drawing.Point(6, 16);
            this.lblCategoryName.Name = "lblCategoryName";
            this.lblCategoryName.Size = new System.Drawing.Size(80, 13);
            this.lblCategoryName.TabIndex = 2;
            this.lblCategoryName.Text = "Category Name";
            // 
            // btnAddCategories
            // 
            this.btnAddCategories.Location = new System.Drawing.Point(11, 116);
            this.btnAddCategories.Name = "btnAddCategories";
            this.btnAddCategories.Size = new System.Drawing.Size(75, 23);
            this.btnAddCategories.TabIndex = 3;
            this.btnAddCategories.Text = "Add";
            this.btnAddCategories.UseVisualStyleBackColor = true;
            this.btnAddCategories.Click += new System.EventHandler(this.BtnAddCategories_ClickEvent);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.txtCategoryDescription);
            this.groupBox1.Controls.Add(this.lblCategoryName);
            this.groupBox1.Controls.Add(this.txtCategoryName);
            this.groupBox1.Controls.Add(this.lblDescription);
            this.groupBox1.Controls.Add(this.btnAddCategories);
            this.groupBox1.Location = new System.Drawing.Point(12, 24);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(223, 174);
            this.groupBox1.TabIndex = 4;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Add Category";
            // 
            // txtCategoryDescription
            // 
            this.txtCategoryDescription.Location = new System.Drawing.Point(9, 82);
            this.txtCategoryDescription.Name = "txtCategoryDescription";
            this.txtCategoryDescription.Size = new System.Drawing.Size(157, 20);
            this.txtCategoryDescription.TabIndex = 6;
            // 
            // txtCategoryName
            // 
            this.txtCategoryName.Location = new System.Drawing.Point(9, 32);
            this.txtCategoryName.Name = "txtCategoryName";
            this.txtCategoryName.Size = new System.Drawing.Size(157, 20);
            this.txtCategoryName.TabIndex = 5;
            // 
            // btnShowAllCategories
            // 
            this.btnShowAllCategories.Location = new System.Drawing.Point(352, 22);
            this.btnShowAllCategories.Name = "btnShowAllCategories";
            this.btnShowAllCategories.Size = new System.Drawing.Size(75, 23);
            this.btnShowAllCategories.TabIndex = 7;
            this.btnShowAllCategories.Text = "Show all";
            this.btnShowAllCategories.UseVisualStyleBackColor = true;
            this.btnShowAllCategories.Click += new System.EventHandler(this.BtnShowAllCategories_ClickEvent);
            // 
            // txtSearchCategories
            // 
            this.txtSearchCategories.Location = new System.Drawing.Point(433, 24);
            this.txtSearchCategories.Name = "txtSearchCategories";
            this.txtSearchCategories.Size = new System.Drawing.Size(166, 20);
            this.txtSearchCategories.TabIndex = 8;
            // 
            // btnSearchCategories
            // 
            this.btnSearchCategories.Location = new System.Drawing.Point(605, 21);
            this.btnSearchCategories.Name = "btnSearchCategories";
            this.btnSearchCategories.Size = new System.Drawing.Size(75, 23);
            this.btnSearchCategories.TabIndex = 9;
            this.btnSearchCategories.Text = "Search";
            this.btnSearchCategories.UseVisualStyleBackColor = true;
            this.btnSearchCategories.Click += new System.EventHandler(this.BtnSearchCategories_ClickEvent);
            // 
            // btnDeleteSelectedCategory
            // 
            this.btnDeleteSelectedCategory.Location = new System.Drawing.Point(686, 21);
            this.btnDeleteSelectedCategory.Name = "btnDeleteSelectedCategory";
            this.btnDeleteSelectedCategory.Size = new System.Drawing.Size(155, 23);
            this.btnDeleteSelectedCategory.TabIndex = 10;
            this.btnDeleteSelectedCategory.Text = "Delete selected category";
            this.btnDeleteSelectedCategory.UseVisualStyleBackColor = true;
            this.btnDeleteSelectedCategory.Click += new System.EventHandler(this.BtnDeleteSelectedCategory_ClickEvent);
            // 
            // gvCategories
            // 
            this.gvCategories.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.gvCategories.Location = new System.Drawing.Point(381, 56);
            this.gvCategories.Name = "gvCategories";
            this.gvCategories.Size = new System.Drawing.Size(346, 128);
            this.gvCategories.TabIndex = 11;
            this.gvCategories.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.gvCategories_CellClick);
            // 
            // btnDeleteSelectedProduct
            // 
            this.btnDeleteSelectedProduct.Location = new System.Drawing.Point(686, 245);
            this.btnDeleteSelectedProduct.Name = "btnDeleteSelectedProduct";
            this.btnDeleteSelectedProduct.Size = new System.Drawing.Size(155, 23);
            this.btnDeleteSelectedProduct.TabIndex = 17;
            this.btnDeleteSelectedProduct.Text = "Delete selected product";
            this.btnDeleteSelectedProduct.UseVisualStyleBackColor = true;
            this.btnDeleteSelectedProduct.Click += new System.EventHandler(this.BtnDeleteSelectedProduct_ClickEvent);
            // 
            // btnSearchProducts
            // 
            this.btnSearchProducts.Location = new System.Drawing.Point(605, 245);
            this.btnSearchProducts.Name = "btnSearchProducts";
            this.btnSearchProducts.Size = new System.Drawing.Size(75, 23);
            this.btnSearchProducts.TabIndex = 16;
            this.btnSearchProducts.Text = "Search";
            this.btnSearchProducts.UseVisualStyleBackColor = true;
            this.btnSearchProducts.Click += new System.EventHandler(this.BtnSearchProducts_ClickEvent);
            // 
            // txtSearchProducts
            // 
            this.txtSearchProducts.Location = new System.Drawing.Point(433, 245);
            this.txtSearchProducts.Name = "txtSearchProducts";
            this.txtSearchProducts.Size = new System.Drawing.Size(166, 20);
            this.txtSearchProducts.TabIndex = 15;
            // 
            // btnShowAllProducts
            // 
            this.btnShowAllProducts.Location = new System.Drawing.Point(352, 242);
            this.btnShowAllProducts.Name = "btnShowAllProducts";
            this.btnShowAllProducts.Size = new System.Drawing.Size(75, 23);
            this.btnShowAllProducts.TabIndex = 14;
            this.btnShowAllProducts.Text = "Show all";
            this.btnShowAllProducts.UseVisualStyleBackColor = true;
            this.btnShowAllProducts.Click += new System.EventHandler(this.BtnShowAllProducts_ClickEvent);
            // 
            // lblProducts
            // 
            this.lblProducts.AutoSize = true;
            this.lblProducts.Location = new System.Drawing.Point(289, 250);
            this.lblProducts.Name = "lblProducts";
            this.lblProducts.Size = new System.Drawing.Size(49, 13);
            this.lblProducts.TabIndex = 13;
            this.lblProducts.Text = "Products";
            // 
            // gvProducts
            // 
            this.gvProducts.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.gvProducts.Location = new System.Drawing.Point(241, 282);
            this.gvProducts.Name = "gvProducts";
            this.gvProducts.Size = new System.Drawing.Size(645, 159);
            this.gvProducts.TabIndex = 18;
            // 
            // lblProductName
            // 
            this.lblProductName.AutoSize = true;
            this.lblProductName.Location = new System.Drawing.Point(2, 15);
            this.lblProductName.Name = "lblProductName";
            this.lblProductName.Size = new System.Drawing.Size(73, 13);
            this.lblProductName.TabIndex = 20;
            this.lblProductName.Text = "Product name";
            // 
            // lblProductsDescription
            // 
            this.lblProductsDescription.AutoSize = true;
            this.lblProductsDescription.Location = new System.Drawing.Point(4, 58);
            this.lblProductsDescription.Name = "lblProductsDescription";
            this.lblProductsDescription.Size = new System.Drawing.Size(60, 13);
            this.lblProductsDescription.TabIndex = 7;
            this.lblProductsDescription.Text = "Description";
            // 
            // lblWholesalePrice
            // 
            this.lblWholesalePrice.AutoSize = true;
            this.lblWholesalePrice.Location = new System.Drawing.Point(4, 97);
            this.lblWholesalePrice.Name = "lblWholesalePrice";
            this.lblWholesalePrice.Size = new System.Drawing.Size(84, 13);
            this.lblWholesalePrice.TabIndex = 21;
            this.lblWholesalePrice.Text = "Wholesale Price";
            // 
            // lblRetailPrice
            // 
            this.lblRetailPrice.AutoSize = true;
            this.lblRetailPrice.Location = new System.Drawing.Point(2, 136);
            this.lblRetailPrice.Name = "lblRetailPrice";
            this.lblRetailPrice.Size = new System.Drawing.Size(57, 13);
            this.lblRetailPrice.TabIndex = 22;
            this.lblRetailPrice.Text = "Retail pice";
            // 
            // txtProductName
            // 
            this.txtProductName.Location = new System.Drawing.Point(5, 35);
            this.txtProductName.Name = "txtProductName";
            this.txtProductName.Size = new System.Drawing.Size(100, 20);
            this.txtProductName.TabIndex = 23;
            // 
            // txtProductDescription
            // 
            this.txtProductDescription.Location = new System.Drawing.Point(5, 74);
            this.txtProductDescription.Name = "txtProductDescription";
            this.txtProductDescription.Size = new System.Drawing.Size(100, 20);
            this.txtProductDescription.TabIndex = 24;
            // 
            // txtWholesalePrice
            // 
            this.txtWholesalePrice.Location = new System.Drawing.Point(5, 113);
            this.txtWholesalePrice.Name = "txtWholesalePrice";
            this.txtWholesalePrice.Size = new System.Drawing.Size(100, 20);
            this.txtWholesalePrice.TabIndex = 25;
            // 
            // txtRetailPrice
            // 
            this.txtRetailPrice.Location = new System.Drawing.Point(5, 152);
            this.txtRetailPrice.Name = "txtRetailPrice";
            this.txtRetailPrice.Size = new System.Drawing.Size(100, 20);
            this.txtRetailPrice.TabIndex = 26;
            // 
            // btnAddProduct
            // 
            this.btnAddProduct.Location = new System.Drawing.Point(30, 189);
            this.btnAddProduct.Name = "btnAddProduct";
            this.btnAddProduct.Size = new System.Drawing.Size(75, 23);
            this.btnAddProduct.TabIndex = 7;
            this.btnAddProduct.Text = "Add";
            this.btnAddProduct.UseVisualStyleBackColor = true;
            this.btnAddProduct.Click += new System.EventHandler(this.BtnAddProduct_ClickEvent);
            // 
            // gbProducts
            // 
            this.gbProducts.Controls.Add(this.lblProductName);
            this.gbProducts.Controls.Add(this.btnAddProduct);
            this.gbProducts.Controls.Add(this.lblProductsDescription);
            this.gbProducts.Controls.Add(this.txtRetailPrice);
            this.gbProducts.Controls.Add(this.lblWholesalePrice);
            this.gbProducts.Controls.Add(this.txtWholesalePrice);
            this.gbProducts.Controls.Add(this.lblRetailPrice);
            this.gbProducts.Controls.Add(this.txtProductDescription);
            this.gbProducts.Controls.Add(this.txtProductName);
            this.gbProducts.Location = new System.Drawing.Point(12, 220);
            this.gbProducts.Name = "gbProducts";
            this.gbProducts.Size = new System.Drawing.Size(223, 232);
            this.gbProducts.TabIndex = 27;
            this.gbProducts.TabStop = false;
            this.gbProducts.Text = "add products";
            // 
            // FrmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(892, 464);
            this.Controls.Add(this.gbProducts);
            this.Controls.Add(this.gvProducts);
            this.Controls.Add(this.btnDeleteSelectedProduct);
            this.Controls.Add(this.btnSearchProducts);
            this.Controls.Add(this.txtSearchProducts);
            this.Controls.Add(this.btnShowAllProducts);
            this.Controls.Add(this.lblProducts);
            this.Controls.Add(this.gvCategories);
            this.Controls.Add(this.btnDeleteSelectedCategory);
            this.Controls.Add(this.btnSearchCategories);
            this.Controls.Add(this.txtSearchCategories);
            this.Controls.Add(this.btnShowAllCategories);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.lblCategories);
            this.Name = "FrmMain";
            this.Text = "Products";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.gvCategories)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.gvProducts)).EndInit();
            this.gbProducts.ResumeLayout(false);
            this.gbProducts.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblCategories;
        private System.Windows.Forms.Label lblDescription;
        private System.Windows.Forms.Label lblCategoryName;
        private System.Windows.Forms.Button btnAddCategories;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtCategoryDescription;
        private System.Windows.Forms.TextBox txtCategoryName;
        private System.Windows.Forms.Button btnShowAllCategories;
        private System.Windows.Forms.TextBox txtSearchCategories;
        private System.Windows.Forms.Button btnSearchCategories;
        private System.Windows.Forms.Button btnDeleteSelectedCategory;
        private System.Windows.Forms.DataGridView gvCategories;
        private System.Windows.Forms.Button btnDeleteSelectedProduct;
        private System.Windows.Forms.Button btnSearchProducts;
        private System.Windows.Forms.TextBox txtSearchProducts;
        private System.Windows.Forms.Button btnShowAllProducts;
        private System.Windows.Forms.Label lblProducts;
        private System.Windows.Forms.DataGridView gvProducts;
       
        private System.Windows.Forms.Label lblProductName;
        private System.Windows.Forms.Label lblProductsDescription;
        private System.Windows.Forms.Label lblWholesalePrice;
        private System.Windows.Forms.Label lblRetailPrice;
        private System.Windows.Forms.TextBox txtProductName;
        private System.Windows.Forms.TextBox txtProductDescription;
        private System.Windows.Forms.TextBox txtWholesalePrice;
        private System.Windows.Forms.TextBox txtRetailPrice;
        private System.Windows.Forms.Button btnAddProduct;
        private System.Windows.Forms.GroupBox gbProducts;
    }
}

