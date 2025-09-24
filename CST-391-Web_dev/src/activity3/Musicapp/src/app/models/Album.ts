// Importing the Track class to use as the type for tracks within an album.
import { Track } from "./Track";

// Exporting the Album class to make it available for use elsewhere in the application.
export class Album {
    // Private properties for album details. Encapsulation is used to control access to these properties.
    private id: number = -1; // A unique identifier for the album, initialized to -1 as a placeholder value.
    private title: string = ""; // The title of the album, initialized with an empty string.
    private artist: string = ""; // The name of the artist or band, initialized with an empty string.
    private description: string = ""; // A description of the album, initialized with an empty string.
    private year: number = 1900; // The release year of the album, initialized to a default value of 1900.
    private image: string = ""; // A URL or path to the album's cover image, initialized with an empty string.
    private tracks: Track[] = []; // An array to hold the tracks of the album, initialized as an empty array.

    // The constructor for creating an instance of Album with specified details.
    constructor(id: number, title: string, artist: string, description: string, year: number, image: string, tracks: Track[]) {
        this.id = id;
        this.title = title;
        this.artist = artist;
        this.description = description;
        this.year = year;
        this.image = image;
        this.tracks = tracks; // Takes an array of Track instances.
    }

    // Getters and setters for each property provide controlled access to the private properties.
    get Id(): number {
        return this.id;
    }
    set Id(id: number) {
        this.id = id;
    }

    get Title(): string {
        return this.title;
    }
    set Title(title: string) {
        this.title = title;
    }

    get Artist(): string {
        return this.artist;
    }
    set Artist(artist: string) {
        this.artist = artist;
    }

    get Description(): string {
        return this.description;
    }
    set Description(description: string) {
        this.description = description;
    }

    get Year(): number {
        return this.year;
    }
    set Year(year: number) {
        // Validation or transformation logic could be added here.
        this.year = year;
    }

    public get Image(): string {
        return this.image;
    }
    public set Image(value: string) {
        this.image = value;
    }

    get Tracks(): Track[] {
        return this.tracks;
    }
    set Tracks(tracks: Track[]) {
        // Additional logic, such as validating the array of tracks, could be added here.
        this.tracks = tracks;
    }
}
