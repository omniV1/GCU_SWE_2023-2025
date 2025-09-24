import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MusicServiceService } from '../service/music-service.service';
import { Album } from '../models/albums.model';

@Component({
  selector: 'app-delete-album',
  templateUrl: './delete-album.component.html',
  styleUrls: ['./delete-album.component.css']
})
export class DeleteAlbumComponent implements OnInit {
  album?: Album;
  wasDeleted: boolean = false;
  
  constructor(
    private route: ActivatedRoute,
    private service: MusicServiceService,
    private router: Router
  ) { }

  ngOnInit() {
    // Get the album ID from the route parameters
    const id = Number(this.route.snapshot.paramMap.get('id'));
    
    // Fetch the album data to show confirmation details
    this.service.getAlbumById(id, (albums: Album[]) => {
      if (albums && albums.length > 0) {
        this.album = albums[0];
      }
    });
  }

  onConfirmDelete() {
    if (this.album) {
      this.service.deleteAlbum(this.album.albumId, () => {
        this.wasDeleted = true;
        // Navigate back to the album list after a short delay
        setTimeout(() => {
          this.router.navigate(['/list-artists']);
        }, 1500);
      });
    }
  }

  onCancel() {
    // Navigate back to the previous page
    window.history.back();
  }
}