import { execute } from "../services/mysql.connector";
import { Artist } from "./artists.model";
import { artistQueries } from './artists.queries';

/**
 * Asynchronously reads all artists from the database.
 * @returns A promise that resolves to an array of Artist objects.
 */
export const readArtists = async (): Promise<Artist[]> => {
    try {
        // Execute the query to read all artists from the database
        const artists = await execute<Artist[]>(artistQueries.readArtists, []);

        // Return the retrieved artists
        return artists;
    } catch (error) {
        // Handle any errors that occur during the process
        console.error('[artists.dao][readArtists][Error]', error);
        throw error; // Re-throw the error to be handled by the caller
    }
};
