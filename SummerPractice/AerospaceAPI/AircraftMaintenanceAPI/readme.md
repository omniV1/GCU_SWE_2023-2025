# Aircraft Maintenance API

This project is a RESTful API for managing aircraft maintenance records.

## Major Checkpoints

### Project Setup
- [x] **Initialized Project Structure**: Set up the basic directory structure and initialized a new ASP.NET Core project.
- [x] **Added Essential Packages**: Installed necessary packages including EntityFrameworkCore, MySqlConnector, and ASP.NET Core tools.

### Database Integration
- [x] **Database Configuration**: Configured MySQL database connection in `appsettings.json`.
- [x] **Entity Framework Integration**: Set up Entity Framework Core with MySQL and created `AircraftMaintenanceContext` for database operations.
- [x] **Database Migrations**: Generated initial database migrations and applied them to create the database schema.

### CRUD Operations Implementation
- [x] **Created Models**: Defined models for `Aircraft`, `MaintenanceRecord`, `PerformanceMetric`, and `User`.
- [x] **Created DbContext**: Set up `AircraftMaintenanceContext` to manage the database context.
- [x] **Implemented Controllers**: Developed `AircraftsController` with CRUD operations (GET, POST, PUT, DELETE).

### Middleware and Error Handling
- [x] **Custom Middleware**: Implemented `ErrorHandlingMiddleware` to handle and log exceptions.
- [x] **Status Code Pages**: Configured status code pages to return JSON responses for API errors.

### Unit and Integration Testing
- [x] **Unit Tests**: Wrote unit tests for service methods.
- [x] **Integration Tests**: Created integration tests using Postman for API endpoints, including tests for response status, content type, and schema validation.

### Documentation
- [x] **API Documentation**: Documented API endpoints and example requests/responses in Postman.
- [x] **README Update**: Detailed documentation of the project setup, API endpoints, and progress in README.md.

### Continuous Integration/Continuous Deployment
- [ ] **CI/CD Pipeline**: Set up GitHub Actions for automated builds and tests (work in progress).

### Frontend Development
- [x] **React Frontend Setup**: Initialized a new React project using Create React App.
- [x] **Project Structure**: Organized the React project with separate directories for components and services.
- [x] **Implemented Components**: Developed components for listing, adding, editing, and deleting aircrafts.
- [x] **API Integration**: Integrated React components with the backend API using Axios.
- [x] **Styling**: Added CSS for consistent styling across components.

## Prerequisites

- .NET 8 SDK
- MySQL server
- Visual Studio or Visual Studio Code
- Postman (for testing API endpoints)

## Setup

### Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/yourusername/AircraftMaintenanceAPI.git
cd AircraftMaintenanceAPI

### Setup the Database

Make sure you have MySQL installed and running. Then, create a new database for the project:

CREATE DATABASE AircraftMaintenanceDB;

### Configure Connection String

Update the connection string in `appsettings.json` to match your MySQL configuration:

{
  "ConnectionStrings": {
    "DefaultConnection": "server=localhost;port=3306;database=AircraftMaintenanceDB;user=root;password=Bannana"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}

### Restore Dependencies

Restore the project's dependencies using the .NET CLI:

dotnet restore

### Apply Database Migrations

To ensure your database schema is up to date, apply the migrations:

dotnet ef database update

### Run the Application

Run the application using the .NET CLI:

dotnet run

The application should now be running on `http://localhost:5240`.

### Setup React Frontend

Navigate to the `aircraft-maintenance-frontend` directory:

cd aircraft-maintenance-frontend

Install the necessary dependencies:

npm install

Start the React development server:

npm start

The frontend application should now be running on `http://localhost:3000`.

## API Documentation

### SEE ![API POSTMAN DOCUMENTATION](https://documenter.getpostman.com/view/32764813/2sA3e1Apqr)

### Endpoints

- **GET** `/api/aircrafts` - Retrieve all aircrafts
- **GET** `/api/aircrafts/{id}` - Retrieve an aircraft by ID
- **POST** `/api/aircrafts` - Create a new aircraft
- **PUT** `/api/aircrafts/{id}` - Update an aircraft
- **DELETE** `/api/aircrafts/{id}` - Delete an aircraft

### Example Requests

#### GET `/api/aircrafts`

[
  {
    "id": 1,
    "model": "Boeing 747",
    "serialNumber": "SN747",
    "lastMaintenanceDate": "2023-07-06T08:00:00"
  },
  {
    "id": 2,
    "model": "Airbus A320",
    "serialNumber": "SNA320",
    "lastMaintenanceDate": "2023-07-06T08:00:00"
  }
]

#### POST `/api/aircrafts`

Request Body:

{
  "model": "Cessna 172",
  "serialNumber": "SN172",
  "lastMaintenanceDate": "2024-07-06T08:00:00"
}

#### PUT `/api/aircrafts/{id}`

Request Body:

{
  "id": 1,
  "model": "Updated Model",
  "serialNumber": "UpdatedSerial123",
  "lastMaintenanceDate": "2024-07-06T08:00:00"
}

#### DELETE `/api/aircrafts/{id}`

Response:

{
  "message": "Aircraft deleted successfully."
}

### Running Tests

To run the Postman tests, import the Postman collection from the `tests` directory and execute the requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Future TODOS

- [ ] **CI/CD Pipeline**: Set up GitHub Actions for automated builds and tests.
- [ ] **User Authentication and Authorization**: Implement user registration, login, and role management.
- [ ] **Search and Filter Functionality**: Add search and filter options for aircrafts.
- [ ] **Additional Features**: Implement additional features such as notifications and reporting.
- [ ] **Performance Optimization**: Optimize API performance and database queries.
- [ ] **Documentation**: Enhance documentation with detailed usage examples and setup guides.
- [ ] **Unit Tests**: Expand unit tests to cover more edge cases and scenarios.
- [ ] **Integration Tests**: Enhance integration tests for comprehensive API validation.
