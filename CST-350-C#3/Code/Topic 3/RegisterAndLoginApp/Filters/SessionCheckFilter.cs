using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace RegisterAndLoginApp.Filters
{
    /// <summary>
    /// Define a class named SessionChcekFilter that inhereits from ActionFilterAttribute
    /// </summary>
    public class SessionCheckFilter : ActionFilterAttribute
    {
        // This code defines an action filter so that our filter (SessionCHeckFilter) that
        // checks whether a user is logged in by verifying the 
        // "User" session variable
        // Override the "OnActionExecuting" method which executes 
        // before an action methods is called

        public override void OnActionExecuting(ActionExecutingContext context)
        {
            // check if there is session variable named "User" and if 
            // it is null (not set or expired).
            if (context.HttpContext.Session.GetString("User") == null)
            {
                // if session variable User is null redirect the user 
                // to the "User/Index" page.
                context.Result = new RedirectResult("/Login/Index");
            }
        } // end of override
    }
}
