// Core Angular decorators and interfaces are imported for component definition and lifecycle hooks.
import { Component, Input, OnInit } from '@angular/core';
// Album model is imported for strong typing and IntelliSense within the component.
import { Album } from '../models/albums.model';
// ActivatedRoute and Router are Angular services that allow you to work with route parameters and navigate programmatically.
import { ActivatedRoute, Router } from '@angular/router';
// MusicServiceService is a custom service that handles operations related to music data.
import { MusicServiceService } from '../service/music-service.service';

// The @Component decorator function is used to define metadata for the DisplayAlbumComponent.
@Component({
  selector: 'app-display-album', // The component's custom HTML selector.
  templateUrl: './display-album.component.html', // The path to the component's HTML template.
  styleUrl: './display-album.component.css' // The path to the component's CSS styles.
})
// DisplayAlbumComponent class definition. This class is not implementing OnInit, thus lifecycle hook related methods like ngOnInit are not used here.
export class DisplayAlbumComponent {
  // @Input decorator marks 'album' property as input-bound, so it can be set by a parent component.
  @Input() album?: Album;

  // Variable to keep track of the current route URL.
  currentRoute: string = '';

  // The constructor injects necessary services for later use.
  constructor(private route: ActivatedRoute, private service: MusicServiceService) {
    // Subscribe to the route parameters observable to react to parameter changes.
    this.route.params.subscribe(params => {
      // Parse the 'id' parameter from the route URL and log it.
      let albumId = parseInt(params['id']);
      console.log("albumId: " + albumId)
      // Make a service call to get the album by its 'id'. The actual service method seems to be commented out.
      // this.album = this.service.getAlbumById(albumId);

      // The service call is made, and upon getting the response, the album property is set.
      // There seems to be an issue here: the callback sets a local variable 'album' but doesn't assign it to this.album.
      this.service.getAlbumById(albumId, (album: Album[]) => {
        // Assuming this callback is supposed to set the component's album property.
        this.album = album[0]; // Corrected line: assign the first album from the response to this.album.
      });

      // Logging this.album to the console. Depending on asynchronous timing, this may log before the service call sets the album.
      console.log(this.album);
    });
  }
}
