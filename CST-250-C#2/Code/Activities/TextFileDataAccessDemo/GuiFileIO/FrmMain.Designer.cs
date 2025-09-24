namespace GuiFileIO
{
    partial class FrmMain
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
            txtFirstName = new TextBox();
            txtLastName = new TextBox();
            txtURL = new TextBox();
            lblFirstName = new Label();
            lblLastName = new Label();
            lblUrl = new Label();
            btnAddToList = new Button();
            btnSaveToFile = new Button();
            btnLoadFromFile = new Button();
            lbxDisplayListofPeople = new ListBox();
            SuspendLayout();
            // 
            // txtFirstName
            // 
            txtFirstName.Location = new Point(143, 23);
            txtFirstName.Name = "txtFirstName";
            txtFirstName.Size = new Size(163, 23);
            txtFirstName.TabIndex = 0;
            // 
            // txtLastName
            // 
            txtLastName.Location = new Point(143, 68);
            txtLastName.Name = "txtLastName";
            txtLastName.Size = new Size(163, 23);
            txtLastName.TabIndex = 1;
            // 
            // txtURL
            // 
            txtURL.Location = new Point(143, 111);
            txtURL.Name = "txtURL";
            txtURL.Size = new Size(163, 23);
            txtURL.TabIndex = 2;
            // 
            // lblFirstName
            // 
            lblFirstName.AutoSize = true;
            lblFirstName.Font = new Font("Verdana", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblFirstName.Location = new Point(21, 23);
            lblFirstName.Name = "lblFirstName";
            lblFirstName.Size = new Size(104, 18);
            lblFirstName.TabIndex = 3;
            lblFirstName.Text = "First Name:";
            // 
            // lblLastName
            // 
            lblLastName.AutoSize = true;
            lblLastName.Font = new Font("Verdana", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblLastName.Location = new Point(22, 73);
            lblLastName.Name = "lblLastName";
            lblLastName.Size = new Size(103, 18);
            lblLastName.TabIndex = 4;
            lblLastName.Text = "Last Name:";
            // 
            // lblUrl
            // 
            lblUrl.AutoSize = true;
            lblUrl.Font = new Font("Verdana", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblUrl.Location = new Point(45, 111);
            lblUrl.Name = "lblUrl";
            lblUrl.Size = new Size(47, 18);
            lblUrl.TabIndex = 5;
            lblUrl.Text = "URL:";
            // 
            // btnAddToList
            // 
            btnAddToList.BackColor = SystemColors.Control;
            btnAddToList.Location = new Point(21, 178);
            btnAddToList.Name = "btnAddToList";
            btnAddToList.Size = new Size(139, 33);
            btnAddToList.TabIndex = 6;
            btnAddToList.Text = "Add to list -->";
            btnAddToList.UseVisualStyleBackColor = false;
            btnAddToList.Click += BtnAddToList_Click;
            // 
            // btnSaveToFile
            // 
            btnSaveToFile.BackColor = SystemColors.Control;
            btnSaveToFile.Location = new Point(71, 281);
            btnSaveToFile.Name = "btnSaveToFile";
            btnSaveToFile.Size = new Size(126, 33);
            btnSaveToFile.TabIndex = 7;
            btnSaveToFile.Text = "Save to File";
            btnSaveToFile.UseVisualStyleBackColor = false;
            btnSaveToFile.Click += BtnSaveToFile_Click;
            // 
            // btnLoadFromFile
            // 
            btnLoadFromFile.BackColor = SystemColors.Control;
            btnLoadFromFile.Location = new Point(71, 341);
            btnLoadFromFile.Name = "btnLoadFromFile";
            btnLoadFromFile.Size = new Size(126, 33);
            btnLoadFromFile.TabIndex = 8;
            btnLoadFromFile.Text = "Load From File";
            btnLoadFromFile.UseVisualStyleBackColor = false;
            btnLoadFromFile.Click += BtnLoadFromFile_Click;
            // 
            // lbxDisplayListofPeople
            // 
            lbxDisplayListofPeople.FormattingEnabled = true;
            lbxDisplayListofPeople.ItemHeight = 15;
            lbxDisplayListofPeople.Location = new Point(328, 12);
            lbxDisplayListofPeople.Name = "lbxDisplayListofPeople";
            lbxDisplayListofPeople.Size = new Size(438, 424);
            lbxDisplayListofPeople.TabIndex = 9;
            // 
            // FrmMain
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.ActiveBorder;
            ClientSize = new Size(800, 450);
            Controls.Add(lbxDisplayListofPeople);
            Controls.Add(btnLoadFromFile);
            Controls.Add(btnSaveToFile);
            Controls.Add(btnAddToList);
            Controls.Add(lblUrl);
            Controls.Add(lblLastName);
            Controls.Add(lblFirstName);
            Controls.Add(txtURL);
            Controls.Add(txtLastName);
            Controls.Add(txtFirstName);
            Name = "FrmMain";
            Text = "People I know";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox txtFirstName;
        private TextBox txtLastName;
        private TextBox txtURL;
        private Label lblFirstName;
        private Label lblLastName;
        private Label lblUrl;
        private Button btnAddToList;
        private Button btnSaveToFile;
        private Button btnLoadFromFile;
        private ListBox lbxDisplayListofPeople;
    }
}
