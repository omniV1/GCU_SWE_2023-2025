import { Injectable } from '@angular/core';

import exampledata from '../../data/sample-music-data.json';

import { Album } from '../models/Album';
import { Artist } from '../models/Artist';
import { Track } from '../models/Track';

// The MusicService is responsible for handling music data operations.
// It communicates with the backend services to fetch and manipulate music data.
@Injectable({ providedIn: 'root' })
export class MusicServiceService {
	 // An array to store artist information.
	private readonly artists: Artist[] = [];
	 // An array to store album information.
	private readonly albums: Album[] = [];

	constructor() {
		this.createArtists();
		this.createAlbums();
	}
// Initializes the artists array with predefined data.
	private createArtists(): void {
		this.artists.push(new Artist(0, 'The Beatles'));
	}
 // Reads the example data and creates albums, only including albums by 'The Beatles'.
	private createAlbums(): void {
		exampledata.forEach((data: any) => {
			if (data.artist === 'The Beatles') {
				const tracks = data.tracks.map((trackData: any) => new Track(trackData.id, trackData.number, trackData.title, trackData.lyrics, trackData.video));
				const album = new Album(data.id, data.title, data.artist, data.description, data.year, data.image, tracks);
				this.albums.push(album);
			}
		});
	}
// Retrieves all artists.
	public getArtists(): Artist[] {
		return this.artists;
	}
// Retrieves all albums for a given artist.
	public getAlbums(artist: string): Album[] {
		return this.albums;
	}
// Retrieves a specific album by its artist and ID.
	public getAlbum(artist: string, id: number): Album | undefined {
		const album = this.albums.find((a) => a.Artist === artist && a.Id === id);

		if (album) {
			const tracks = album.Tracks.map((track) => new Track(track.Id, track.Number, track.Title, track.Lyrics, track.Video));
			return new Album(album.Id, album.Title, album.Artist, album.Description, album.Year, album.Image, tracks);
		}

		return undefined;
	}
// Adds a new album to the collection.
	public createAlbum(album: Album): void {
		this.albums.push(album);
	}
 // Updates an existing album's information.
	public updateAlbum(album: Album): void {
		const index = this.albums.findIndex((a) => a.Id === album.Id);

		if (index !== -1) {
			this.albums.splice(index, 1, album);
		}
	}
/// Deletes an album from the collection based on its ID and artist.
// Returns 0 if successful, -1 if the album is not found.
public deleteAlbum(id: number, artist: string): number {
	const index = this.albums.findIndex(a => a.Id === id && a.Artist === artist);
	if (index !== -1) {
	  // Remove the album from the albums array
	  this.albums.splice(index, 1);
	  return 0; // Indicate success
	}
	return -1; // Indicate failure
  }
  
	}