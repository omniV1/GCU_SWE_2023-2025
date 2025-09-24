// Defines the Track class which models the concept of a musical track.
export class Track {
    // Private properties to hold track details. Access to these properties is controlled through getters and setters.
    private id: number = -1; // A unique identifier for the track. Initialized to -1 as a default value.
    private number: number = 0; // The track number in an album. Initialized to 0 as a default value.
    private title: string = ""; // The title of the track. Initialized to an empty string.
    private lyrics: string = ""; // The lyrics of the track. Initialized to an empty string.
    private video: string = ""; // A URL or identifier for a video associated with the track. Initialized to an empty string.

    // The constructor initializes a new instance of the Track class with the specified details.
    constructor(id: number, number: number, title: string, lyrics: string, video: string) {
        this.id = id; // Sets the track's id.
        this.number = number; // Sets the track number.
        this.title = title; // Sets the track title.
        this.lyrics = lyrics; // Sets the track lyrics.
        this.video = video; // Sets the video associated with the track.
    }

    // Getter for the track's id.
    get Id(): number {
        return this.id;
    }
    // Setter for the track's id. Allows updating the track's id.
    set Id(id: number) {
        this.id = id;
    }

    // Getter for the track number.
    get Number(): number {
        return this.number;
    }
    // Setter for the track number. Allows updating the track number.
    set Number(number: number) {
        this.number = number;
    }

    // Getter for the track title.
    get Title(): string {
        return this.title;
    }
    // Setter for the track title. Allows updating the track title.
    set Title(title: string) {
        this.title = title;
    }

    // Getter for the track lyrics.
    get Lyrics(): string {
        return this.lyrics;
    }
    // Setter for the track lyrics. Allows updating the track lyrics.
    set Lyrics(lyrics: string) {
        this.lyrics = lyrics;
    }

    // Getter for the video associated with the track.
    public get Video(): string {
        return this.video;
    }
    // Setter for the video associated with the track. Allows updating the video information.
    public set Video(value: string) {
        this.video = value;
    }
}
