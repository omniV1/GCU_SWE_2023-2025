// Importing the NgModule decorator from Angular core, which is essential for defining an Angular module.
import { NgModule } from '@angular/core';
// Importing RouterModule and Routes from Angular's router package. RouterModule is used to configure the router in Angular applications, and Routes is a type that represents route configurations.
import { RouterModule, Routes } from '@angular/router';

// Defining an empty array of routes. This is where you would add your app's route configurations.
// Each route will be an object that maps a URL path to a component.
const routes: Routes = [];

// Using the NgModule decorator to declare the AppRoutingModule. This decorator function takes a single metadata object whose properties describe the module.
@NgModule({
  // Importing the RouterModule and calling its forRoot method, passing in the routes array.
  // The forRoot method is used to provide the router service at the application's root level.
  // It initializes the router and starts it listening for browser location changes.
  imports: [RouterModule.forRoot(routes)],
  
  // Exporting RouterModule allows components in other modules that import this AppRoutingModule to have access to router directives like RouterLink and RouterOutlet.
  exports: [RouterModule]
})
// Exporting the AppRoutingModule class, which encapsulates the route configuration for the app. By separating the routing into its own module,
// we adhere to the principle of modular design and can keep the app's structure organized.
export class AppRoutingModule { }
