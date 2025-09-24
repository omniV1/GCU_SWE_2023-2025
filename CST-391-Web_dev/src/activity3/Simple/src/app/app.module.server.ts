// Importing NgModule decorator from Angular core, which is essential for defining an Angular module.
import { NgModule } from '@angular/core';
// Importing ServerModule from Angular's platform-server package. This module is used for server-side rendering of the application.
import { ServerModule } from '@angular/platform-server';

// Importing the root application module, AppModule, to include it in the server module.
import { AppModule } from './app.module';
// Importing the root AppComponent to specify it as the bootstrap (or entry) component.
import { AppComponent } from './app.component';

// Using the NgModule decorator to declare the AppServerModule. This decorator function takes a single metadata object whose properties describe the module.
@NgModule({
  imports: [
    // Including the AppModule, the root application module containing components, services, and other modules the application depends on.
    AppModule,
    // Including the ServerModule, which provides services necessary for server-side rendering.
    ServerModule,
  ],
  // Specifying the AppComponent as the bootstrap component. This is the root component that Angular creates and inserts into the server-side rendered page.
  bootstrap: [AppComponent],
})
// Exporting the AppServerModule class. This module is specific for server-side rendering purposes, allowing the Angular app to be rendered on the server.
export class AppServerModule {}
