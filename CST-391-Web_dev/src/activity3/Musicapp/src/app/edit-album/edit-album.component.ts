// Import statements to include Angular core functionalities, the service for music data retrieval, and model classes.
import { Component, OnInit, Input } from '@angular/core';
import { MusicServiceService } from '../service/music-service.service';
import { Album } from '../models/Album';
import { Artist } from '../models/Artist';

@Component({
	selector: 'app-edit-album',
	templateUrl: './edit-album.component.html',
	styleUrls: ['./edit-album.component.css']
  })
export class EditAlbumComponent implements OnInit {
	ngOnInit(): void {
		throw new Error('Method not implemented.');
	}

}
