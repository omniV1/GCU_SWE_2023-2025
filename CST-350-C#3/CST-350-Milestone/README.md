# CST-350-Milestone

# CST-350 Milestone Project

This repository contains the code for the Milestone project in the CST-350 course. The project involves building a web application with registration, login, and restricted access functionality.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Registration](#registration)
  - [Login](#login)
  - [Restricted Access](#restricted-access)
- [Project Structure](#project-structure)
## Introduction

The Milestone project is a web application that allows users to register, log in, and access restricted content. The application is built using ASP.NET Core, a popular framework for building modern web applications.

## Features

The application includes the following key features:

1. **Registration**: Users can register by providing a username, password, and selecting their group (e.g., Admin, Users, Students).
2. **Login**: Registered users can log in to the application using their username and password.
3. **Restricted Access**: Authenticated users can access the "StartGame" feature, while unauthenticated users are redirected to the login page.

## Technologies Used

The Milestone project was built using the following technologies:

- **ASP.NET Core**: A free, open-source, and cross-platform web framework for building modern web applications.
- **SQL Server**: A relational database management system used to store user information.
- **Entity Framework Core**: An Object-Relational Mapping (ORM) framework used for data access and management.
- **Bootstrap**: A popular CSS framework used for responsive and mobile-first web development.

## Getting Started

### Prerequisites

To run the Milestone project locally, you'll need to have the following installed on your machine:

- [.NET Core SDK](https://dotnet.microsoft.com/download)
- [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

### Installation

1. Clone the repository to your local machine:
git clone https://github.com/your-username/cst-350-milestone.git

2. Open the solution in your preferred IDE (e.g., Visual Studio, Visual Studio Code).

3. Update the database connection string in the `appsettings.json` file to match your local SQL Server configuration.

4. Build and run the application:

- In Visual Studio, click the "Start" button or press `F5`.
- In Visual Studio Code, open a terminal, navigate to the project directory, and run `dotnet run`.

5. The application should now be running at `https://localhost:7218/`.

## Usage

### Registration

1. Navigate to the registration page by clicking the "Register" link in the navigation menu.
2. Fill out the registration form with a username, password, and select the appropriate group.
3. Click the "Register" button to create a new user account.

### Login

1. Navigate to the login page by clicking the "Login" link in the navigation menu.
2. Enter your registered username and password.
3. Click the "Login" button to access the application.

### Restricted Access

1. After logging in, you should see a "Start Game" link in the navigation menu.
2. Click the "Start Game" link to access the restricted content.
3. If you're not logged in, you won't see the "Start Game" link, and attempting to access the restricted content will redirect you to the login page.

## Project Structure

The Milestone project is structured as follows:
| Directory | File | Description |
| --- | --- | --- |
| `Controllers` | `HomeController.cs` | Handles the actions and logic for the home page and error handling. |
| `Controllers` | `LoginController.cs` | Handles the actions and logic for user authentication (login, logout, registration). |
| `Controllers` | `UserController.cs` | Handles the actions and logic for managing user-related functionality (e.g., viewing user details, updating user information). |
| `Filters` | `AdminOnlyAttribute.cs` | Custom action filter that restricts access to administrative-only functionality. |
| `Filters` | `SessionCheckFilter.cs` | Custom action filter that checks if the user is authenticated before allowing access to certain actions. |
| `Models` | `GroupViewModel.cs` | Represents a user group and its selection status. |
| `Models` | `LoginViewModel.cs` | Defines the model for the login form. |
| `Models` | `RegisterViewModel.cs` | Defines the model for the registration form. |
| `Models` | `UserModel.cs` | Represents a user and their associated data (e.g., username, password hash, group). |
| `Models` | `ErrorViewModel.cs` | Defines the model for the error view. |
| `Services/DAO` | `UserDAO.cs` | Handles the data access operations for user-related functionality (e.g., CRUD operations on the user table). |
| `Services/Business` | `UserCollection.cs` | Encapsulates the business logic for user-related operations (e.g., registration, login, user management). |
| `Views/Home` | `Index.cshtml`, `Privacy.cshtml`, `StartGame.cshtml` | Views related to the home page and error handling. |
| `Views/Login` | `AddUser.cshtml`, `Index.cshtml`, `LoginFailure.cshtml`, `LoginSuccess.cshtml`, `Register.cshtml` | Views related to user authentication (login, registration, logout). |
| `Views/User` | `AllUsers.cshtml`, `Delete.cshtml`, `Edit.cshtml`, `Index.cshtml` | Views related to user management functionality. |
| N/A | `Startup.cs` | Configures the application services and middleware. |
| N/A | `Program.cs` | The application's entry point. |
| N/A | `appsettings.json` | Application configuration settings. |
| N/A | `_Layout.cshtml` | The main layout file that defines the application's structure. |
| N/A | `_ValidationScriptsPartial.cshtml` | Partial view that includes client-side validation scripts. |
