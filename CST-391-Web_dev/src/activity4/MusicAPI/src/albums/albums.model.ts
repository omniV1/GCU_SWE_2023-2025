import { Track } from '../tracks/tracks.model'; // Importing the Track interface from another file

// Definition of the Album interface
export interface Album {
    albumId: number; // ID of the album
    title: string; // Title of the album
    artist: string; // Name of the artist
    description: string; // Description of the album
    year: string; // Year of release
    image: string; // Image URL of the album cover
    tracks: Track[]; // Array of Track objects representing the tracks in the album
}
