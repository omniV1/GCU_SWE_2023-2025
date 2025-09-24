using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LINQdemo
{
    // Student class with IComparable implementation
    public class Student : IComparable<Student>
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public int Grade { get; set; }

        // Constructor for convenience
        public Student(string name, int age, int grade)
        {
            Name = name;
            Age = age;
            Grade = grade;
        }

        // CompareTo method to sort students by Grade
        public int CompareTo(Student other)
        {
            // Assuming we're sorting students by Grade in ascending order
            return this.Grade.CompareTo(other.Grade);
        }

        // Override ToString method to make printing easier
        public override string ToString()
        {
            return $"Name: {Name}, Age: {Age}, Grade: {Grade}";
        }
    }

}
