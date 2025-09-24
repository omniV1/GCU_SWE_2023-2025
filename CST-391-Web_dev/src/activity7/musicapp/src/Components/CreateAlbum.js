import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

/**
 * CreateAlbum component allows users to create a new album by providing album details and adding tracks.
 * 
 * @component
 * @example
 * return (
 *   <CreateAlbum />
 * )
 * 
 * @returns {JSX.Element} The rendered CreateAlbum component.
 * 
 * @function
 * @name CreateAlbum
 * 
 * @description
 * This component provides a form for users to input album details such as title, artist, year released, image URL, and description.
 * Users can also add multiple tracks to the album by providing track title, lyrics, and video URL.
 * 
 * @property {function} useNavigate - Hook from react-router-dom to navigate programmatically.
 * @property {object} albumData - State object containing album details.
 * @property {string} albumData.title - Title of the album.
 * @property {string} albumData.artist - Artist of the album.
 * @property {string} albumData.description - Description of the album.
 * @property {string} albumData.yearReleased - Year the album was released.
 * @property {string} albumData.imageUrl - URL of the album cover image.
 * @property {Array} albumData.tracks - Array of tracks in the album.
 * @property {object} newTrack - State object containing details of a new track being added.
 * @property {string} newTrack.title - Title of the new track.
 * @property {string} newTrack.lyrics - Lyrics of the new track.
 * @property {string} newTrack.videoUrl - Video URL of the new track.
 * 
 * @method handleInputChange
 * @description Handles input changes for album details and updates the albumData state.
 * @param {object} e - Event object from the input change.
 * 
 * @method handleAddTrack
 * @description Adds a new track to the albumData state if the track title is provided.
 * 
 * @method handleSubmit
 * @description Handles form submission to create a new album by sending a POST request to the server.
 * @param {object} e - Event object from the form submission.
 * 
 * @throws Will throw an error if the POST request to create a new album fails.
 */
const CreateAlbum = () => {
  const navigate = useNavigate();
  const [albumData, setAlbumData] = useState({
    title: '',
    artist: '',
    description: '',
    yearReleased: '',
    imageUrl: '',
    tracks: []
  });

  const [newTrack, setNewTrack] = useState({
    title: '',
    lyrics: '',
    videoUrl: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setAlbumData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleAddTrack = () => {
    if (newTrack.title) {
      setAlbumData(prev => ({
        ...prev,
        tracks: [...prev.tracks, { ...newTrack, id: Date.now() }]
      }));
      setNewTrack({ title: '', lyrics: '', videoUrl: '' });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:3001/api/albums', albumData);
      navigate('/');
    } catch (error) {
      console.error('Error creating album:', error);
    }
  };

  return (
    <div className="container mt-4">
      <h2>Create New Album</h2>
      <form onSubmit={handleSubmit}>
        <div className="row">
          <div className="col-md-6">
            <div className="mb-3">
              <label className="form-label">Title</label>
              <input
                type="text"
                className="form-control"
                name="title"
                value={albumData.title}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Artist</label>
              <input
                type="text"
                className="form-control"
                name="artist"
                value={albumData.artist}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Year Released</label>
              <input
                type="number"
                className="form-control"
                name="yearReleased"
                value={albumData.yearReleased}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Image URL</label>
              <input
                type="url"
                className="form-control"
                name="imageUrl"
                value={albumData.imageUrl}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Description</label>
              <textarea
                className="form-control"
                name="description"
                value={albumData.description}
                onChange={handleInputChange}
                rows="3"
                required
              />
            </div>
          </div>
          
          <div className="col-md-6">
            <h3>Add Tracks</h3>
            <div className="mb-3">
              <label className="form-label">Track Title</label>
              <input
                type="text"
                className="form-control"
                value={newTrack.title}
                onChange={e => setNewTrack(prev => ({ ...prev, title: e.target.value }))}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Lyrics</label>
              <textarea
                className="form-control"
                value={newTrack.lyrics}
                onChange={e => setNewTrack(prev => ({ ...prev, lyrics: e.target.value }))}
                rows="3"
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Video URL</label>
              <input
                type="url"
                className="form-control"
                value={newTrack.videoUrl}
                onChange={e => setNewTrack(prev => ({ ...prev, videoUrl: e.target.value }))}
              />
            </div>
            <button 
              type="button" 
              className="btn btn-secondary mb-3"
              onClick={handleAddTrack}
            >
              Add Track
            </button>

            <div className="track-list">
              <h4>Added Tracks:</h4>
              <ul className="list-group">
                {albumData.tracks.map(track => (
                  <li key={track.id} className="list-group-item">
                    {track.title}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        <div className="mt-4">
          <button type="submit" className="btn btn-primary me-2">Create Album</button>
          <button 
            type="button" 
            className="btn btn-secondary"
            onClick={() => navigate('/')}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateAlbum;