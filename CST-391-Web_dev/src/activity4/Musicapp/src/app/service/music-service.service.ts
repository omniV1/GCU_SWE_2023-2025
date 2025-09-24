import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Artist } from './../models/artists.model';
import { Album } from '../models/albums.model';

/**
 * The MusicServiceService class is responsible for fetching and manipulating music-related data.
 * It provides methods to interact with the backend API to perform CRUD operations on albums and artists.
 */
@Injectable({ providedIn: 'root' })
export class MusicServiceService {

  private readonly host = "http://localhost:5000"; // Base URL for the backend API

  constructor(private http: HttpClient) {}

  /**
   * Retrieves all artists data from the backend API.
   */
  public getArtists(callback: (artists: Artist[]) => void): void {
    this.http.get<Artist[]>(`${this.host}/artists`).subscribe((artists: Artist[]) => {
      callback(artists);
    });
  }

  /**
   * Retrieves all albums data from the backend API.
   */
  public getAlbums(callback: (albums: Album[]) => void): void  {
    this.http.get<Album[]>(`${this.host}/albums`).subscribe((albums: Album[]) => {
      callback(albums);
    });
  }

  /**
   * Retrieves albums of a specific artist from the backend API.
   */
  public getAlbumsOfArtist(callback: (albums: Album[]) => void, artistName: string): void {
    this.http.get<Album[]>(`${this.host}/albums/${artistName}`).subscribe((albums: Album[]) => {
      callback(albums);
    });
  }

  /**
   * Creates a new album by sending a POST request to the backend API.
   */
  public createAlbum(album: Album, callback: () => void): void {
    this.http.post<Album[]>(`${this.host}/albums/`, album).subscribe(() => {
      callback();
    });
  }

  /**
   * Updates an existing album by sending a PUT request to the backend API.
   */
  public updateAlbum(album: Album, callback: () => void): void {
    this.http.put<Album[]>(`${this.host}/albums/`, album).subscribe(() => {
      callback();
    });
  }

  /**
   * Deletes an album from the backend API based on the provided album ID.
   */
  public deleteAlbum(id: number, callback: () => void): void {
    this.http.delete(`${this.host}/albums/${id}`).subscribe(() => {
      callback();
    });
  }

  /**
   * Retrieves an album by its ID from the backend API.
   */
  public getAlbumById(id: number, callback: (albums: Album[]) => void): void {
    this.http.get<Album[]>(`${this.host}/albums?albumId=${id}`).subscribe((albums: Album[]) => {
      callback(albums);
    });
  }
}
