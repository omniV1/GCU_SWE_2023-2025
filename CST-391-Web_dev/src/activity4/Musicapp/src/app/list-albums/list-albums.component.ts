// Importing Angular core decorators and interfaces for component interaction and lifecycle hooks.
import { Component, Input, OnInit } from '@angular/core';
// Importing a custom service that handles music-related data fetching.
import { MusicServiceService } from '../service/music-service.service';
// Importing Album and Artist models for type safety and structure.
import { Album } from '../models/albums.model';
import { Artist } from '../models/artists.model';

// The @Component decorator to define metadata about the component.
@Component({
  selector: 'app-list-albums', // The name of the HTML element that will represent this component.
  templateUrl: './list-albums.component.html', // The HTML template file for the component.
  styleUrl: './list-albums.component.css' // The CSS styles file for the component.
})
// The ListAlbumsComponent class which will handle the display of a list of albums.
// It implements the OnInit interface to hook into the Angular component initialization lifecycle.
export class ListAlbumsComponent implements OnInit {

  // @Input decorator marks 'artist' as an input property, which can be set by the parent component.
  // It is expected to hold the Artist data for which albums are to be displayed.
  @Input() artist?: Artist;

  // An array of Album type to store the list of albums received from the music service.
  // The exclamation mark (!) indicates that the property will be definitely assigned.
  albums!: Album[];

  // A property to hold the currently selected album. It is initially set to null.
  selectedAlbum: Album | null = null;

  // The constructor for this component with dependency injection of the MusicServiceService.
  constructor(private service: MusicServiceService) {}

  // ngOnInit is a lifecycle hook that gets called after Angular has initialized the component.
  // This is where we fetch the albums for the given artist.
  ngOnInit() {
    // A call is made to the service to retrieve albums for the specified artist.
    // A callback function is provided to handle the response from the service.
    this.service.getAlbumsOfArtist((albums: Album[]) => {
      this.albums = albums; // The response (array of albums) is assigned to the component's albums property.
    }, this.artist!.artist); // The artist name is passed to the service method using the non-null assertion (!) as we expect it to be provided by the parent component.
  }

  // onSelectAlbum is a method to handle the logic when an album is selected from the list.
  // It receives an Album object which is the album that was selected.
  public onSelectAlbum(album: Album) {
    this.selectedAlbum = album; // The selectedAlbum property is set to the album that was clicked.
  }

}
