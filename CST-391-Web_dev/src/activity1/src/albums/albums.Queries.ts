export const albumQueries = 
{
    readAlbums: 
    `SELECT
     id as albumId,
     title,
     artist,
     year,
     image,
     description,
     notes
     FROM
     music.albums`, 
    
     readAlbumsByArtist: 
     `SELECT
     id as albumId,
     title,
     artist,
     year,
     image,
     description,
     notes
     FROM
     music.albums
     WHERE
     artist = ?`, 
     
     readAlbumsByArtistSearch: 
     `
     SELECT
     id as albumId,
     title,
     artist,
     year,
     image,
     description,
     notes
     FROM
     music.albums
     WHERE
     LOWER(artist) LIKE LOWER(?)`,
    
    readAlbumsByDescriptionSearch:
    `SELECT
    id as albumId,
    title,
    artist,
    year,
    image,
    description,
    notes
    FROM
    music.albums
    WHERE
    music.albums.description LIKE ?`,

    readAlbumsByAlbumId: 
    `SELECT
    id as albumId,
    title,
    artist,
    year,
    image,
    description,
    notes
    FROM
    music.albums
    WHERE
    music.albums.id = ?`,

    createAlbum: 
    `INSERT INTO 
    albums(title, artist, year, image, description, notes) 
    VALUES (?,?,?,?,?,?)`,
   
    updateAlbum: 
    `UPDATE music.albums
    SET title = ?, artist = ?, year = ?, image = ?, description = ?, notes = ?
    WHERE id = ?`,

    deleteAlbum: 
    `DELETE FROM music.albums
    WHERE id = ?`,
}