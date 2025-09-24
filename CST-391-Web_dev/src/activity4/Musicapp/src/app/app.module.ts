/*
* Owen Lindsey
* CST-391
* activity 4 
* 03/14/2024
* Citations found in documentation 
* //////////////// DOCUMENTATION LINK ///////////////
* 
* //////////////////////////////////////////////////
*/

// NgModule decorator and core Angular modules are imported to define the module's metadata and functionality.
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

// AppRoutingModule is imported to include routing capabilities in the application.
import { AppRoutingModule } from './app-routing.module';
// AppComponent and other components are imported to declare them as part of this module.
import { AppComponent } from './app.component';
import { ListArtistsComponent } from './list-artists/list-artists.component';
import { ListAlbumsComponent } from './list-albums/list-albums.component';
import { CreateAlbumComponent } from './create-album/create-album.component';
import { DisplayAlbumComponent } from './display-album/display-album.component';
import { EditAlbumComponent } from './edit-album/edit-album.component';
import { DeleteAlbumComponent } from './delete-album/delete-album.component';
// FormsModule is imported to use template-driven forms, enabling the use of ngModel for two-way data binding.
import { FormsModule } from '@angular/forms';
// HttpClientModule is imported to make HTTP requests to external APIs or backend endpoints.
import { HttpClientModule } from '@angular/common/http';

// Decorator that marks a class as an NgModule and supplies configuration metadata.
@NgModule({
  declarations: [
    // List of components that belong to this module. Angular creates a factory for each component.
    AppComponent,
    ListArtistsComponent,
    ListAlbumsComponent,
    CreateAlbumComponent,
    DisplayAlbumComponent,
    EditAlbumComponent,
    DeleteAlbumComponent
  ],
  imports: [
    // List of modules required by this module. BrowserModule is needed for running the app in a browser.
    BrowserModule,
    // FormsModule is included to work with Angular forms.
    FormsModule,
    // HttpClientModule is included to perform HTTP requests.
    HttpClientModule,
    // AppRoutingModule is included for configuring the routes of the application.
    AppRoutingModule
  ],
  providers: [
    // Services that are available to be injected into components. Empty here, but you can add any service providers.
  ],
  bootstrap: [
    // The main application view, called the root component, that hosts all other app views. Only the root module should set this bootstrap property.
    AppComponent
  ]
})
// The class name follows the Angular naming convention, appending Module to the class name.
export class AppModule {}
