// Core Angular imports for component creation and initialization.
import { Component, OnInit } from '@angular/core';
// ActivatedRoute is used to interact with the route parameters.
import { ActivatedRoute } from '@angular/router';
// Importing the MusicServiceService which will provide artist data.
import { MusicServiceService } from '../service/music-service.service';
// Importing the Artist model to define the structure of artist data.
import { Artist } from '../models/artists.model';

// Component decorator to define metadata for ListArtistsComponent.
@Component({
  selector: 'app-list-artists', // Defines the HTML tag for this component.
  templateUrl: './list-artists.component.html', // Points to the HTML template for the component.
  styleUrls: ['./list-artists.component.css'] // Points to the CSS styles for this component.
})
// Component class that will be instantiated when the app-list-artists tag is used.
export class ListArtistsComponent implements OnInit {

  // Class constructor with private members for the ActivatedRoute and MusicServiceService injected.
  constructor(private route: ActivatedRoute, private service: MusicServiceService) {}

  // Property to hold the currently selected artist.
  selectedArtist: Artist | null = null;

  // Property to hold the list of artists fetched from the service.
  artists: Artist[] = [];

  // ngOnInit is an Angular lifecycle hook that gets called once the component is initialized.
  ngOnInit() {
    // Fetch the list of artists from the service.
    this.service.getArtists((artists: Artist[]) => {
      this.artists = artists; // Store the fetched artists in the component's property.
      // Output the list of artists to the console for debugging purposes.
      console.log("this.artists", this.artists);
    });
  }

  // Method that gets called when an artist is selected by the user.
  onSelectArtist(artist: Artist) {
    this.selectedArtist = artist; // Update the selectedArtist property with the chosen artist.
  }
}
