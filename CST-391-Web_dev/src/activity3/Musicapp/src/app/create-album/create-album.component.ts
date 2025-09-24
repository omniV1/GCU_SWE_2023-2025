// Core Angular imports for component functionality
import { Component, OnInit } from '@angular/core';
// Importing model classes for strong typing and structure
import { Album } from '../models/Album';
import { Track } from '../models/Track';
// Importing a service that handles data operations for music albums
import { MusicServiceService } from '../service/music-service.service';

@Component({
	selector: 'app-create-album', // Defines the custom HTML tag for this component.
	templateUrl: './create-album.component.html', // Specifies the HTML template for the component.
	styleUrls: ['./create-album.component.css'], // Specifies the CSS styles for the component.
})
export class CreateAlbumComponent implements OnInit {
	// Initializing a new Album object to collect user input from the form.
	// A random ID is generated to uniquely identify the new album.
	album: Album = new Album(Math.floor(Math.random() * 1000000), '', '', '', 0, '', []);

	// Holds the user input for tracks in a raw string format before parsing.
	tracksRaw: string = '';

	// Flag to indicate whether the album submission form has been submitted.
	wasSubmitted: boolean = false;

	// Injecting the music service to handle album creation.
	constructor(private service: MusicServiceService) { }

	// Lifecycle hook for initialization. No specific actions are performed on component initialization in this case.
	ngOnInit() { }

	// Handles the submission of the album creation form.
	public onSubmit() {
		// Parses the raw track data from the form into an array of Track objects.
		const tracks: Track[] = this.parseTracks(this.tracksRaw);

		// Assigns the parsed tracks to the album's Tracks property.
		this.album.Tracks = tracks;

		// Uses the injected service to create the album with the provided data.
		const status = this.service.createAlbum(this.album);

		// Logs the result of the album creation operation.
		console.log('The return from createAlbum() was ' + status);

		// Sets the submission flag to true, which can be used to show feedback or navigate away.
		this.wasSubmitted = true;
	}

	// Parses a raw string of track data into an array of Track objects.
	private parseTracks(rawTracks: string): Track[] {
		const tracks: Track[] = [];
		// Splits the raw string into lines, each line representing a track.
		const lines = rawTracks.split('\n');

		// Iterates over each line, creating a new Track object from the data.
		lines.forEach((line, index) => {
			// Splits the line into components based on a delimiter (':') and assigns each to a variable.
			const [title, lyrics, video] = line.split(':');
			// Creates and adds a new Track object to the tracks array with a unique ID and the parsed data.
			tracks.push(new Track(Math.floor(Math.random() * 1000000), index + 1, title, lyrics || '', video || ''));
		});

		return tracks;
	}
}
