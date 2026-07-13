# Aircraft Maintenance Frontend

This project is a React 18 frontend built with Create React App and CRACO. It
uses React Router, Axios, and project CSS to manage aircraft and maintenance
records through the Aircraft Maintenance API.

## Major Checkpoints

### Project Setup
- [x] **Initialized React Project**: Created a new React project using Create React App.
- [x] **Organized Project Structure**: Structured the project with separate directories for components and services.

### Component Development
- [x] **AircraftList Component**: Developed to display a list of all aircrafts.
- [x] **AircraftDetails Component**: Created to show details of a specific aircraft.
- [x] **AircraftForm Component**: Built to handle adding and updating aircrafts.
- [x] **AircraftEdit Component**: Added to facilitate editing of existing aircrafts.

### API Integration
- [x] **Configured Axios**: Set up Axios to communicate with the backend API.
- [x] **Implemented CRUD Operations**: Integrated the frontend components with the API for full CRUD functionality.

### Routing
- [x] **Set Up React Router**: Configured routing to navigate between different components.

### Styling
- [x] **Styled Components**: Added CSS for a consistent and clean UI.

## Prerequisites

- Node.js and npm
- Node.js 20 and npm

## Setup

### Clone the Repository

1.) First, clone the repository to your local machine:
```
git clone https://github.com/omniV1/GCU_SWE_2023-2025.git
cd GCU_SWE_2023-2025/SummerPractice/AerospaceAPI/aircraft-maintenance-frontend

```
### Install Dependencies

2.) Install the necessary dependencies:
```
npm ci
```
### Run the Application

3.) Start the React development server:
```
npm start
```

The frontend application should now be running on `http://localhost:3000`.

## Project Structure
``` Plain text
aircraft-maintenance-frontend/
├── public/
│ ├── favicon.ico
│ ├── index.html
│ ├── logo192.png
│ ├── logo512.png
│ ├── manifest.json
│ └── robots.txt
├── src/
│ ├── components/
│ │ ├── AircraftDetails.js
│ │ ├── AircraftEdit.js
│ │ ├── AircraftForm.js
│ │ ├── AircraftList.js
│ │ ├── Footer.js
│ │ ├── Header.js
│ │ └── NavBar.js
│ ├── services/
│ │ └── api.js
│ ├── styles/
│ │ └── App.css
│ ├── App.js
│ ├── App.test.js
│ ├── index.css
│ ├── index.js
│ ├── logo.svg
│ ├── reportWebVitals.js
│ └── setupTests.js
├── .gitignore
├── package-lock.json
├── package.json
└── README.md
```

## Components

### AircraftList Component

Displays a list of all aircrafts.

### AircraftDetails Component

Shows details of a specific aircraft.

### AircraftForm Component

Handles adding new aircrafts.

### AircraftEdit Component

Facilitates editing of existing aircrafts.

## Services

### API Service (api.js)

Handles communication with the backend API using Axios.

- **getAircrafts**: Retrieves all aircrafts.
- **getAircraftById**: Retrieves a specific aircraft by ID.
- **createAircraft**: Adds a new aircraft.
- **updateAircraft**: Updates an existing aircraft.
- **deleteAircraft**: Deletes an aircraft by ID.

## Routing

The application uses React Router to navigate between different components:

- **/**: Home page displaying the list of aircrafts.
- **/add**: Page for adding a new aircraft.
- **/edit/:id**: Page for editing an existing aircraft.

## Styling

Component and application styles are split across `src/styles` and `src/index.css`.

## Running Tests

The current smoke test verifies that the main aircraft list route and primary
navigation render while the API request is mocked. Run it once in
non-interactive mode with:
```
npm test -- --watchAll=false
```
## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Future TODOS

- [ ] **Error Handling**: Implement more robust error handling and display error messages in the UI.
- [ ] **Validation**: Add form validation to ensure data integrity.
- [ ] **User Authentication**: Implement user authentication and authorization.
- [ ] **Styling Improvements**: Enhance the UI with more styling and responsiveness.
- [ ] **Automated Tests**: Expand component coverage for forms, API errors, and maintenance record workflows.

## APP Layout

![Add](https://github.com/omniV1/SummerPractice/blob/main/AerospaceAPI/aircraft-maintenance-frontend/screenshots/Add.png)


![Edit](https://github.com/omniV1/SummerPractice/blob/main/AerospaceAPI/aircraft-maintenance-frontend/screenshots/Edit.png)

![View](https://github.com/omniV1/SummerPractice/blob/main/AerospaceAPI/aircraft-maintenance-frontend/screenshots/View.png)

![delete](https://github.com/omniV1/SummerPractice/blob/main/AerospaceAPI/aircraft-maintenance-frontend/screenshots/delete.png)
