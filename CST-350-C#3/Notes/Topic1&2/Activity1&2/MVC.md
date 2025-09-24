# ASP.NET Core MVC Study Guide: Login and Registration System

## Table of Contents
1. [Introduction to ASP.NET Core MVC](#introduction-to-aspnet-core-mvc)
2. [N-Layer Architecture](#n-layer-architecture)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Creating an ASP.NET Core MVC Project](#creating-an-aspnet-core-mvc-project)
5. [User Authentication and Authorization](#user-authentication-and-authorization)
6. [Password Security](#password-security)
7. [Session Management](#session-management)
8. [Razor Views and Domain Models](#razor-views-and-domain-models)
9. [Form Validation](#form-validation)
10. [Database Integration with Entity Framework Core](#database-integration-with-entity-framework-core)
11. [Security Best Practices](#security-best-practices)
12. [User Management](#user-management)
13. [Testing](#testing)
14. [Conclusion and Next Steps](#conclusion-and-next-steps)

## 1. Introduction to ASP.NET Core MVC

ASP.NET Core MVC is a web application framework developed by Microsoft that implements the Model-View-Controller (MVC) architectural pattern.

- **Model**: Represents the data and business logic of the application.
- **View**: Handles the presentation layer (UI).
- **Controller**: Manages user requests, works with the Model, and selects Views to render.

Key features:
- Cross-platform
- High-performance
- Dependency injection
- Highly testable

## 2. N-Layer Architecture

N-Layer Architecture is a software design pattern that separates an application into logical layers.

Typical layers:
1. **Presentation Layer**: User interface and controllers
2. **Business Logic Layer**: Application's business logic
3. **Data Access Layer**: Interacts with the database
4. **Data Storage**: The actual database

Benefits:
- Separation of concerns
- Improved maintainability
- Enhanced scalability

## 3. Setting Up the Development Environment

To get started with ASP.NET Core MVC development:

1. Install Visual Studio (latest version recommended)
2. During installation, select the "ASP.NET and web development" workload
3. Install .NET Core SDK (latest LTS version)

Verify installation:
```bash
dotnet --version
```

## 4. Creating an ASP.NET Core MVC Project

Steps to create a new project:
1. Open Visual Studio
2. Click "Create a new project"
3. Select "ASP.NET Core Web Application"
4. Choose a project name and location
5. Select ".NET Core" and "ASP.NET Core 5.0" (or latest version)
6. Choose "Web Application (Model-View-Controller)"

Explore the project structure:
- `Controllers/`: Contains controller classes
- `Models/`: For model classes
- `Views/`: Razor view files
- `wwwroot/`: Static files (CSS, JS, images)
- `Startup.cs`: Application configuration
- `Program.cs`: Entry point of the application

## 5. User Authentication and Authorization

Authentication verifies user identity, while authorization determines access rights.

Implementing basic authentication:

1. Create a `User` model:

```csharp
public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string PasswordHash { get; set; }
    public string Email { get; set; }
}
```

2. Create an `AccountController`:

```csharp
public class AccountController : Controller
{
    private readonly UserManager<User> _userManager;
    private readonly SignInManager<User> _signInManager;

    public AccountController(UserManager<User> userManager, SignInManager<User> signInManager)
    {
        _userManager = userManager;
        _signInManager = signInManager;
    }

    // Registration and Login actions will be implemented here
}
```

3. Implement registration and login actions in the controller.

## 6. Password Security

Never store passwords in plain text. Use hashing and salting.

1. Password hashing:
   - Use `BCrypt` or ASP.NET Core Identity's built-in methods

2. Salting:
   - Add a unique salt to each password before hashing

Example using ASP.NET Core Identity:

```csharp
var user = new User { UserName = model.Email, Email = model.Email };
var result = await _userManager.CreateAsync(user, model.Password);
```

## 7. Session Management

Sessions help maintain user state across requests.

1. Configure session in `Startup.cs`:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddDistributedMemoryCache();
    services.AddSession(options =>
    {
        options.IdleTimeout = TimeSpan.FromMinutes(30);
        options.Cookie.HttpOnly = true;
        options.Cookie.IsEssential = true;
    });
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    app.UseSession();
    // Other middleware
}
```

2. Using session in controllers:

```csharp
HttpContext.Session.SetString("UserID", user.Id.ToString());
var userId = HttpContext.Session.GetString("UserID");
```

## 8. Razor Views and Domain Models

Razor is a view engine that allows embedding C# code in HTML.

1. Create a view model:

```csharp
public class LoginViewModel
{
    [Required]
    [EmailAddress]
    public string Email { get; set; }

    [Required]
    [DataType(DataType.Password)]
    public string Password { get; set; }

    [Display(Name = "Remember me?")]
    public bool RememberMe { get; set; }
}
```

2. Create a Razor view (`Login.cshtml`):

```html
@model LoginViewModel

<h2>Login</h2>

<form asp-action="Login" method="post">
    <div asp-validation-summary="ModelOnly" class="text-danger"></div>
    <div class="form-group">
        <label asp-for="Email"></label>
        <input asp-for="Email" class="form-control" />
        <span asp-validation-for="Email" class="text-danger"></span>
    </div>
    <div class="form-group">
        <label asp-for="Password"></label>
        <input asp-for="Password" class="form-control" />
        <span asp-validation-for="Password" class="text-danger"></span>
    </div>
    <div class="form-group">
        <div class="checkbox">
            <label asp-for="RememberMe">
                <input asp-for="RememberMe" />
                @Html.DisplayNameFor(m => m.RememberMe)
            </label>
        </div>
    </div>
    <button type="submit" class="btn btn-primary">Log in</button>
</form>
```

## 9. Form Validation

Implement both server-side and client-side validation.

1. Server-side validation using data annotations:

```csharp
public class RegisterViewModel
{
    [Required]
    [EmailAddress]
    [Display(Name = "Email")]
    public string Email { get; set; }

    [Required]
    [StringLength(100, ErrorMessage = "The {0} must be at least {2} characters long.", MinimumLength = 6)]
    [DataType(DataType.Password)]
    [Display(Name = "Password")]
    public string Password { get; set; }

    [DataType(DataType.Password)]
    [Display(Name = "Confirm password")]
    [Compare("Password", ErrorMessage = "The password and confirmation password do not match.")]
    public string ConfirmPassword { get; set; }
}
```

2. Client-side validation:
   - Include jQuery Validation scripts in your layout file
   - Use `asp-validation-for` tag helpers in your views

## 10. Database Integration with Entity Framework Core

1. Install required NuGet packages:
   - `Microsoft.EntityFrameworkCore.SqlServer`
   - `Microsoft.EntityFrameworkCore.Tools`

2. Create a DbContext:

```csharp
public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public DbSet<User> Users { get; set; }
}
```

3. Configure the database in `Startup.cs`:

```csharp
services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));
```

4. Create and apply migrations:

```bash
dotnet ef migrations add InitialCreate
dotnet ef database update
```

## 11. Security Best Practices

1. Use HTTPS
2. Implement CSRF protection:
   - Add `[ValidateAntiForgeryToken]` attribute to POST actions
   - Use `@Html.AntiForgeryToken()` in forms
3. Secure cookies
4. Implement proper error handling and logging
5. Use parameterized queries to prevent SQL injection

## 12. User Management

Implement features like:
- User profile editing
- Password reset functionality
- Account lockout after failed login attempts

Example of a logout action:

```csharp
public async Task<IActionResult> Logout()
{
    await _signInManager.SignOutAsync();
    return RedirectToAction("Index", "Home");
}
```

## 13. Testing

1. Unit Testing:
   - Test individual components in isolation
   - Use xUnit or NUnit framework

2. Integration Testing:
   - Test multiple components together
   - Use `Microsoft.AspNetCore.Mvc.Testing` package for integration tests

Example of a simple unit test:

```csharp
[Fact]
public async Task Login_WithValidCredentials_ReturnsSuccess()
{
    // Arrange
    var controller = new AccountController(/* dependencies */);
    var model = new LoginViewModel { Email = "test@example.com", Password = "password" };

    // Act
    var result = await controller.Login(model) as RedirectToActionResult;

    // Assert
    Assert.NotNull(result);
    Assert.Equal("Index", result.ActionName);
    Assert.Equal("Home", result.ControllerName);
}
```

