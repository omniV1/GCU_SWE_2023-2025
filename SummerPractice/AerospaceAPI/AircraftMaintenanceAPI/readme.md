# Aircraft Maintenance API

This project combines an ASP.NET Core 8 REST API, Entity Framework Core with
MySQL, and a React 18 frontend for managing aircraft maintenance records.

## Major Checkpoints

### Project Setup
- [x] **Initialized Project Structure**: Set up the basic directory structure and initialized a new ASP.NET Core project.
- [x] **Added Essential Packages**: Uses Entity Framework Core and the Pomelo MySQL provider on .NET 8.

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

### API Testing
- [x] **Postman Documentation**: Documented requests for manual API exploration.
- [x] **Automated Test Project**: Added xUnit integration tests using `WebApplicationFactory` and an isolated in-memory database.

### Documentation
- [x] **API Documentation**: Documented API endpoints and example requests/responses in Postman.
- [x] **README Update**: Detailed documentation of the project setup, API endpoints, and progress in README.md.

### Continuous Integration/Continuous Deployment
- [x] **CI Pipeline**: GitHub Actions restores, builds, and tests the API and installs, tests, and builds the frontend.

### Frontend Development
- [x] **React Frontend Setup**: Initialized a new React project using Create React App.
- [x] **Project Structure**: Organized the React project with separate directories for components and services.
- [x] **Implemented Components**: Developed components for listing, adding, editing, and deleting aircrafts.
- [x] **API Integration**: Integrated React components with the backend API using Axios.
- [x] **Styling**: Added CSS for consistent styling across components.

## Prerequisites

- .NET 8 SDK
- MySQL server
- Node.js 20 and npm
- Visual Studio or Visual Studio Code
- Postman (optional, for manual API exploration)

## Setup

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/omniV1/GCU_SWE_2023-2025.git
cd GCU_SWE_2023-2025/SummerPractice/AerospaceAPI/AircraftMaintenanceAPI
```

### Setup the Database

Make sure you have MySQL installed and running. Then, create a new database for the project:

CREATE DATABASE AircraftMaintenanceDB;

### Configure Connection String

Keep credentials out of `appsettings.json`. Store the local connection string with
.NET user secrets:

```bash
dotnet user-secrets set "ConnectionStrings:DefaultConnection" "Server=localhost;Port=3306;Database=AircraftMaintenanceDB;User=your_user;Password=your_password;"
```

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

Install the locked dependencies:

npm ci

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

From the `AerospaceAPI` directory, run the backend integration tests:

```bash
dotnet restore AircraftMaintenanceAPI/AircraftMaintenanceAPI.sln --configfile ../../NuGet.Config
dotnet test AircraftMaintenanceAPI/AircraftMaintenanceAPI.sln --no-restore
```

Run the frontend test once, without interactive watch mode:

```bash
cd aircraft-maintenance-frontend
npm test -- --watchAll=false
```

The backend suite currently exercises representative aircraft endpoint behavior:
not-found responses, validation, creation, persistence, and retrieval. The
frontend suite smoke-tests the main aircraft list route and navigation.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Future TODOS

- [ ] **User Authentication and Authorization**: Implement user registration, login, and role management.
- [ ] **Search and Filter Functionality**: Add search and filter options for aircrafts.
- [ ] **Additional Features**: Implement additional features such as notifications and reporting.
- [ ] **Performance Optimization**: Optimize API performance and database queries.
- [ ] **Documentation**: Enhance documentation with detailed usage examples and setup guides.
- [ ] **Automated Tests**: Expand integration coverage to maintenance record endpoints and failure paths.
