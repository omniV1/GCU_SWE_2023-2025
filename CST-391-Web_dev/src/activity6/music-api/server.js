const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');
const app = express();

// Enable CORS and JSON parsing
app.use(cors());
app.use(express.json());

// Create MySQL connection pool
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',  // replace with your MySQL username
  password: 'root', // replace with your MySQL password
  database: 'music_db'
});

// Convert pool query to promise to use async/await
const promisePool = pool.promise();

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

// Search albums
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

// Get album by ID
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

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});