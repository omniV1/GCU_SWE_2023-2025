import { execute } from "../services/mysql.connector";
import { Track } from "./tracks.model";
import { trackQueries } from './tracks.queries';

// Function to read tracks for a given album ID from the database
export const readTracks = async (albumId: number) => {
    return execute<Track[]>(trackQueries.readTracks, [albumId]);
};

// Function to create a new track in the database for a given album ID
export const createTrack = async (track: Track, index: number, albumId: number) => {
    return execute<Track[]>(trackQueries.createTrack,
        [albumId, track.title, track.number, track.video, track.lyrics]);
};

// Function to update an existing track in the database
export const updateTrack = async (track: Track) => {
    return execute<Track[]>(trackQueries.updateTrack,
        [track.title, track.number, track.video, track.lyrics, track.trackId]);
};
