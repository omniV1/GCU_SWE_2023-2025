

using TextFileDataAccessDemo;

namespace GuiFileIO
{
    public partial class FrmMain : Form
    {
        public FrmMain()
        {
            InitializeComponent();
        }

        // Event handler for the 'Add to List' button click.
        private void BtnAddToList_Click(object sender, EventArgs e)
        {
            // Create a new Person object using input from the text boxes.
            // Here you may want to add validation for the input.
            Person newPerson = new Person
            {
                FirstName = txtFirstName.Text,
                LastName = txtLastName.Text,
                Url = txtURL.Text
            };

            // Add the new person to the ListBox and clear the text boxes.
            lbxDisplayListofPeople.Items.Add(newPerson);
            txtFirstName.Clear();
            txtLastName.Clear();
            txtURL.Clear();
        }

        // Event handler for the 'Save to File' button click.
        private void BtnSaveToFile_Click(object sender, EventArgs e)
        {
            using (SaveFileDialog sfd = new SaveFileDialog())
            {
                sfd.Filter = "Text Files|*..txt|All Files|*.*";
                sfd.Title = "Save People List";

                if (sfd.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        List<string> linesToWrite = new List<string>();
                        foreach (Person person in lbxDisplayListofPeople.Items)
                        {
                            // Use the overridden ToString method for consistent formatting
                            linesToWrite.Add(person.ToString());
                        }
                        File.WriteAllLines(sfd.FileName, linesToWrite);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show($"Error saving file: {ex.Message}", "Save Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }


        // Event handler for the 'Load from File' button click.
        private void BtnLoadFromFile_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog ofd = new OpenFileDialog())
            {
                ofd.Filter = "Text Files|*.txt|All Files|*.*";
                ofd.Title = "Open People List";

                // Show the Open File Dialog. If the user clicks OK, load the data.
                if (ofd.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        lbxDisplayListofPeople.Items.Clear();
                        string[] linesToRead = File.ReadAllLines(ofd.FileName);
                        foreach (string line in linesToRead)
                        {
                            string[] parts = line.Split(',');
                            if (parts.Length == 3)
                            {
                                lbxDisplayListofPeople.Items.Add(new Person
                                {
                                    FirstName = parts[0],
                                    LastName = parts[1],
                                    Url = parts[2]
                                });
                            }
                            else
                            {
                                // Inform the user if a line does not have 3 parts.
                                MessageBox.Show($"Invalid line format: {line}", "Format Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            }
                        }
                    }
                    catch (Exception ex)
                    {
                        // Inform the user if an error occurs during the load operation.
                        MessageBox.Show($"Error loading file: {ex.Message}", "Load Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }
    }
}
