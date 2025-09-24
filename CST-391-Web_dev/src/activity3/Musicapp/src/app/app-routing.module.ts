//  Angular modules for routing are imported.
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

// Import statements for each component that will be routed to in the application.
// These components correspond to different views/pages in your app.
import { CreateAlbumComponent } from './create-album/create-album.component';
import { DeleteAlbumComponent } from './delete-album/delete-album.component';
import { DisplayAlbumComponent } from './display-album/display-album.component';
import { ListAlbumsComponent } from './list-albums/list-albums.component';
import { ListArtistsComponent } from './list-artists/list-artists.component';

// Routes array where each route is defined as an object.
// 'path' defines the URL path, and 'component' specifies which component to render.
const routes: Routes = [
	{ path: 'create', component: CreateAlbumComponent }, // Route for creating a new album.
	{ path: 'list-artists', component: ListArtistsComponent }, // Route to list all artists.
	{ path: 'list-albums', component: ListAlbumsComponent }, // Route to list all albums.
	{ path: 'display/:id', component: DisplayAlbumComponent }, // Dynamic route to display a specific album based on its 'id'.
	{ path: 'delete/:artist/:id', component: DeleteAlbumComponent } // Dynamic route to delete a specific album. Also requires 'artist' and 'id'.
];

// @NgModule decorator to define this class as an Angular module.
@NgModule({
	imports: [
		RouterModule.forRoot(routes) // Configuring the router at the application's root level.
		// The 'routes' array defined above is passed to 'forRoot' to register the routes.
	],
	exports: [
		RouterModule // Exporting RouterModule allows it to be imported into the root module (AppModule),
		             // making the routing configuration available throughout the application.
	]
})
export class AppRoutingModule { }
