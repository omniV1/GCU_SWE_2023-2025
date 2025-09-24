export const trackQueries = 
{
    createTrack:
    `INSERT INTO tracks (album_id, title, number, video_url, lyrics) VALUES(?,?,?,?,?)`,

    readTracks:
    `SELECT id, title, number, video_url as video, lyrics
    FROM music.tracks
    WHERE album_id = ?`, 

    updateTrack:
    `UPDATE music.tracks
    SET title = ?, number = ?, video_url = ?, lyrics = ?
    WHERE id = ?`
}