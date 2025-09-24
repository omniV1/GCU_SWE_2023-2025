using System.Collections;

namespace LINQdemo
{
    class program
    {
        static void Main(string[] args)
        {
            // make some test scores
            var scores = new[] { 50, 66, 90, 81, 77, 45, 0, 100, 99, 72, 87, 85, 81, 80, 77, 74, 95, 97 };

            ////////////////// print the scores ///////////////////////////////////
            /*
            foreach (var individualScore in scores)
            {
                Console.WriteLine("One of the scores was {0}", individualScore); 
            }
            // pause to see the output before closing 
            Console.ReadLine();
            */
            /////////////////////////////////////////////////////////////////////


            ///////////////////// Use a LINQ statement to filter the list ////////////////////
            /*
            var theBestStudents = 
                from individualScore in scores
                where individualScore > 90 
                select individualScore;

            // print only the bestscores
            foreach (var individualScore in theBestStudents)
            {
                Console.WriteLine("One of the BEST scores was {0}", individualScore); 
            }
            //poause to see the output before closing 
            Console.ReadLine ();

            */
            //////////////////////////////////////////////////////////////////////////


            /////////////// use LINQ to sort the results ///////////////////////////////

            /*
             
            var sortedScores =
                from individualScore in scores
                orderby individualScore
                select individualScore;

            //print the sorted list
            foreach (var individualScore in sortedScores )
            {
                Console.WriteLine("One of the scores was {0}", individualScore);
            }

            Console.ReadLine ();
            */
            /////////////////////////////////////////////////////////////////////////////

            /////////////// LINQ query to filter B students (scores between 80 and 89) in ascending order /////////////////////////
            /*
            var bStudents =
                from individualScore in scores
                where individualScore >= 80 && individualScore <= 89
                orderby individualScore
                select individualScore;

            // Print the B students' scores
            Console.WriteLine("B students' scores in ascending order:");
            foreach (var score in bStudents)
            {
                Console.WriteLine(score);
            }
            Console.ReadLine(); // Pause to see the output before closing
            */

            // Create an ArrayList of Student objects
            ArrayList studentList = new ArrayList
            {
                 new Student("John Doe", 20, 85),
                 new Student("Jane Smith", 19, 92),
                 new Student("Emily Johnson", 22, 76),
                  
             };

            // Use LINQ to sort the student list by grade

            // We need to cast the objects in ArrayList to Student before applying LINQ
            var sortedStudents =
                from Student student in studentList.Cast<Student>()
                orderby student.Grade
                select student;

            // Print the sorted student list
            Console.WriteLine("Students sorted by grade:");

            foreach (var student in sortedStudents)
            {
                Console.WriteLine(student);
            }
            Console.ReadLine(); // Pause to see the output before closing

        }
    }
}