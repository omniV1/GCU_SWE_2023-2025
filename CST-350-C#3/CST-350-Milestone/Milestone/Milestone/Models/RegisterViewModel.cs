namespace Milestone.Models
{
    // class GroupViewModel used to name the 
    // groups that the user can be part of 
    //Since these are associated they can be
    // in the same model
    public class GroupViewModel
    {
        public bool IsSelected { get; set; }
        public string GroupName { get; set; }
    }

    public class RegisterViewModel
    {
        // Properties for the entry screen
        public string Username { get; set; }
        public string Password { get; set; }
        public List<GroupViewModel> Groups { get; set; }

        /// <summary>
        /// Default constructor 
        /// </summary>
        public RegisterViewModel()
        {
            Username = "";
            Password = "";

            //Create the selections we want to have for checkboxes
            Groups = new List<GroupViewModel>
            {
                new GroupViewModel { GroupName = "Admin", IsSelected = false },
                new GroupViewModel { GroupName = "Users", IsSelected = false },
                new GroupViewModel { GroupName = "Students", IsSelected = false }
            };
        }
    }


}