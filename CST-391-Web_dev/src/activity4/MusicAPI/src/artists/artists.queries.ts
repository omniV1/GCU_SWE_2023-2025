
export const artistQueries = {
    /**
     * SQL query to read distinct artist names from the albums table.
     */
    readArtists:
        `select distinct artist as artist from music.albums`
};
