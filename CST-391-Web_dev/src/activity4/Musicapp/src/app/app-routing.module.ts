// app-routing.module.ts

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

// Import all components that need routing
import { ListArtistsComponent } from './list-artists/list-artists.component';
import { ListAlbumsComponent } from './list-albums/list-albums.component';
import { CreateAlbumComponent } from './create-album/create-album.component';
import { DisplayAlbumComponent } from './display-album/display-album.component';
import { EditAlbumComponent } from './edit-album/edit-album.component';
import { DeleteAlbumComponent } from './delete-album/delete-album.component';

// Define routes
const routes: Routes = [
  // Default route redirects to list-artists
  { path: '', redirectTo: '/list-artists', pathMatch: 'full' },
  
  // Route for listing all artists
  { path: 'list-artists', component: ListArtistsComponent },
  
  // Route for listing albums (optional artist parameter)
  { path: 'list-albums', component: ListAlbumsComponent },
  { path: 'list-albums/:artist', component: ListAlbumsComponent },
  
  // Route for creating new album
  { path: 'create', component: CreateAlbumComponent },
  
  // Route for displaying album details
  { path: 'display/:id', component: DisplayAlbumComponent },
  
  // Route for editing album
  { path: 'edit/:artist/:id', component: EditAlbumComponent },
  
  // Route for deleting album
  { path: 'delete/:artist/:id', component: DeleteAlbumComponent },
  
  // Wildcard route for 404 - put this last
  { path: '**', redirectTo: '/list-artists' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }