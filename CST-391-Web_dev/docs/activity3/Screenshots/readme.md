### Part 1: Basic Angular Components, Events, Routes, and Data Binding

#### Overview

In this activity, we built a simple test application that implements multiple components, handles page events, and binds data to a view template.

#### Execution

We executed this assignment according to the following guidelines:

1. **Creating a Simple Application:**
   - We navigated to the desired location and created a directory named `simpleapp`.
   - Next, we used the Angular CLI to create a new Angular application named `simpleapp`, selecting Angular routing and CSS options during installation.

2. **Creating a VS Code Workspace:**
   - We created a VS Code Workspace by selecting the `simpleapp` directory and saving it for future use.

3. **Starting the Application:**
   - We navigated to the `simpleapp` directory and started the Node server using the command `ng serve --o`. This automatically opened the application in the default web browser.

4. **Adding Bootstrap and Popper Modules:**
   - Bootstrap and Popper modules were added to the application using npm commands.
   - We updated the `angular.json` file to include Bootstrap styles and scripts for the application.

5. **Implementing Bootstrap Grid Layout:**
   - We replaced the contents of `app.component.html` with a Bootstrap grid layout.

6. **Verifying Responsiveness:**
   - Using Chrome Dev Tools, we verified the responsiveness of the grid layout by toggling between device emulations.

#### Code Snippets

```json
"styles": [
    "node_modules/bootstrap/dist/css/bootstrap.css"
],
"scripts": [
    "node_modules/bootstrap/dist/js/bootstrap.bundle.js"
]
```

```html 
<!-- Bootstrap Grid Layout -->
<div class="container">
    <div class="row">
        <div class="col-sm">Column 1</div>
        <div class="col-sm">Column 2</div>
        <div class="col-sm">Column 3</div>
    </div>
</div>

```

Screenshots
Below are screenshots demonstrating the responsiveness of the Bootstrap grid layout:

Small Screen:


Large Screen: