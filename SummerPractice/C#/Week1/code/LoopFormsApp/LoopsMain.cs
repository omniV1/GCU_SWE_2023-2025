using System;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace LoopFormsApp
{
    public partial class LoopsMain : Form
    {
        public LoopsMain()
        {
            InitializeComponent();
            // Attach event handler to button click
            btnResult.Click += BtnResult_Click;
        }

        /// <summary>
        /// Handles the Click event of the btnResult control.
        /// Processes the input text to display vowels or consonants and their positions.
        /// </summary>
        private void BtnResult_Click(object sender, EventArgs e)
        {
            // Get user input from the text box
            string input = txtSentence.Text;

            // Validate input
            if (string.IsNullOrWhiteSpace(input))
            {
                lblResults.Text = "Please enter a valid sentence.";
                return;
            }

            // Check if an option is selected
            if (!rbDisplayVowel.Checked && !rbDisplayCon.Checked)
            {
                lblResults.Text = "Please select an option to display vowels or consonants.";
                return;
            }

            // Initialize StringBuilder for formatted output
            StringBuilder output = new StringBuilder();

            if (rbDisplayVowel.Checked)
            {
                // Select character and index, filter vowels, and format with padding
                var vowels = input
                    .Select((c, i) => (Character: c, Index: i))
                    .Where(x => "aeiouAEIOU".Contains(x.Character))
                    .Select(x => $"{x.Character} at position {x.Index}".PadRight(20))
                    .ToList();

                // Header for output
                output.AppendLine("Vowels and their positions:");

                // Append each formatted vowel to output
                vowels.ForEach(v => output.AppendLine(v));
            }
            else if (rbDisplayCon.Checked)
            {
                // Select character and index, filter consonants, and format with padding
                var consonants = input
                    .Select((c, i) => (Character: c, Index: i))
                    .Where(x => !"aeiouAEIOU".Contains(x.Character) && char.IsLetter(x.Character))
                    .Select(x => $"{x.Character} at position {x.Index}".PadRight(20))
                    .ToList();

                // Header for output
                output.AppendLine("Consonants and their positions:");

                // Append each formatted consonant to output
                consonants.ForEach(c => output.AppendLine(c));
            }

            // Display the formatted output
            lblResults.Text = output.ToString();
        }
    }
}
