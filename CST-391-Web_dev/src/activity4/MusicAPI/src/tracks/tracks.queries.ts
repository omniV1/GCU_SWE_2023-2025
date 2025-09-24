/**
 * Contains SQL queries related to tracks.
 */
export const trackQueries = {
    /**
     * SQL query to insert a new track into the database.
     */
    createTrack:
        `insert into tracks (album_id, title, number, video_url) VALUES(?,?,?,?)`,
    
    /**
     * SQL query to read tracks associated with a specific album from the database.
     */
    readTracks:
        `select title as title, video_url as video, lyrics as lyrics from music.tracks where album_id = ?`,
    
    /**
     * SQL query to update an existing track in the database.
     */
    updateTrack:
        `update music.tracks set title =?, number = ?, video_url = ?, lyrics = ? where id = ?;`
};
