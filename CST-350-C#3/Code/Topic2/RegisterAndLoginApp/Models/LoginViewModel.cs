using System.ComponentModel.DataAnnotations;

namespace RegisterAndLoginApp.Models
{
    public class LoginViewModel
    {
        [Required]
        public required string Username { get; set; }

        [Required] 
        public required string Password { get; set; }
    }
}
