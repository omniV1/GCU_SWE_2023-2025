import { Track } from "./Track"; // Importing the Track class

export class Album {
  private id: number = -1; // ID of the album, initialized to -1
  private title: string = ""; // Title of the album, initialized to an empty string
  private artist: string = ""; // Artist of the album, initialized to an empty string
  private description: string = ""; // Description of the album, initialized to an empty string
  private year: number = 1900; // Year of the album, initialized to 1900
  private image: string = ""; // Image filename of the album, initialized to an empty string
  private tracks: Track[] = []; // Array of tracks associated with the album, initialized to an empty array

  // Constructor function to create an instance of Album
  constructor(
    id: number,
    title: string,
    artist: string,
    description: string,
    year: number,
    image: string,
    tracks: Track[]
  ) {
    // Assigning values passed to the constructor to respective properties
    this.id = id;
    this.title = title;
    this.artist = artist;
    this.description = description;
    this.year = year;
    this.image = image;
    this.tracks = tracks;
  }

  // Getter and setter methods for the ID property
  get Id(): number {
    return this.id;
  }
  set Id(id: number) {
    this.id = id;
  }

  // Getter and setter methods for the Title property
  get Title(): string {
    return this.title;
  }
  set Title(title: string) {
    this.title = title;
  }

  // Getter and setter methods for the Artist property
  get Artist(): string {
    return this.artist;
  }
  set Artist(artist: string) {
    this.artist = artist;
  }

  // Getter and setter methods for the Description property
  get Description(): string {
    return this.description;
  }
  set Description(description: string) {
    this.description = description;
  }
  
  // Getter and setter methods for the Year property
  get Year(): number {
    return this.year;
  }
  set Year(year: number) {
    this.year = year;
  }

  // Getter and setter methods for the Image property
  public get Image(): string {
    return this.image;
  }
  public set Image(value: string) {
    this.image = value;
  }

  // Getter and setter methods for the Tracks property
  get Tracks(): Track[] {
    return this.tracks;
  }
  set Tracks(tracks: Track[]) {
    this.tracks = tracks;
  }
}
