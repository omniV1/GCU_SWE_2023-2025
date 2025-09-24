# CST-391: JavaScript Web Application Development
### Welcome to the CST-391 repository! 

### This repository contains all the materials for the CST-391: JavaScript Web Application Development.

### **docs**: contains all documentation for activities and milestone ( screen shots,  research questions, etc). 

### **src**: contains all src code for all activites and milestone


| Activity                              | Description                                                                                      |
|---------------------------------------|--------------------------------------------------------------------------------------------------|
| **Activity 0:**                       |                                                                                                  |
| NodeJS "Hello World" Application      | Setting up a basic NodeJS app and running a "Hello World" script.                                 |
| Express/NodeJS Hello World           | Implementing an Express/NodeJS server to serve "Hello World" text.                                |
| NodeJS with TypeScript               | Exploring NodeJS development with TypeScript.                                                    |
| Installing node -v and npm -v        | Confirming Node.js and npm installation.                                                         |
--
| **Activity 1:**                       |                                                                                                  |
| Routes Declared                      | Defining CRUD routes for artists and albums in Express.                                           |
| Postman Tests                        | Conducting Postman tests to verify route functionality.                                           |
| Code Implementation                  | Implementing routes and controller actions.                                                       |
| Documentation                        | Providing documentation for each route.                                                           |
--
| **Activity 2:**                       |                                                                                                  |
| Installation of Angular CLI          | Installing Angular CLI and verifying the version.                                                 |
| Creation of Test Application         | Creating a test Angular app with routing and CSS options.                                         |
| Setup of VS Code Workspace           | Setting up a VS Code Workspace for project management.                                            |
| Running the Application              | Starting the Node server and opening the app in a browser.                                        |
| Modifying Component Files            | Updating the app component and adding new member variables.                                       |
| Research                             | Describing the Angular project structure and default page generation.                              |
--
| **Activity 3:**                       |                                                                                                  |
| Basic Angular Components             | Creating a simple Angular app with Bootstrap integration.                                         |
| Simple Data Binding                  | Implementing data binding and form handling.                                                      |
| Building a New Component             | Generating a new component demonstrating 2-way data binding.                                       |
| Research                             | Explaining the usage of Angular decorators and directives.                                         |
--
| **Activity 4:**                       |                                                                                                  |
| Create a Copy of Music Application   | Copying the existing Music app for further modifications.                                         |
| Add HTTP Client Module               | Importing HttpClientModule for HTTP client functionality.                                          |
| Refactor Music Service               | Refactoring the service to use HttpClient for live data fetching.                                  |
| Research                             | Recommending research on Angular app state maintenance.                                            |
--
| **Milestone 3 - Rest API:**          |                                                                                                  |
| Project Proposal                     | Providing a detailed project description, requirements, and REST API specifications.               |
| Postman API Documentation           | Creating detailed API documentation for interacting with the app.                                  |
| Diagrams and Wireframes             | Developing ER and UML diagrams, wireframes for the web app.                                        |



# Closer look at activites 
- **Activity 0:** 
 1. **NodeJS "Hello World" Application**
This project started with a basic NodeJS "Hello World" application. It involved running a simple JavaScript file (`app.js`) in the integrated terminal, demonstrating the initial setup and execution of a NodeJS script.

1. **Express/NodeJS Hello World**

    Following the NodeJS introduction, the project progressed to implementing an Express/NodeJS "Hello World" server. This included setting up a web server with Express and serving a basic webpage displaying the "Hello World" text.

2. **NodeJS with TypeScript**

    The project then explored NodeJS development with TypeScript. It involved converting the Express server code to TypeScript and adding comments for clarity. The TypeScript code was compiled to JavaScript and executed, demonstrating the use of TypeScript in NodeJS projects.

3. **Installing node -v and npm -v**

    Finally, the installation of Node.js and npm was confirmed using terminal commands `node -v` and `npm -v`. This step ensured that the necessary Node.js and npm versions were installed properly for development.
 ---

- **Activity 1:** 
1. **Routes Declared:**
In this activity, routes for handling various CRUD (Create, Read, Update, Delete) operations were declared for both artists and albums. These routes were implemented using Express.js and specified the corresponding controller actions to handle requests.

2. **Postman Tests:**
Postman tests were conducted to ensure the functionality of the implemented routes. Screenshots were taken to demonstrate the successful execution of the tests, as well as any failures encountered during testing.

3. **Code Implementation:**
The implementation of routes and controller actions was done in the app.ts file. Each route was mapped to its corresponding controller action, ensuring proper handling of incoming requests and responses.

4. **Documentation:**
Documentation was provided for each route, specifying its purpose, HTTP method, route path, and associated controller action. This documentation served as a reference for understanding the API endpoints and their functionalities.

---
- **Activity 2:** 
 1. **Installation of Angular CLI:**
The Angular CLI was installed globally using the npm package manager. The version of Angular CLI was verified using the ng version command.

2. **Creation of Test Application:**
A new Angular application named testapp was created using the Angular CLI. During the creation process, Angular routing and CSS styling options were selected.

3. **Setup of VS Code Workspace:**
A VS Code Workspace was created by opening the testapp directory and saving it as a workspace file. This allowed for easy management and navigation of the project files.

4. **Running the Application:**
The Node server was started using the ng serve -o command, which automatically opened the application in the default web browser.

5. **Modifying Component Files:**
The app.component.ts file was modified to change the value of the title variable, and the changes were automatically reflected in the browser. Additionally, a new class member variable named message was added, and its value was rendered in the Component Template.

6. **Research:**
The purpose of each folder and file in the default project structure was described, including node_modules, src, src/app, src/assets, src/environments, angular.json, package.json, and tsconfig.json.
An overview of how the default page is generated by Angular was provided by describing the purpose of files like main.ts, app.component.css, app.component.html, app.component.ts, and app.module.ts.

---
- **Activity 3:** 
  
### Part 1: Basic Angular Components, Events, Routes, and Data Binding:

1. ***Create a Simple Application:**
Angular CLI was used to generate a new Angular application named simpleapp. Bootstrap and Popper modules were added, and a responsive grid layout was implemented.

2. **Simple Data Binding to Labels and Handling a Form Post:**
A new component named shop was created, implementing reactive forms for data handling. Form submission and data display functionalities were added, demonstrating 2-way data binding.

3. **Building a New Component with Leverage 2-Way Data Binding:**
Another component named info was generated, showcasing 2-way data binding with form controls and displaying dynamic content based on user input.

4. **Research:**
The usage of @Input decorator, [value] attribute, and [(ngModel)] directive were described in the context of Angular components and templates.

### Part 2: Creating a Music Application – The Front End:

1. **Create the Music Application:**
An Angular application named musicapp was created, with routing support and Bootstrap integration.

2. **Add Mock JSON and Album Images to the Application:**
Mock JSON data and album images were added to the application, along with necessary TypeScript typings for JSON modules.

3. **Create the Object Models:**
Object model classes for artists and albums were created and placed in the models directory.

4. **Update the Routes Module:**
The routes module (app-routing-module.ts) was updated to include routes for various components, such as creating, listing, displaying, editing, and deleting albums.

5. **Add a Bootstrap NavBar:**
A Bootstrap NavBar was added to the application with navigation links and button functionalities.

6. **Create a Music Service:**
A music service (music-service.service.ts) was implemented to handle data retrieval and manipulation operations, including fetching artists and albums.

7. **Implement Components:**
Components for listing artists, listing albums, creating albums, displaying albums, editing albums, and deleting albums were implemented with appropriate functionalities.

8. **Research:**
Complete comments were added to the music-service.service.ts file, detailing the functionality and usage of each method.
---
- **Activity 4:** 
 1. **Create a Copy of the Music Application:**
The existing Music application is copied to a new directory for further modifications and integration with the backend.

2. **Add the HTTP Client Module:**
HttpClientModule is imported and added to the imports list in app.module.ts to enable HTTP client functionality in the Angular application.

3. **Refactor the Music Service:**
The Music service is refactored to utilize HttpClient for fetching live data from the backend instead of hard-coded data.
Methods are updated to handle asynchronous operations and callback functions are used to process the received data.
The hard-coded data is progressively replaced with live API data, ensuring the proper functioning of the application.

4. **Research:**

Research on how an Angular application maintains a logged-in state and communicates this state to the server is recommended.



# **Milestone Project**
 ### Objective

The objective of the milestone project is to design and develop a comprehensive web application using JavaScript frameworks such as React and Angular, integrated with an Express.js server. The project will involve creating backend services using Express and Node.js, implementing a REST API for CRUD operations on product data stored in a MySQL database, and developing frontend web applications using Angular and React frameworks.

### Features

- Ability to list, create, read, update, and delete products (modified GameCubes).
- Integration of two frontend web applications with backend REST APIs.
- Optional Christian theme, with considerations for building an app serving Christian communities.

### Documentation

The project documentation includes technical decisions, technical designs, UML diagrams, ER diagrams, UI designs, and other technical artifacts captured in the design report.

## Directory Structure

- **src**: Contains source code for the milestone project.
- **docs**: Holds documentation including diagrams, wireframes, site maps, and other related materials.

## Milestone 3 - Rest API Using Express Framework

For Milestone 1, a project proposal was created defining the functionality and scope of the complete web application. It includes:

- Detailed project description.
- List of requirements.
- REST API specifications.
- Diagrams (ER, UML).
- Wireframes.
- Site map.

## Postman API Documentation

The Postman API documentation provides detailed information about the REST API endpoints for interacting with the GameCube store.

**API Src Code Location:** [GitHub Repository](https://github.com/omniV1/CST-391/tree/main/src/Milestone/src)

## Diagrams and Wireframes

- **ER Diagram**: Represents the entity-relationship model for the database.
- **UML Diagrams**: Includes diagrams for services, shopping cart, and GameCube.
- **Wireframes**: Provides wireframes for various pages of the web application.

