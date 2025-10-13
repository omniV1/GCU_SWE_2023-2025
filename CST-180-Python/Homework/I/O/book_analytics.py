# Owen Lindsey
# CST-180
# 10/13/2025
# book_analytics.py

"""
Book Analytics Program
This program reads a CSV file containing book information, performs statistical analysis on the data, and outputs the results to both a file and the terminal display.
"""

# DEFINE input_file as "books.csv"
# Set the name of the input CSV file containing book data
input_file = "books.csv"
# DEFINE output_file as "book_analysis.txt"
# Set the name of the output file where results will be saved
output_file = "book_analysis.txt"
# DEFINE total_years as 0
# Initialize accumulator for sum of all publication years
total_years = 0
# DEFINE total_pages as 0
# Initialize accumulator for sum of all page counts
total_pages = 0
# DEFINE book_count as 0
# Initialize counter for total number of books processed
book_count = 0
# DEFINE max_pages as 0
# Initialize variable to track the highest page count found
max_pages = 0
# DEFINE max_pages_title as ""
# Initialize variable to store title of book with most pages
max_pages_title = ""
# DEFINE max_pages_author as ""
# Initialize variable to store author of book with most pages
max_pages_author = ""
# DEFINE max_pages_year as 0
# Initialize variable to store year of book with most pages
max_pages_year = 0
# DEFINE min_pages as float('inf')
# Initialize variable to track the lowest page count found (start with infinity)
min_pages = float('inf')
# DEFINE min_pages_title as ""
# Initialize variable to store title of book with fewest pages
min_pages_title = ""
# DEFINE min_pages_author as ""
# Initialize variable to store author of book with fewest pages
min_pages_author = ""
# DEFINE min_pages_year as 0
# Initialize variable to store year of book with fewest pages
min_pages_year = 0
# DEFINE average_year as 0.0
# Initialize variable to store calculated average publication year
average_year = 0.0
# DEFINE average_pages as 0.0
# Initialize variable to store calculated average page count
average_pages = 0.0


# TRY TO OPEN input_file
# Attempt to open the CSV file for reading
# IF file cannot be opened, PRINT error message and exit
# IF file opens successfully, READ file line by line
try:
    with open(input_file, 'r') as file:
        # DEFINE line_number as 0
        # Initialize counter to track current line number for error reporting
        line_number = 0
        # FOR each line IN file:
        # Process each line of the CSV file
        for line in file:
            # COMPUTE line_number as line_number + 1
            # Increment line counter for error tracking
            line_number += 1
            # DEFINE fields as line.strip().split(',')
            # Split the line by comma delimiter and remove whitespace
            fields = line.strip().split(',')
            # IF len(fields) EQUALS 4:
            # Check if line has exactly 4 fields (title, author, year, pages)
            if len(fields) == 4:
                try:
                    # DEFINE title, author, year_str, pages_str as fields
                    # Extract the four fields from the line
                    title, author, year_str, pages_str = fields
                    # DEFINE year as int(year_str)
                    # Convert year string to integer
                    year = int(year_str)
                    # DEFINE pages as int(pages_str)
                    # Convert pages string to integer
                    pages = int(pages_str)
                    # COMPUTE total_years as total_years + year
                    # Add current book's year to the running total
                    total_years += year
                    # COMPUTE total_pages as total_pages + pages
                    # Add current book's pages to the running total
                    total_pages += pages
                    # COMPUTE book_count as book_count + 1
                    # Increment the total book counter
                    book_count += 1

                    # IF pages GREATER THAN max_pages:
                    # Check if current book has more pages than previous maximum
                    if pages > max_pages:
                        # DEFINE max_pages as pages
                        # Update the maximum page count
                        max_pages = pages
                        # DEFINE max_pages_title as title
                        # Store title of book with most pages
                        max_pages_title = title
                        # DEFINE max_pages_author as author
                        # Store author of book with most pages
                        max_pages_author = author
                        # DEFINE max_pages_year as year
                        # Store year of book with most pages
                        max_pages_year = year
                        
                    # IF pages LESS THAN min_pages:
                    # Check if current book has fewer pages than previous minimum
                    if pages < min_pages:
                        # DEFINE min_pages as pages
                        # Update the minimum page count
                        min_pages = pages
                        # DEFINE min_pages_title as title
                        # Store title of book with fewest pages
                        min_pages_title = title
                        # DEFINE min_pages_author as author
                        # Store author of book with fewest pages
                        min_pages_author = author
                        # DEFINE min_pages_year as year
                        # Store year of book with fewest pages
                        min_pages_year = year
                except ValueError as ve:
                    # PRINT warning message for invalid data format
                    print(f"Warning: Skipping line {line_number} - Invalid data format: {ve}")
                    print(f"  Line content: {line.strip()}")
            else:
                # PRINT warning message for incorrect number of fields
                print(f"Warning: Skipping line {line_number} - Expected 4 fields, found {len(fields)}")
                print(f"  Line content: {line.strip()}")

    # IF book_count EQUALS 0:
    # Check if any valid books were processed
    if book_count == 0:
        # PRINT warning message
        print("Warning: No valid books found in file")
        # OPEN output_file for writing
        with open(output_file, 'w') as file:
            # WRITE report header to file
            file.write("Book Analytics Report\n")
            file.write("=" * 50 + "\n")
            # WRITE warning message to file
            file.write("Warning: No valid books found in file\n")
        # PRINT message about no results
        print(f"No results to save. Check file {output_file} for details.")
    # ELSE:
    # If valid books were found, calculate and display results
    else:
        # COMPUTE average_year as total_years / book_count
        # Calculate the average publication year
        average_year = total_years / book_count
        # COMPUTE average_pages as total_pages / book_count
        # Calculate the average number of pages
        average_pages = total_pages / book_count

        # OPEN output_file for writing
        # Write results to output file with proper formatting
        with open(output_file, 'w') as file:
            # WRITE report header to file
            file.write("Book Analytics Report\n")
            file.write("=" * 50 + "\n")
            # WRITE average year to file
            file.write(f"Average Publication Year: {average_year:.1f}\n")
            # WRITE average pages to file
            file.write(f"Average Number of Pages: {average_pages:.1f}\n")
            # WRITE book with most pages to file
            file.write(f"Book with Most Pages: {max_pages_title}, {max_pages_author}, {max_pages_year}, {max_pages}\n")
            # WRITE book with fewest pages to file
            file.write(f"Book with Fewest Pages: {min_pages_title}, {min_pages_author}, {min_pages_year}, {min_pages}\n")

        # PRINT report header to terminal
        # Display results to terminal
        print("Book Analytics Report")
        print("=" * 50)
        # PRINT average year to terminal
        print(f"Average Publication Year: {average_year:.1f}")
        # PRINT average pages to terminal
        print(f"Average Number of Pages: {average_pages:.1f}")
        # PRINT book with most pages to terminal
        print(f"Book with Most Pages: {max_pages_title}, {max_pages_author}, {max_pages_year}, {max_pages}")
        # PRINT book with fewest pages to terminal
        print(f"Book with Fewest Pages: {min_pages_title}, {min_pages_author}, {min_pages_year}, {min_pages}")

        # PRINT success message
        print(f"\nResults have been saved to {output_file}")
# EXCEPT FileNotFoundError:
# Handle case where input file does not exist
except FileNotFoundError:
    # PRINT file not found error message
    print(f"Error: Input file '{input_file}' not found.")
    print("Please make sure the file exists in the current directory.")
# EXCEPT PermissionError:
# Handle case where file access is denied
except PermissionError:
    # PRINT permission denied error message
    print(f"Error: Permission denied when trying to access '{input_file}' or write to '{output_file}'.")
    print("Please check file permissions.")
# EXCEPT any other Exception:
# Handle any other unexpected errors
except Exception as e:
    # PRINT generic error message
    print(f"Unexpected error: {e}")
    print("Please check the file format and try again.")    
