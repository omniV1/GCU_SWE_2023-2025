using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using Milestone.Models;

namespace Milestone.Filters
{
    public class AdminOnlyAttribute : SessionCheckFilter
    {
        public override void OnActionExecuting(ActionExecutingContext context)
        {
            // First, call the base SessionCheckFilter
            base.OnActionExecuting(context);

            // If the result is already set (e.g., redirected to login), return
            if (context.Result != null)
            {
                return;
            }

            // Now check if the user is an admin
            var userJson = context.HttpContext.Session.GetString("User");
            if (!string.IsNullOrEmpty(userJson))
            {
                var userData = ServiceStack.Text.JsonSerializer.DeserializeFromString<UserModel>(userJson);
                if (userData.Group != "Admin")
                {
                    context.Result = new ForbidResult();
                }
            }
            else
            {
                // This shouldn't happen due to SessionCheckFilter, but just in case
                context.Result = new RedirectToActionResult("Index", "Login", null);
            }
        }
    }
}