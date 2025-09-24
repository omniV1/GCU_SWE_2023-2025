/**
 * Track class representing a music track.
 */
export class Track {
    private id: number = -1; // Track ID
    private number: number = 0; // Track number
    private title: string = ""; // Track title
    private lyrics: string = ""; // Track lyrics
    private video: string = ""; // Track video URL

    /**
     * Constructor to create a new Track instance.
     * @param id Track ID
     * @param number Track number
     * @param title Track title
     * @param lyrics Track lyrics
     * @param video Track video URL
     */
    constructor(id: number, number: number, title: string, lyrics: string, video: string) {
        this.id = id;
        this.number = number;
        this.title = title;
        this.lyrics = lyrics;
        this.video = video;
    }

    /**
     * Getter method for retrieving the track ID.
     */
    get Id(): number {
        return this.id;
    }

    /**
     * Setter method for setting the track ID.
     */
    set Id(id: number) {
        this.id = id;
    }

    /**
     * Getter method for retrieving the track number.
     */
    get Number(): number {
        return this.number;
    }

    /**
     * Setter method for setting the track number.
     */
    set Number(number: number) {
        this.number = number;
    }

    /**
     * Getter method for retrieving the track title.
     */
    get Title(): string {
        return this.title;
    }

    /**
     * Setter method for setting the track title.
     */
    set Title(title: string) {
        this.title = title;
    }

    /**
     * Getter method for retrieving the track lyrics.
     */
    get Lyrics(): string {
        return this.lyrics;
    }

    /**
     * Setter method for setting the track lyrics.
     */
    set Lyrics(lyrics: string) {
        this.lyrics = lyrics;
    }

    /**
     * Getter method for retrieving the track video URL.
     */
    public get Video(): string {
        return this.video;
    }

    /**
     * Setter method for setting the track video URL.
     */
    public set Video(value: string) {
        this.video = value;
    }
}
