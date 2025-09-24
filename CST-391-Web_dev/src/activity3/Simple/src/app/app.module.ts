// Importing core Angular modules and specific functionalities
import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
// Importing routing and component classes from the application
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ShopComponent } from './shop/shop.component';
import { InfoComponent } from './info/info.component';

// Decorating the AppModule class with @NgModule to specify app metadata
@NgModule({
  declarations: [
    // Declaring components that this module uses. These components can now be used in this module.
    AppComponent,
    ShopComponent,
    InfoComponent,
  ],
  imports: [
    // Importing BrowserModule: essential for running the app in a web browser.
    BrowserModule,
    // Importing AppRoutingModule: defines routes for the application.
    AppRoutingModule,
    // Importing ReactiveFormsModule: provides reactive forms functionality.
    ReactiveFormsModule,
    // Importing FormsModule: provides template-driven forms functionality.
    FormsModule,
  ],
  providers: [
    // Registering provideClientHydration(): a service/function for client hydration (specific to this setup, might involve server-side rendering).
    provideClientHydration()
  ],
  bootstrap: [
    // Bootstrapping AppComponent: Angular creates an instance of AppComponent and inserts it into the index.html host web page.
    AppComponent
  ]
})
export class AppModule { }
