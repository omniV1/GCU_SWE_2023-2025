import { OkPacket } from "mysql";
import { execute } from "../services/mysql.connector";
import { Album} from "./albums.model";
import { albumQueries } from './albums.Queries'; 

export const readAlbums = async () => 
{
    return execute<Album[]>(albumQueries.readAlbums, []);
};

export const readAlbumsByArtist = async (artistName: string): Promise<Album[]> => {
    console.log('Searching for artist:', artistName);
    return execute<Album[]>(albumQueries.readAlbumsByArtist, [artistName]);
};

export const readAlbumsByArtistSearch = async (search: string): Promise<Album[]> => {
    const searchParam = `%${search}%`;
    console.log('search param', searchParam);
    return execute<Album[]>(albumQueries.readAlbumsByArtistSearch, [searchParam]);
};

export const readAlbumsByDescriptionSearch = async (search:string) => 
{
    console.log('search param', search);
    return execute<Album[]>(albumQueries.readAlbumsByDescriptionSearch, [search]);
};

export const readAlbumsByAlbumId = async (albumId : number) => 
{
    return execute<Album[]>(albumQueries.readAlbumsByAlbumId, [albumId]);
}; 

export const createAlbum = async (album: Album) => 
{
    return execute<OkPacket>(albumQueries.createAlbum,[album.title, album.artist, album.year, album.image, album.description, album.notes]);
}; 
export const updateAlbum = async (album: Album): Promise<OkPacket> => {
    return execute<OkPacket>(
        albumQueries.updateAlbum,
        [album.title, album.artist, album.year, album.image, album.description, album.albumId, album.notes]
    );
};
export const deleteAlbum = async (albumId : number) => 
{
    return execute<OkPacket>(albumQueries.deleteAlbum, [albumId]); 
}; 