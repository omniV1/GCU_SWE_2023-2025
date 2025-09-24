import { OkPacket } from "mysql";
import { execute } from "../services/mysql.connector";
import { Album } from "./albums.model";
import { albumQueries } from './albums.queries';

/**
 * Reads all albums.
 * @returns Promise resolving to an array of albums.
 */
export const readAlbums = async () => {
    return execute<Album[]>(albumQueries.readAlbums, []);
};

/**
 * Reads albums by artist name.
 * @param artistName The name of the artist.
 * @returns Promise resolving to an array of albums.
 */
export const readAlbumsByArtist = async (artistName: string) => {
    return execute<Album[]>(albumQueries.readAlbumsByArtist, [artistName]);
};

/**
 * Reads albums by artist name search.
 * @param search The search query for artist name.
 * @returns Promise resolving to an array of albums.
 */
export const readAlbumsByArtistSearch = async (search: string) => {
    console.log('search param', search);
    return execute<Album[]>(albumQueries.readAlbumsByArtistSearch, [search]);
};

/**
 * Reads albums by description search.
 * @param search The search query for album description.
 * @returns Promise resolving to an array of albums.
 */
export const readAlbumsByDescriptionSearch = async (search: string) => {
    console.log('search param', search);
    return execute<Album[]>(albumQueries.readAlbumsByDescriptionSearch, [search]);
};

/**
 * Reads albums by album ID.
 * @param albumId The ID of the album.
 * @returns Promise resolving to an array of albums.
 */
export const readAlbumsByAlbumId = async (albumId: number) => {
    return execute<Album[]>(albumQueries.readAlbumsByAlbumId, [albumId]);
};

/**
 * Creates a new album.
 * @param album The album object to be created.
 * @returns Promise resolving to a MySQL OkPacket.
 */
export const createAlbum = async (album: Album) => {
    return execute<OkPacket>(albumQueries.createAlbum,
        [album.title, album.artist, album.description, album.year, album.image]);
};

/**
 * Updates an existing album.

 */
export const updateAlbum = async (album: Album) => {
    return execute<OkPacket>(albumQueries.updateAlbum,
        [album.title, album.artist, album.year, album.image, album.description, album.albumId]);
};

/**
 * Deletes an album by its ID.
 * @param albumId The ID of the album to be deleted.
 * @returns Promise resolving to a MySQL OkPacket.
 */
export const deleteAlbum = async (albumId: number) => {
    return execute<OkPacket>(albumQueries.deleteAlbum, [albumId]);
};
