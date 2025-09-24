# Angular Project Structure Overview

##### Owen Lindsey

##### CST-391

###### This work was done with help from the assignment guide

---

This document serves as a guide to understand the structure of an Angular project and the purpose of its key files and directories.

## Directory Structure

| Folder/File           | Purpose                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------|
| `node_modules/`       | Contains all the libraries and dependencies necessary for the project.                    |
| `src/`                | The main folder where the source code of the application lives.                           |
| `src/app/`            | Contains components, services, and other files that constitute the application's logic.   |
| `src/assets/`         | Stores static assets like images, fonts, and other files that can be used across the app. |
| `src/environments/`   | Houses configuration files for different environments, like production or development.    |

## Key Files

| File              | Purpose                                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| `angular.json`    | Configuration file for Angular CLI that specifies how to build, serve, test, and lint the application.                        |
| `package.json`    | Lists the project dependencies and metadata, including scripts for common commands like build and start.                      |
| `tsconfig.json`   | Provides the TypeScript compiler with instructions on how to compile TypeScript code into JavaScript.                         |

## How Angular Generates the Default Page

- `main.ts`: Initializes the platform that your application runs in, then uses the `AppModule` to bootstrap your application.

- `app.component.*`: 
  - `app.component.css`: Defines the styles for the root component.
  - `app.component.html`: Contains the HTML template for the root component.
  - `app.component.ts`: Contains the logic for the root component, such as data and behavior.

- `app.module.ts`: The root module that tells Angular how to assemble the application. It identifies the app's components, templates, and services.

## Detailed Explanations

### `node_modules/`
This directory is auto-generated when you install dependencies for your project using npm (Node Package Manager). You will not need to manually alter the contents of this directory.

### `src/`
The `src/` folder is the working directory where you will spend most of your time. It contains the application logic, views, styles, images, and anything else your app will need.

### `src/app/`
The `src/app/` folder is where the core of your Angular application lives. It includes modules, components, services, and everything that makes up the logical structure of your application.

### `src/assets/`
The `src/assets/` folder is a place to store static asset files like images, icons, JSON files, and more. These files can be referenced and used throughout your application.

### `src/environments/`
The `src/environments/` folder contains configuration settings for different stages of your application deployment, such as development, staging, and production.

### `angular.json`
The `angular.json` file is like a blueprint for the Angular CLI. It defines various configurations for projects and specifies default settings for builders and schematics.

### `package.json`
The `package.json` file acts like a manifest for the application. It defines project dependencies and contains scripts to run tasks like starting the dev server, building the application, and running tests.

### `tsconfig.json`
The `tsconfig.json` file contains settings for the TypeScript compiler. TypeScript enhances JavaScript with types, and this file includes the rules on how TypeScript should be transpiled into JavaScript.

### `main.ts`
The `main.ts` file is the entry point for your Angular app. It's responsible for bootstrapping the root Angular module (`AppModule`) to run in the browser.

### `app.component.*`
- `app.component.css`: Styles specific to the `AppComponent`.
- `app.component.html`: The view template for the `AppComponent`.
- `app.component.ts`: The TypeScript file that contains the logic for the `AppComponent`, including properties and methods.

### `app.module.ts`
The `app.module.ts` file is the root module of the application. It's where you tell Angular about other components and modules that the app depends on.


### Screenshots 

---

1. **Terminal showing Angular version.**

![Terminal showing Angular version](https://github.com/omniV1/CST-391/blob/main/docs/activity2/screenshots/angular_version.png)


2. **app inital page structure before editing the app.component.ts.**

![app-inital](https://github.com/omniV1/CST-391/blob/main/docs/activity2/screenshots/angularapp-initial.png)


3. **h3 element added to the app.component.ts file.**
   
  
![h3 element added](https://github.com/omniV1/CST-391/blob/main/docs/activity2/screenshots/angularapp-h3.png)


4. **App message modifaction to the app.component.ts.**
   

![App Message modifcation](https://github.com/omniV1/CST-391/blob/main/docs/activity2/screenshots/angularapp-message.png)

