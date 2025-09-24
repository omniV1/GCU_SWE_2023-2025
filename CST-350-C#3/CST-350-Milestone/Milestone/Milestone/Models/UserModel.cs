using System;
using System.Security.Cryptography;
using System.Linq;
using System;
using System.Data.SqlClient;
using Dapper; // You need to install Dapper NuGet package
using Microsoft.Extensions.Configuration;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Linq;


namespace Milestone.Models

{
    public class UserModel
    {
        public int Id { get; set; }
        public string Username { get; set; }
        public string PasswordHash { get; set; }
        public byte[] Salt { get; set; }
        public string Group { get; set; }
        


        // Size of the salt in bytes
        private const int SaltSize = 16;

        // Size of the hash in bytes
        private const int HashSize = 32;

        // Number of iterations for the hashing algorithm
        private const int Iterations = 10000;

        // Owen Lindsey
        // Method to set a new password for the user
        public void SetPassword(string password)
        {
            this.Salt = GenerateSalt();
            this.PasswordHash = HashPassword(password, this.Salt);
        }

        // Owen Lindsey
        // Method to verify if a given password matches the stored hash
        public bool VerifyPassword(string password)
        {
            string hashedPassword = HashPassword(password, this.Salt);
            return this.PasswordHash == hashedPassword;
        }

        // Method to generate a random salt
        private byte[] GenerateSalt()
        {
            return RandomNumberGenerator.GetBytes(SaltSize);
        }


        // Method to hash a password with a given salt
        private string HashPassword(string password, byte[] salt)
        {
            // Convert password to byte array
            byte[] passwordBytes = System.Text.Encoding.UTF8.GetBytes(password);

            // Use PBKDF2 to derive a key (hash) from the password and salt
            byte[] hashBytes = Rfc2898DeriveBytes.Pbkdf2(
                passwordBytes,
                salt,
                Iterations,
                HashAlgorithmName.SHA256,
                HashSize);

            // Convert the hash to a Base64 string for storage
            return Convert.ToBase64String(hashBytes);
        }
    }
}