import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MusicServiceService } from '../service/music-service.service';
import { Album } from '../models/albums.model';
import { Track } from '../models/tracks.model';

@Component({
  selector: 'app-edit-album',
  templateUrl: './edit-album.component.html',
  styleUrls: ['./edit-album.component.css']
})
export class EditAlbumComponent implements OnInit {
  album: Album = {
    albumId: 0,
    title: "",
    artist: "",
    description: "",
    year: "",
    image: "",
    tracks: []
  };

  tracksRaw: string = "";
  wasSubmitted: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private service: MusicServiceService,
    private router: Router
  ) {}

  ngOnInit() {
    // Get the album ID from the route parameters
    const id = Number(this.route.snapshot.paramMap.get('id'));
    
    // Fetch the album data
    this.service.getAlbumById(id, (albums: Album[]) => {
      if (albums && albums.length > 0) {
        this.album = albums[0];
        // Convert tracks to raw string format for editing
        this.tracksRaw = this.album.tracks
          .map(track => `${track.title}:${track.lyrics}:${track.video}`)
          .join('\n');
      }
    });
  }

  onSubmit() {
    // Parse tracks from raw text
    let tracks: Track[] = [];
    let tracksAll = this.tracksRaw.split('\n');
    
    for (let i = 0; i < tracksAll.length; ++i) {
      let trackParts = tracksAll[i].split(':');
      tracks.push({
        trackId: this.album.tracks[i]?.trackId || Math.floor(Math.random() * 1000000),
        number: i + 1,
        title: trackParts[0] || '',
        lyrics: trackParts[1] || '',
        video: trackParts[2] || ''
      });
    }
    
    this.album.tracks = tracks;

    // Update album
    this.service.updateAlbum(this.album, () => {
      this.wasSubmitted = true;
      // Navigate back to the album list after a short delay
      setTimeout(() => {
        this.router.navigate(['/list-artists']);
      }, 1500);
    });
  }
}