import { Request, RequestHandler, Response } from "express";
import * as ArtistDao from './artist.dao';

export const readArtists: RequestHandler = async (req: Request, res: Response) => {
    try {
        const artist = await ArtistDao.readArtist();
        res.status(200).json(artist);
    } catch (error) {
        console.error('[artists.controller][readArtists][Error]', error);
        res.status(500).json({
            message: 'There was an error when fetching artists'
        });
    }
};