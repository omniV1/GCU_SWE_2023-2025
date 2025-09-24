import { execute } from "../services/mysql.connector";
import { Artist } from "./artist.model";
import { artistQueries } from './artist.queries'; 

export const readArtist = async () => 
{
    return execute<Artist[]>(artistQueries.readArtist,[]);
}