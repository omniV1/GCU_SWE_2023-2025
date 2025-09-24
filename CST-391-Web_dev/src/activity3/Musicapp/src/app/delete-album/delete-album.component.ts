// Angular core imports for component definition and lifecycle hooks.
import { Component, OnInit } from '@angular/core';
// Imports for handling routing within the Angular application.
import { ActivatedRoute, Router } from '@angular/router';
// Custom service for music data operations.
import { MusicServiceService } from '../service/music-service.service';

@Component({
  selector: 'app-delete-album', // The custom element tag to represent this component in HTML.
  templateUrl: './delete-album.component.html', // The HTML template file associated with this component.
  styleUrls: ['./delete-album.component.css'] // The CSS styles specific to this component.
})
export class DeleteAlbumComponent implements OnInit {
  // Flags to track the state of the deletion process.
  isDeleting: boolean = false; // Indicates if the deletion process is currently happening.
  isDeleted: boolean = false; // Indicates if the album has been successfully deleted.
  deleteError: boolean = false; // Indicates if there was an error during the deletion process.

  // Injecting necessary services via the constructor.
  constructor(
    private route: ActivatedRoute, // To access route parameters.
    private musicService: MusicServiceService, // To call deletion logic on the music service.
    private router: Router // To navigate to another route upon successful deletion.
  ) { }

  ngOnInit() {
    // Retrieving the 'artist' and 'id' from the route parameters.
    const artist = this.route.snapshot.paramMap.get('artist');
    const id = Number(this.route.snapshot.paramMap.get('id'));

    // Ensures that both 'artist' and 'id' are present before proceeding with deletion.
    if (artist && id) {
      this.deleteAlbum(id, artist);
    }
  }

  // Method to handle the deletion of an album.
  deleteAlbum(id: number, artist: string) {
    this.isDeleting = true; // Marks the beginning of the deletion process.
    // Calls the musicService to delete the album by its id and artist.
    const result = this.musicService.deleteAlbum(id, artist);
    // Once the service call is complete, update the deletion status flags accordingly.
    this.isDeleting = false; // Marks the end of the deletion process.
    
    if (result === 0) {
      // If the album was successfully deleted, set the flag and log a success message.
      this.isDeleted = true;
      console.log('Album successfully deleted');
      // After a delay, navigate to the list-albums page.
      setTimeout(() => this.router.navigate(['/list-albums']), 2000);
    } else {
      // If deletion failed, set the error flag and log an error message.
      this.deleteError = true;
      console.log('Error deleting album');
    }
  }
}
