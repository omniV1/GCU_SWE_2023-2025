import { Component, OnInit } from '@angular/core';
import { Album } from '../models/albums.model';
import { Track } from '../models/tracks.model';
import { MusicServiceService } from '../service/music-service.service';

@Component({
  selector: 'app-create-album',
  templateUrl: './create-album.component.html',
  styleUrls: ['./create-album.component.css']
})
export class CreateAlbumComponent implements OnInit {

  // Initialize album object with default values
  album: Album = {
    albumId: Math.floor(Math.random() * 1000000),
    title: "",
    artist: "",
    description: "",
    year: "",
    image: "",
    tracks: [],
  };

  // Raw input for tracks
  tracksRaw: string = "";

  // Flag to indicate if form was submitted
  wasSubmitted: boolean = false;

  constructor(private service: MusicServiceService) { }

  ngOnInit() {
  }

  // Function to handle form submission
  public onSubmit() {
    // Parse the Tracks and add to the Album then call the Service to create the new Album
    let tracks: Track[] = [];
    let tracksAll = this.tracksRaw.split('\n');
    for (let i = 0; i < tracksAll.length; ++i) {
      let title = "";
      let lyrics = "";
      let video = "";
      let trackInfo = tracksAll[i];
      let trackParts = trackInfo.split(':');
      // Check the number of parts in each track entry and assign values accordingly
      if (trackParts.length == 3) {
        title = trackParts[0];
        lyrics = trackParts[1];
        video = trackParts[2];
      }
      else if (trackParts.length == 2) {
        title = trackParts[0];
        lyrics = trackParts[1];
      }
      else {
        title = trackParts[0];
      }
      // Push the parsed track data into the tracks array
      tracks.push(
        { trackId: Math.floor(Math.random() * 1000000), number: i + 1, title, lyrics, video }
      );
    }
    // Assign the parsed tracks to the album object
    this.album.tracks = tracks;
    console.log(this.album);
    // Call the service method to create the new album
    this.service.createAlbum(this.album, () => {
      console.log("Created Album");
    });

    // Set flag to indicate form submission
    this.wasSubmitted = true;
  }
}
