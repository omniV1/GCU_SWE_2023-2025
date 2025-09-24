// Core Angular imports for component creation and lifecycle hooks
import { Component, OnInit } from '@angular/core';
// ActivatedRoute is used to access route parameters, in this case, potentially to filter or sort the artist list based on URL query parameters.
import { ActivatedRoute } from '@angular/router';
// Importing a custom service that handles fetching artist data.
import { MusicServiceService } from '../service/music-service.service';

// Importing the Artist model to strongly type the artist data used within the component.
import { Artist } from '../models/Artist';

// Component decorator defining metadata for this Angular component
@Component({
	selector: 'app-list-artists', // The custom HTML tag that will be used to represent this component.
	templateUrl: './list-artists.component.html', // The path to the HTML template file for the component.
	styleUrls: ['./list-artists.component.css'] // The path(s) to the CSS styles for this component.
})
// Class definition for the ListArtistsComponent, implementing OnInit to hook into the component initialization process.
export class ListArtistsComponent implements OnInit {
	// An array to store the list of artists fetched from the service.
	artists: Artist[] = [];
	// A property to track the currently selected artist.
	selectedArtist: Artist | null = null;

	// The class constructor, injecting the ActivatedRoute and MusicServiceService for later use.
	constructor(private route: ActivatedRoute, private service: MusicServiceService) { }

	// ngOnInit is a lifecycle hook called by Angular to indicate the component is about to be rendered.
	// This is often used for component initialization, such as fetching data.
	ngOnInit() {
		// Subscribing to queryParams allows the component to react to changes in query parameters in the URL.
		this.route.queryParams.subscribe(params => {
			console.log("Getting data...");
			// Fetches the list of artists from the service and assigns it to the component's artists property.
			this.artists = this.service.getArtists();
			// Resets the selected artist to null whenever the query parameters change.
			this.selectedArtist = null;
		});
	}

	// A public method for handling the selection of an artist from the list.
	// It logs the selected artist's name and updates the selectedArtist property.
	public onSelectArtist(artist: Artist) {
		console.log("Selected Artist of " + artist.Name);
		this.selectedArtist = artist;
	}
}
