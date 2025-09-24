import { Component, OnInit, Input } from '@angular/core';
import { MusicServiceService } from '../service/music-service.service';
import { Album } from '../models/Album';
import { Artist } from '../models/Artist';

// The @Component decorator indicates that the class is an Angular component,
// specifies the selector, template, and stylesheet for the component.
@Component({
	selector: 'app-list-albums', // The component's CSS element selector
	templateUrl: './list-albums.component.html', // The location of the template file for this component
	styleUrls: ['./list-albums.component.css'] // The location of the CSS styles for this component
})

// ListAlbumsComponent is responsible for displaying a list of albums for a selected artist.
export class ListAlbumsComponent implements OnInit {
	// @Input decorator to accept 'artist' from parent component.
	// It holds the currently selected artist object or null if no artist is selected.
	@Input() artist: Artist | null = null;

	// 'albums' holds the list of albums for the selected artist.
	albums: Album[] = [];

	// 'selectedAlbum' holds the currently selected album object or null if no album is selected.
	selectedAlbum: Album | null = null;

	// Injecting the MusicServiceService to access its methods for album data retrieval.
	constructor(private service: MusicServiceService) { }

	// ngOnInit lifecycle hook is called after Angular has initialized all data-bound properties.
	// Here, it uses the music service to load albums for the selected artist if an artist is selected.
	ngOnInit() {
		if (this.artist) {
			this.albums = this.service.getAlbums(this.artist.Name);
		}
	}

	// 'onSelectAlbum' is an event handler called when an album is selected.
	// It logs the selected album's title and updates the 'selectedAlbum' property.
	public onSelectAlbum(album: Album) {
		console.log("Selected Album of " + album.Title);
		this.selectedAlbum = album;
	}
}

