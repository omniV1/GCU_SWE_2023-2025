// Importing necessary types from the express package to handle HTTP request and response objects.
import { Request, RequestHandler, Response } from 'express';
// Importing Album and Track models for type definitions.
import { Album } from './albums.model';
import { Track } from './../tracks/tracks.model';
// Importing Data Access Objects (DAO) for albums and tracks to interact with the database.
import * as AlbumDao from '../albums/albums.dao';
import * as TracksDao from '../tracks/tracks.dao';
// Importing OkPacket from mysql, which represents the result of an insert or update operation.
import { OkPacket } from 'mysql';

// Handler for reading all albums or a specific album by its ID.
export const readAlbums: RequestHandler = async (req: Request, res: Response) => {
    try {
        let albums;
        // Attempt to parse albumId from query parameters, if provided.
        let albumId = parseInt(req.query.albumId as string);

        console.log('albumId', albumId);
        // If albumId is not a number (NaN), fetch all albums; otherwise, fetch the specified album.
        if (Number.isNaN(albumId)) {
            albums = await AlbumDao.readAlbums();
        } else {
            albums = await AlbumDao.readAlbumsByAlbumId(albumId);
        }
        // Enrich albums with their tracks.
        await readTracks(albums, res);
        // Respond with the albums data.
        res.status(200).json(albums);
    } catch (error) {
        // Log and respond with error information.
        console.error('[albums.controller][readAlbums][Error]', error);
        res.status(500).json({
            message: 'There was an error when fetching albums'
        });
    }
};

// Handler for reading albums filtered by artist.
export const readAlbumsByArtist: RequestHandler = async (req: Request, res: Response) => {
    try {
        // Fetch albums by artist using the artist parameter from the URL.
        const albums = await AlbumDao.readAlbumsByArtist(req.params.artist);
        // Enrich albums with their tracks.
        await readTracks(albums, res);

        res.status(200).json(albums);
    } catch (error) {
        console.error('[albums.controller][readAlbums][Error] ', error);
        res.status(500).json({
            message: 'There was an error when fetching albums'
        });
    }
};

// Handler for reading albums filtered by an artist search term.
export const readAlbumsByArtistSearch: RequestHandler = async (req: Request, res: Response) => {
    try {
        console.log('search', req.params.search);
        // Fetch albums by search term, using a wildcard search pattern.
        const albums = await AlbumDao.readAlbumsByArtistSearch('%' + req.params.search + '%');

        await readTracks(albums, res);

        res.status(200).json(albums);
    } catch (error) {
        console.error('[albums.controller][readAlbums][Error] ', error);
        res.status(500).json({
            message: 'There was an error when fetching albums'
        });
    }
};

// Handler for reading albums filtered by a description search term.
export const readAlbumsByDescriptionSearch: RequestHandler = async (req: Request, res: Response) => {
    try {
        console.log('search', req.params.search);
        // Fetch albums by description search term, using a wildcard search pattern.
        const albums = await AlbumDao.readAlbumsByDescriptionSearch('%' + req.params.search + '%');

        await readTracks(albums, res);

        res.status(200).json(albums);
    } catch (error) {
        console.error('[albums.controller][readAlbums][Error] ', error);
        res.status(500).json({
            message: 'There was an error when fetching albums'
        });
    }
};

// Handler for creating a new album with its tracks.
export const createAlbum: RequestHandler = async (req: Request, res: Response) => {
    try {
        // Create a new album using the request body.
        const okPacket: OkPacket = await AlbumDao.createAlbum(req.body);

        console.log('req.body', req.body);
        console.log('album', okPacket);

        // Iterate over each track in the request body and create them in the database.
        req.body.tracks.forEach(async (track: Track, index: number) => {
            try {
                await TracksDao.createTrack(track, index, okPacket.insertId);
            } catch (error) {
                console.error('[albums.controller][createAlbumTracks][Error] ', error);
                res.status(500).json({
                    message: 'There was an error when writing album tracks'
                });
            }
        });

        res.status(200).json(okPacket);
    } catch (error) {
        console.error('[albums.controller][createAlbum][Error] ', error);
        res.status(500).json({
            message: 'There was an error when writing albums'
        });
    }
};

// Handler for updating an existing album and its tracks.
export const updateAlbum: RequestHandler = async (req: Request, res: Response) => {
    try {
        // Update an album using the request body.
        const okPacket: OkPacket = await AlbumDao.updateAlbum(req.body);

        console.log('req.body', req.body);
        console.log('album', okPacket);

        // Iterate over each track in the request body and update them in the database.
        req.body.tracks.forEach(async (track: Track, index: number) => {
            try {
                await TracksDao.updateTrack(track);
            } catch (error) {
                console.error('[albums.controller][updateAlbum][Error] ', error);
                res.status(500).json({
                    message: 'There was an error when updating album tracks'
                });
            }
        });

        res.status(200).json(okPacket);
    } catch (error) {
        console.error('[albums.controller][updateAlbum][Error] ', error);
        res.status(500).json({
            message: 'There was an error when writing albums'
        });
    }
};

// Handler for deleting an album by its ID.
export const deleteAlbum: RequestHandler = async (req: Request, res: Response) => {
    try {
        // Parse albumId from the route parameters.
        let albumId = parseInt(req.params.albumId as string);
        console.log('albumId', albumId);

        // Ensure albumId is a valid number before attempting to delete.
        if (!Number.isNaN(albumId)) {
            const response = await AlbumDao.deleteAlbum(albumId);
            res.status(200).json(response);
        } else {
            throw new Error("Integer expected for albumId");
        }
    } catch (error) {
        console.error('[albums.controller][deleteAlbum][Error] ', error);
        res.status(500).json({
            message: 'There was an error when deleting albums'
        });
    }
};

// Utility function to read and attach tracks to each album in a list of albums.
async function readTracks(albums: Album[], res: Response<any, Record<string, any>>) {
    for (let i = 0; i < albums.length; i++) {
        try {
            // Fetch tracks for the current album and attach them to the album object.
            const tracks = await TracksDao.readTracks(albums[i].albumId);
            albums[i].tracks = tracks;
        } catch (error) {
            console.error('[albums.controller][readTracks][Error] ', error);
            res.status(500).json({
                message: 'There was an error when fetching albums tracks'
            });
        }
    }
};
