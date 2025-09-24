### Part 1: Basic Angular Components, Events, Routes, and Data Binding

#### Overview

### Deliverables: 

Screenshots
Below are screenshots demonstrating the responsiveness of the Bootstrap grid layout along with the page showing our components:

Small Screen:
![Small Screen](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/small-screen.png)

Large Screen:
![Large Screen](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/bigs-screen.png)


# Research
1. **Describe @Input decorator used in info.component.ts**:
The @Input decorator in Angular is a way of defining inputs for a component. It allows data to flow from a parent component into a child component. Essentially, it marks a class field as an input property and supplies configuration metadata. The @Input property is bound to a DOM property in the template. When an external component interacts with the child component, it can pass data to the @Input property, allowing the child component to use external data within its class.

For example, in info.component.ts, if we have:

```typescript
@Input() name!: string;
```
This means the InfoComponent expects to receive a name value from its parent component, which it can use internally, such as displaying it in its template.

---
2. **Describe [value] used in info.component.html**:
The [value] binding in Angular templates is a way to bind a property of a component to the value attribute of an HTML element. This is a one-way binding from the component to the view. It is often used within `select` elements to bind each `option` element's value to a dynamic value from the component's class.


```html
<option *ngFor="let product of products" [value]="product">{{product}}</option>
```

This code iterates over the products array defined in the component's TypeScript file and sets the value of each `option` in a `select` dropdown to the corresponding product. When a user selects an option, the selected product's value is used, which can be bound to a model or used in form submission.

---
3. **Describe [(ngModel)] also used in info.component.html**:
The [(ngModel)] directive is used in Angular forms to enable two-way data binding between the template form control and the component's property. This means that any changes to the form control's value in the UI are immediately reflected in the associated component's property and vice versa.

```html
<input type="text" [(ngModel)]="selectedProduct" name="product">
```

It binds the input element's value to the selectedProduct property on the component. If the user changes the input, selectedProduct is updated with the new value. Likewise, if selectedProduct is programmatically changed in the component, the input's value in the UI is updated to reflect this change. This directive is particularly useful for forms, as it simplifies handling form inputs and validations by ensuring the view and the component are always in sync.

---

### Part 2: Creating a Music Application – The Front End

#### Overview

In this activity, we built the front end for the Music application by implementing multiple components, handling page events, and binding data to a view template.

#### Execution

We executed this assignment according to the following guidelines:

1. **Creating the Music Application:**
   - We created an Angular application named `musicapp` following the same initial instructions as Part 1.
   - Angular routing support was added during application creation, and Bootstrap and Popper dependencies were included.

2. **Adding Mock JSON and Album Images:**
   - A `data` directory was created in the `src` directory to store mock JSON data.
   - Sample music data and album images were copied from the provided "CST-391 Activity 3 Part 2 Resources" zip file to the appropriate directories.
   - A TypeScript typings file was added to treat the JSON data as TypeScript modules.

3. **Creating Object Models:**
   - Object model classes for artists and albums were created in the `models` directory under `src/app`.
   - These models were copied from the provided resources and matched exactly to the server's API object models.

4. **Updating the Routes Module:**
   - The routes module (`app-routing-module.ts`) was updated to include routes for all the components: creating, listing, displaying, editing, and deleting albums.
   - Imports for all components were added to the file.

5. **Adding a Bootstrap NavBar:**
   - The `app.component.html` file was modified to include a Bootstrap NavBar with navigation links and button functionalities.
   - The application title was changed to "My Music Collection," and a version property was added.
   - Functions were added to display version information and artist lists.
   
6. **Creating the Music Service:**
   - A service directory was created under `src/app` to contain the Music Service.
   - The `music-service.service.ts` file was copied from the provided resources and implemented to fetch music data using mocked JSON.
   - Methods were added to retrieve artists, albums, create, update, and delete albums.

7. **Updating the App Component:**
   - The `app.component.ts` file was updated to inject a Router into the constructor and define functions to navigate to the artist list component.
   
8. **Implementing Components:**
   - Components were generated for listing artists, listing albums, creating albums, displaying albums, editing albums, and deleting albums.
   - Each component was implemented with necessary functionalities, including data binding and event handling.


9. **Captioned Screenshots:**
   a. Initial application page 
![Initial Screen](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/initial-screen.png)

   b. GCU homepage
 ![GCU Homepage](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/gcu-homepage.png)

   c. Create Album page
![Create Album](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/create-album.png)

   d. Artist List page showing the added album/artist
![Artists List](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/artsits-list.png)
   
   e. About Box:
![About Box](https://github.com/omniV1/CST-391/blob/main/docs/activity3/Screenshots/about-box.png)


11. **Research Questions:**
- Complete comments for `music-service.service.ts` providing detailed explanations of each method and its functionality.
  
  - [Link to music-service.service.ts](https://github.com/omniV1/CST-391/blob/main/src/activity3/Musicapp/src/app/service/music-service.service.ts)

## References

- **Angular Components**: Documentation on Angular components and their lifecycle hooks.
  - [Angular Components Overview](https://angular.io/guide/component-overview)

- **Angular CLI**: Official Angular CLI documentation for creating and managing Angular projects.
  - [Angular CLI Documentation](https://angular.io/cli)

- **Angular Routing & Navigation**: Guides on how Angular routing works and how to implement it.
  - [Angular Routing & Navigation](https://angular.io/guide/router)

- **Data Binding**: Explanation of data binding in Angular and how it's used to display dynamic data in templates.
  - [Angular Data Binding Guide](https://angular.io/guide/binding-syntax)

- **@Input and @Output decorators**: Deep dive into how to pass data into and out of Angular components.
  - [Component Interaction](https://angular.io/guide/inputs-outputs)

- **Angular Forms**: Guide to implementing forms in Angular, including template-driven and reactive approaches.
  - [Angular Forms](https://angular.io/guide/forms-overview)

- **Bootstrap in Angular**: How to integrate Bootstrap styles and components with Angular applications.
  - [Integrating Bootstrap with Angular](https://ng-bootstrap.github.io/#/home)
