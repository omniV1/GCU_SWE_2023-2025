# Windows Forms Application - Detailed Summary of Concepts

## Overview

This guide provides a detailed summary of the key concepts used in the Windows Forms application that processes user input to display either vowels or consonants along with their positions. It leverages C# and LINQ to perform string processing and display results.

## Topics Covered

### 1. User Interface Components
- **TextBox (`txtSentence`)**: Allows user input.
- **RadioButtons (`rbDisplayVowel`, `rbDisplayCon`)**: Enable the user to select whether to display vowels or consonants.
- **Button (`btnResult`)**: Triggers the processing of the input based on the selected option.
- **Label (`lblResults`)**: Displays the output of the processing.

### 2. Event Handling
- **Button Click Event**: 
  - Triggers the logic to process user input and display results.
  - `btnResult.Click += BtnResult_Click;`

### 3. Input Validation
- Checks if the input is empty or contains only whitespace.
- Ensures that the user has selected one of the radio button options.
- Example:
    ```
    if (string.IsNullOrWhiteSpace(input))
    {
        lblResults.Text = "Please enter a valid sentence.";
        return;
    }

    if (!rbDisplayVowel.Checked && !rbDisplayCon.Checked)
    {
        lblResults.Text = "Please select an option to display vowels or consonants.";
        return;
    }
    ```

### 4. String Processing with LINQ
- **Character Filtering**: Uses LINQ to filter characters based on the user's selection.
- **Formatting**: Formats each character and its position for output.
- Example:
    ```
    var vowels = input
        .Select((c, i) => (Character: c, Index: i))
        .Where(x => "aeiouAEIOU".Contains(x.Character))
        .Select(x => $"{x.Character} at position {x.Index}".PadRight(20))
        .ToList();
    ```

### 5. Displaying Results
- Uses `StringBuilder` to construct the output string efficiently.
- Output is formatted to display each character with its position.
- Example:
    ```
    StringBuilder output = new StringBuilder();
    output.AppendLine("Vowels and their positions:");
    vowels.ForEach(v => output.AppendLine(v));
    lblResults.Text = output.ToString();
    ```
### Forms Design
![Vowels](https://github.com/omniV1/SummerPractice/blob/main/C%23/Week1/notes/vowels.png)

![Cons](https://github.com/omniV1/SummerPractice/blob/main/C%23/Week1/notes/cons.png)
## Definitions Table

| Term           | Definition                                                               |
|----------------|--------------------------------------------------------------------------|
| **TextBox**    | A control for user input.                                                |
| **RadioButton**| Allows users to select between predefined options.                       |
| **Button**     | A control that triggers actions when clicked.                            |
| **Label**      | Displays text or results on the form.                                    |
| **LINQ**       | Language Integrated Query, used for filtering and manipulating data.     |
| **StringBuilder**| A mutable string class that allows efficient string manipulation.   |

