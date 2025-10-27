**Video Essay Script (First-Person, ~5 minutes, Kdenlive-ready)**

[fade in voice-over]  
Hi, I’m Owen Lindsey, and in this video I’ll be walking through my Book Analytics Program for CST-180. This Python script, `book_analytics.py`, reads book data from a CSV file, performs statistical analysis, and outputs results to both the console and a report file. I’ll go step by step through how the code works, explaining the logic, the control flow, and how errors are handled.

## Scene 1: Introduction and Setup

[cut to title card: “Book Analytics Program”]

I start by defining two key file names — `input_file` as `"books.csv"` and `output_file` as `"book_analysis.txt"`. These act as the input source and destination for all results.

Next, I initialize variables that track totals, counts, and min/max statistics. `total_years` and `total_pages` accumulate data, while `max_pages` starts at `0` so that the first legitimate book immediately becomes the new maximum. For the opposite extreme I set `min_pages` to `float('inf')`, which is Python’s way of representing positive infinity. That sentinel value guarantees the first book encountered replaces it, letting the subsequent logic focus on simple comparisons.

To keep the code readable, I leverage a DEFINE comment structure that explains each line in plain English — almost like pseudocode that parallels the Python syntax. This makes it easy for anyone reading the program to understand not just what it does, but why each variable exists before it’s used.

## Scene 2: Reading and Processing the CSV File

[cut to code block showing `try:` section]

After setup, I wrap the main logic inside a `try` block. This ensures that any issues with file access or format are caught cleanly.

Inside the `try`, the program opens the input CSV file in read mode using a `with open` statement. This automatically handles closing the file when finished.

Each line of the file represents one book entry. I use a loop to go through every line, incrementing a `line_number` counter for easier debugging. Then, I split the line into fields using `line.strip().split(',')`, which separates the title, author, year, and page count.

To verify data integrity, I check if there are exactly four fields. If not, a warning is printed — this prevents malformed data from breaking the analysis later.

## Scene 3: Type Conversion and Accumulation

[cut to highlighted section showing `int(year_str)` and `int(pages_str)`]

For valid lines, I unpack the four fields into `title`, `author`, `year_str`, and `pages_str`, converting the numeric values to integers. Then I add those to running totals for pages and publication years, and increment `book_count`.

After that, the program compares each book’s page count against the current `max_pages` and `min_pages`. If a new extreme is found, it updates the associated title, author, and year variables. Thanks to the initial `0` and `float('inf')` seeds, the comparisons are straightforward and always latch onto the first real data encountered.

## Scene 4: Error Handling During Processing

[on screen: terminal output with a warning message example]

If the conversion to integer fails — for example, if a year or page value isn’t numeric — the code catches that inside a nested `try-except` block. I print a clear warning that includes the line number and the invalid content. This ensures the user can correct any data issues while allowing the rest of the program to continue analyzing the valid records.

## Scene 5: Calculating Results and Writing Output

[cut to section showing averages being calculated]

Once all lines have been processed, I check whether any valid books were counted. If `book_count` equals zero, the program writes a warning message to the output file and informs the user that no results were generated.

Otherwise, I calculate the averages by dividing the totals by `book_count`. `average_year` gives the mean publication year, and `average_pages` gives the mean page count.

Both results, along with the highest and lowest page counts, are written to `book_analysis.txt` in a formatted report style. At the same time, they’re printed to the terminal so the user can see immediate feedback.

## Scene 6: Exception Handling and Robustness

[cut to bottom of code showing global `except` blocks]

Outside of the main `try`, I include specific exception handlers. If the input file doesn’t exist, a `FileNotFoundError` prints a user-friendly message telling the reader to check the directory. A `PermissionError` handles cases where the program can’t access or write files due to system restrictions. Finally, a general exception catch ensures that any unexpected error still provides a descriptive message instead of crashing.

This layered approach demonstrates defensive programming — anticipating issues before they happen and making the program resilient.

## Scene 7: Closing Reflection

[cut to terminal output and fade to summary slide]

In summary, this script reads structured data, validates it, performs numeric analysis, and outputs clear results to both text and terminal. Every variable serves a purpose, every potential error is caught, and the output provides meaningful insights about the dataset.

The program demonstrates proper code organization, consistent naming conventions, clear indentation, and a focus on maintainability. I’m especially proud of how readable the comment structure makes it — you can follow the pseudocode line by line without needing to guess what each part does.

[fade out voice-over]  
That’s my walkthrough of the Book Analytics Program. Thanks for watching.
