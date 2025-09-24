namespace CarShopGUI
{
    partial class FormMain : Form
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            gbCreateCar = new GroupBox();
            rbUsed = new RadioButton();
            lblYear = new Label();
            txtYear = new TextBox();
            rbNew = new RadioButton();
            lblMake = new Label();
            lblModel = new Label();
            lblPrice = new Label();
            btnCreateCar = new Button();
            txtPrice = new TextBox();
            txtModel = new TextBox();
            txtMake = new TextBox();
            gbCarInventory = new GroupBox();
            lbCarInventory = new ListBox();
            gbShoppingCart = new GroupBox();
            lbShoppingCart = new ListBox();
            btnAddToCart = new Button();
            btnCheckout = new Button();
            lblTotalCost = new Label();
            lblDisplayTotal = new Label();
            gbCreateCar.SuspendLayout();
            gbCarInventory.SuspendLayout();
            gbShoppingCart.SuspendLayout();
            SuspendLayout();
            // 
            // gbCreateCar
            // 
            gbCreateCar.BackColor = SystemColors.ActiveCaption;
            gbCreateCar.Controls.Add(rbUsed);
            gbCreateCar.Controls.Add(lblYear);
            gbCreateCar.Controls.Add(txtYear);
            gbCreateCar.Controls.Add(rbNew);
            gbCreateCar.Controls.Add(lblMake);
            gbCreateCar.Controls.Add(lblModel);
            gbCreateCar.Controls.Add(lblPrice);
            gbCreateCar.Controls.Add(btnCreateCar);
            gbCreateCar.Controls.Add(txtPrice);
            gbCreateCar.Controls.Add(txtModel);
            gbCreateCar.Controls.Add(txtMake);
            gbCreateCar.Font = new Font("Microsoft Sans Serif", 9F, FontStyle.Regular, GraphicsUnit.Point);
            gbCreateCar.Location = new Point(12, 12);
            gbCreateCar.Name = "gbCreateCar";
            gbCreateCar.Size = new Size(200, 258);
            gbCreateCar.TabIndex = 0;
            gbCreateCar.TabStop = false;
            gbCreateCar.Text = "Create a car";
            // 
            // rbUsed
            // 
            rbUsed.AutoSize = true;
            rbUsed.Location = new Point(76, 172);
            rbUsed.Name = "rbUsed";
            rbUsed.Size = new Size(54, 19);
            rbUsed.TabIndex = 12;
            rbUsed.TabStop = true;
            rbUsed.Text = "Used";
            rbUsed.UseVisualStyleBackColor = true;
            // 
            // lblYear
            // 
            lblYear.AutoSize = true;
            lblYear.Location = new Point(25, 121);
            lblYear.Name = "lblYear";
            lblYear.Size = new Size(32, 15);
            lblYear.TabIndex = 11;
            lblYear.Text = "Year";
            // 
            // txtYear
            // 
            txtYear.Location = new Point(70, 118);
            txtYear.Name = "txtYear";
            txtYear.Size = new Size(100, 21);
            txtYear.TabIndex = 10;
            // 
            // rbNew
            // 
            rbNew.AutoSize = true;
            rbNew.Location = new Point(76, 147);
            rbNew.Name = "rbNew";
            rbNew.Size = new Size(50, 19);
            rbNew.TabIndex = 7;
            rbNew.TabStop = true;
            rbNew.Text = "New";
            rbNew.UseVisualStyleBackColor = true;
            // 
            // lblMake
            // 
            lblMake.AutoSize = true;
            lblMake.Location = new Point(25, 31);
            lblMake.Name = "lblMake";
            lblMake.Size = new Size(41, 15);
            lblMake.TabIndex = 9;
            lblMake.Text = "Make:";
            // 
            // lblModel
            // 
            lblModel.AutoSize = true;
            lblModel.Location = new Point(20, 63);
            lblModel.Name = "lblModel";
            lblModel.Size = new Size(45, 15);
            lblModel.TabIndex = 8;
            lblModel.Text = "Model:";
            // 
            // lblPrice
            // 
            lblPrice.AutoSize = true;
            lblPrice.Location = new Point(26, 89);
            lblPrice.Name = "lblPrice";
            lblPrice.Size = new Size(38, 15);
            lblPrice.TabIndex = 7;
            lblPrice.Text = "Price:";
            // 
            // btnCreateCar
            // 
            btnCreateCar.BackColor = Color.Black;
            btnCreateCar.FlatStyle = FlatStyle.System;
            btnCreateCar.Font = new Font("Microsoft Sans Serif", 9F, FontStyle.Regular, GraphicsUnit.Point);
            btnCreateCar.ForeColor = SystemColors.ActiveBorder;
            btnCreateCar.Location = new Point(43, 210);
            btnCreateCar.Name = "btnCreateCar";
            btnCreateCar.Size = new Size(75, 29);
            btnCreateCar.TabIndex = 3;
            btnCreateCar.Text = "create car";
            btnCreateCar.TextAlign = ContentAlignment.TopCenter;
            btnCreateCar.UseVisualStyleBackColor = false;
            btnCreateCar.Click += BtnCreateCar_OnClick_EventHandler;
            // 
            // txtPrice
            // 
            txtPrice.Location = new Point(70, 89);
            txtPrice.Name = "txtPrice";
            txtPrice.Size = new Size(100, 21);
            txtPrice.TabIndex = 2;
            // 
            // txtModel
            // 
            txtModel.Location = new Point(70, 60);
            txtModel.Name = "txtModel";
            txtModel.Size = new Size(100, 21);
            txtModel.TabIndex = 1;
            // 
            // txtMake
            // 
            txtMake.Location = new Point(70, 31);
            txtMake.Name = "txtMake";
            txtMake.Size = new Size(100, 21);
            txtMake.TabIndex = 0;
            // 
            // gbCarInventory
            // 
            gbCarInventory.BackColor = SystemColors.ActiveCaption;
            gbCarInventory.Controls.Add(lbCarInventory);
            gbCarInventory.Location = new Point(218, 12);
            gbCarInventory.Name = "gbCarInventory";
            gbCarInventory.Size = new Size(224, 342);
            gbCarInventory.TabIndex = 1;
            gbCarInventory.TabStop = false;
            gbCarInventory.Text = "Car inventory";
            // 
            // lbCarInventory
            // 
            lbCarInventory.FormattingEnabled = true;
            lbCarInventory.ItemHeight = 15;
            lbCarInventory.Location = new Point(0, 22);
            lbCarInventory.Name = "lbCarInventory";
            lbCarInventory.Size = new Size(224, 319);
            lbCarInventory.TabIndex = 0;
            // 
            // gbShoppingCart
            // 
            gbShoppingCart.BackColor = SystemColors.ActiveCaption;
            gbShoppingCart.Controls.Add(lbShoppingCart);
            gbShoppingCart.Location = new Point(588, 12);
            gbShoppingCart.Name = "gbShoppingCart";
            gbShoppingCart.Size = new Size(232, 342);
            gbShoppingCart.TabIndex = 1;
            gbShoppingCart.TabStop = false;
            gbShoppingCart.Text = "Shopping cart";
            // 
            // lbShoppingCart
            // 
            lbShoppingCart.FormattingEnabled = true;
            lbShoppingCart.ItemHeight = 15;
            lbShoppingCart.Location = new Point(0, 22);
            lbShoppingCart.Name = "lbShoppingCart";
            lbShoppingCart.Size = new Size(230, 319);
            lbShoppingCart.TabIndex = 1;
            // 
            // btnAddToCart
            // 
            btnAddToCart.Location = new Point(464, 159);
            btnAddToCart.Name = "btnAddToCart";
            btnAddToCart.Size = new Size(98, 26);
            btnAddToCart.TabIndex = 2;
            btnAddToCart.Text = "add to cart";
            btnAddToCart.UseVisualStyleBackColor = true;
            btnAddToCart.Click += BtnAddToCart_OnClick_EventHandler;
            // 
            // btnCheckout
            // 
            btnCheckout.Location = new Point(648, 360);
            btnCheckout.Name = "btnCheckout";
            btnCheckout.Size = new Size(75, 23);
            btnCheckout.TabIndex = 4;
            btnCheckout.Text = "Checkout";
            btnCheckout.UseVisualStyleBackColor = true;
            btnCheckout.Click += BtnCheckout_OnClick_EventHandler;
            // 
            // lblTotalCost
            // 
            lblTotalCost.AutoSize = true;
            lblTotalCost.Location = new Point(561, 406);
            lblTotalCost.Name = "lblTotalCost";
            lblTotalCost.Size = new Size(62, 15);
            lblTotalCost.TabIndex = 5;
            lblTotalCost.Text = "Total cost:";
            // 
            // lblDisplayTotal
            // 
            lblDisplayTotal.AutoSize = true;
            lblDisplayTotal.Location = new Point(629, 406);
            lblDisplayTotal.Name = "lblDisplayTotal";
            lblDisplayTotal.Size = new Size(55, 15);
            lblDisplayTotal.TabIndex = 6;
            lblDisplayTotal.Text = "amount: ";
            // 
            // FormMain
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(873, 450);
            Controls.Add(lblDisplayTotal);
            Controls.Add(lblTotalCost);
            Controls.Add(btnCheckout);
            Controls.Add(btnAddToCart);
            Controls.Add(gbShoppingCart);
            Controls.Add(gbCarInventory);
            Controls.Add(gbCreateCar);
            Font = new Font("Microsoft Sans Serif", 9F, FontStyle.Regular, GraphicsUnit.Point);
            Name = "FormMain";
            Text = "Car Shop GUI";
            gbCreateCar.ResumeLayout(false);
            gbCreateCar.PerformLayout();
            gbCarInventory.ResumeLayout(false);
            gbShoppingCart.ResumeLayout(false);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private GroupBox gbCreateCar;
        private RadioButton rbUsed;
        private Label lblYear;
        private TextBox txtYear;
        private RadioButton rbNew;
        private Label lblMake;
        private Label lblModel;
        private Label lblPrice;
        private Button btnCreateCar;
        private TextBox txtPrice;
        private TextBox txtModel;
        private TextBox txtMake;
        private GroupBox gbCarInventory;
        private ListBox lbCarInventory;
        private GroupBox gbShoppingCart;
        private ListBox lbShoppingCart;
        private Button btnAddToCart;
        private Button btnCheckout;
        private Label lblTotalCost;
        private Label lblDisplayTotal;
    }
}