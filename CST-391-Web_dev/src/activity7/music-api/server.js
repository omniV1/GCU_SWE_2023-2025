const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');
const app = express();

// Enable CORS for cross-origin requests and JSON parsing
// This is necessary for our React frontend to communicate with our server
app.use(cors());
app.use(express.json());

// Create MySQL connection pool for better performance
// The pool allows multiple connections to be maintained
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',  // replace with your MySQL username
  password: 'root', // replace with your MySQL password
  database: 'music_db'
});

// Convert pool query to promise to use async/await
// This makes our database queries cleaner and easier to handle
const promisePool = pool.promise();

// ===== READ Operations (GET endpoints) =====

// Get all albums
app.get('/api/albums', async (req, res) => {
  try {
    const [rows] = await promisePool.query('SELECT * FROM albums');
    res.json(rows);
  } catch (error) {
    console.error('Error fetching albums:', error);
    res.status(500).json({ error: 'Error fetching albums' });
  }
});

// Search albums - supports partial matching on title, artist, or description
app.get('/api/albums/search', async (req, res) => {
  try {
    const searchTerm = `%${req.query.term}%`;
    const [rows] = await promisePool.query(
      'SELECT * FROM albums WHERE title LIKE ? OR artist LIKE ? OR description LIKE ?',
      [searchTerm, searchTerm, searchTerm]
    );
    res.json(rows);
  } catch (error) {
    console.error('Error searching albums:', error);
    res.status(500).json({ error: 'Error searching albums' });
  }
});

// Get single album by ID
app.get('/api/albums/:id', async (req, res) => {
  try {
    const [rows] = await promisePool.query(
      'SELECT * FROM albums WHERE id = ?',
      [req.params.id]
    );
    if (rows.length > 0) {
      res.json(rows[0]);
    } else {
      res.status(404).json({ error: 'Album not found' });
    }
  } catch (error) {
    console.error('Error fetching album:', error);
    res.status(500).json({ error: 'Error fetching album' });
  }
});

// Get all tracks for a specific album
app.get('/api/albums/:id/tracks', async (req, res) => {
  try {
    const [rows] = await promisePool.query(
      'SELECT * FROM tracks WHERE albumId = ? ORDER BY number',
      [req.params.id]
    );
    res.json(rows);
  } catch (error) {
    console.error('Error fetching tracks:', error);
    res.status(500).json({ error: 'Error fetching tracks' });
  }
});

// Get single track by ID
app.get('/api/tracks/:id', async (req, res) => {
  try {
    const [rows] = await promisePool.query(
      'SELECT * FROM tracks WHERE id = ?',
      [req.params.id]
    );
    if (rows.length > 0) {
      res.json(rows[0]);
    } else {
      res.status(404).json({ error: 'Track not found' });
    }
  } catch (error) {
    console.error('Error fetching track:', error);
    res.status(500).json({ error: 'Error fetching track' });
  }
});

// ===== UPDATE Operations (PUT endpoints) =====

// Update album details
app.put('/api/albums/:id', async (req, res) => {
  try {
    console.log('Updating album:', {
      id: req.params.id,
      data: req.body
    });

    const result = await promisePool.query(
      'UPDATE albums SET title = ?, artist = ?, description = ?, yearReleased = ?, imageUrl = ? WHERE id = ?',
      [
        req.body.title,
        req.body.artist,
        req.body.description,
        req.body.yearReleased,
        req.body.imageUrl,
        req.params.id
      ]
    );

    if (result[0].affectedRows === 0) {
      return res.status(404).json({ error: 'Album not found' });
    }

    res.json({ message: 'Album updated successfully' });
  } catch (error) {
    console.error('Error updating album:', error);
    res.status(500).json({ error: 'Error updating album' });
  }
});

// Update album tracks - replaces all tracks for an album
app.put('/api/albums/:id/tracks', async (req, res) => {
  try {
    console.log('Updating tracks for album:', {
      albumId: req.params.id,
      trackCount: req.body.length
    });

    // Start a transaction to ensure data consistency
    await promisePool.query('START TRANSACTION');

    // Remove existing tracks
    await promisePool.query('DELETE FROM tracks WHERE albumId = ?', [req.params.id]);
    
    // Insert new tracks
    for (const track of req.body) {
      await promisePool.query(
        'INSERT INTO tracks (albumId, title, number, lyrics, video_url) VALUES (?, ?, ?, ?, ?)',
        [req.params.id, track.title, track.number, track.lyrics, track.video_url]
      );
    }
    
    // Commit the transaction
    await promisePool.query('COMMIT');
    
    res.json({ message: 'Tracks updated successfully' });
  } catch (error) {
    // Rollback changes if anything fails
    await promisePool.query('ROLLBACK');
    console.error('Error updating tracks:', error);
    res.status(500).json({ error: 'Error updating tracks' });
  }
});

// Update single track
app.put('/api/tracks/:id', async (req, res) => {
  try {
    const { title, number, lyrics, video_url } = req.body;
    const result = await promisePool.query(
      'UPDATE tracks SET title = ?, number = ?, lyrics = ?, video_url = ? WHERE id = ?',
      [title, number, lyrics, video_url, req.params.id]
    );

    if (result[0].affectedRows === 0) {
      return res.status(404).json({ error: 'Track not found' });
    }

    res.json({ message: 'Track updated successfully' });
  } catch (error) {
    console.error('Error updating track:', error);
    res.status(500).json({ error: 'Error updating track' });
  }
});

// POST create new album with tracks
app.post('/api/albums', async (req, res) => {
  try {
    const { title, artist, description, yearReleased, imageUrl, tracks } = req.body;
    
    // Insert new album
    const [result] = await promisePool.query(
      'INSERT INTO albums (title, artist, description, yearReleased, imageUrl) VALUES (?, ?, ?, ?, ?)',
      [title, artist, description, yearReleased, imageUrl]
    );
    
    const albumId = result.insertId;

    // Insert tracks 
    for (const track of tracks) {
      await promisePool.query(
        'INSERT INTO tracks (albumId, title, number, lyrics, video_url) VALUES (?, ?, ?, ?, ?)',
        [albumId, track.title, track.number, track.lyrics, track.video_url]
      );
    }
    
    res.status(201).json({ id: albumId });
  } catch (error) {
    console.error('Error creating album:', error);
    res.status(500).json({ error: 'Error creating album' });
  }
});

// Delete track
app.delete('/api/tracks/:id', async (req, res) => {
  try {
    const result = await promisePool.query('DELETE FROM tracks WHERE id = ?', [req.params.id]);
    
    if (result[0].affectedRows === 0) {
      return res.status(404).json({ error: 'Track not found' });
    }

    res.json({ message: 'Track deleted successfully' });
  } catch (error) {
    console.error('Error deleting track:', error);
    res.status(500).json({ error: 'Error deleting track' });
  }
});

// Start the server
const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log(`Ready to handle requests at http://localhost:${PORT}`);
});