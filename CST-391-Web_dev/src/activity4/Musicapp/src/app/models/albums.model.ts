import { Track } from './tracks.model'; // Importing the Track interface

// Album interface representing the structure of an album
export interface Album {
    albumId: number; // ID of the album
    title: string; // Title of the album
    artist: string; // Artist of the album
    description: string; // Description of the album
    year: string; // Year of the album
    image: string; // Image filename of the album
    tracks: Track[]; // Array of tracks associated with the album
}
