/*
* Owen Lindsey
* CST-391
* activity 3
* 03/14/2024
* Citations found in documentation 
* //////////////// DOCUMENTATION LINK ///////////////
* 
* //////////////////////////////////////////////////
*/

// Core Angular modules for app startup and functionality
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser'; // Module to run the app in a web browser
import { FormsModule, ReactiveFormsModule } from '@angular/forms'; // Modules for template-driven and reactive forms, respectively

// Main application component
import { AppComponent } from './app.component';
// Routing module to handle navigation within the app
import { AppRoutingModule } from './app-routing.module';

// Component imports for different features of the application
import { CreateAlbumComponent } from './create-album/create-album.component';
import { DeleteAlbumComponent } from './delete-album/delete-album.component';
import { DisplayAlbumComponent } from './display-album/display-album.component';
import { EditAlbumComponent } from './edit-album/edit-album.component';
import { ListAlbumsComponent } from './list-albums/list-albums.component';
import { ListArtistsComponent } from './list-artists/list-artists.component';

// Decorator marking the class as an NgModule and providing metadata about the module
@NgModule({
	declarations: [
		// Components that belong to this NgModule
		AppComponent,
		CreateAlbumComponent,
		DeleteAlbumComponent,
		DisplayAlbumComponent,
		EditAlbumComponent,
		ListAlbumsComponent,
		ListArtistsComponent,
	],
	imports: [
		// Other modules whose exported classes are needed by component templates declared in this NgModule
		AppRoutingModule, // Routing for the application
		BrowserModule, // Necessary for running the app in a web browser
		FormsModule, // For using template-driven forms
		ReactiveFormsModule // For using reactive forms
	],
	providers: [
		// Creators of services that this NgModule contributes to the global collection of services; they become accessible in all parts of the app
		// (Empty in this case, indicating no providers are added)
	],
	bootstrap: [
		AppComponent // The main application view, called the root component, that hosts all other app views. Only the root NgModule should set the bootstrap property.
	]
})
export class AppModule { }
