using System;
using System.IO;

namespace FileIOApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // File path for the input data.
            string filePath = @"C:\Users\Owenl\source\repos\250\Activities\TextFileDataAccessDemo\test.txt";

            // Initialize a new list of people.
            List<Person> people = new List<Person>();
            
            // Read all lines from the file into a list.
            List<String> lines = File.ReadAllLines(filePath).ToList();

            // Process each line and create a Person object if the line is valid.
            foreach (string line in lines)
            {
                string[] entries = line.Split(',');
                if (entries.Length == 3)
                {
                    // Create and add the Person object to the list of people.
                   people.Add(new Person()
                    {
                        FirstName = entries[0],
                        LastName = entries[1],
                        Url = entries[2]
                    });
                }
                else
                {
                    // Display a warning if a line does not have 3 items.
                    Console.WriteLine($"Warning: The following line does not have 3 items: {line}");
                }
            }

            // Output lines to be written to the file.
            List<string> outputLines = new List<string>();
            
            Console.WriteLine("Here is the list of people I have:");
            foreach (Person p in people)
            {
                string outputLine = $"First Name: {p.FirstName}, Last Name: {p.LastName}, URL: {p.Url}";
               
                // Print to the console and add to the output lines.
                Console.WriteLine(outputLine);
                outputLines.Add(outputLine);
            }

            // File path for the output data.
            string outPath = @"C:\Users\Owenl\source\repos\250\Activities\TextFileDataAccessDemo\peopleOut.txt";
            
            // Write all output lines to the file.
            File.WriteAllLines(outPath, outputLines);




            /////////////////   Commenting earlier code from activity //////////////////////////////


            /* List<string> lines = File.ReadAllLines(filePath).ToList();

            lines.Add("Steve, Jobs, www.apple.com");

            foreach (string line in lines)
            {
                Console.WriteLine(line);
            }

            File.WriteAllLines(filePath, lines); */

            ///////////////////////////                          ////////////////////////////////// 


            Console.ReadLine(); 
        }
        
    }
}


