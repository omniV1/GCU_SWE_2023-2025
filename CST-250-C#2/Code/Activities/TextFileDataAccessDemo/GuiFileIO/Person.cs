using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;

namespace TextFileDataAccessDemo
{
    public class Person
    {
        public string? FirstName { get; set; }
        public string? LastName { get; set; }
        public string? Url { get; set; }

        public override string ToString()
        {
            // This will format the person's data as "First Name: <FirstName>, Last Name: <LastName>, URL: <Url>"
            return $"First Name: {FirstName}, Last Name: {LastName}, URL: {Url}";
        }
    }

}

