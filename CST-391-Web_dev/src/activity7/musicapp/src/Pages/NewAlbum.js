import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import dataSource from '../Services/dataSource';

/**
 * NewAlbum component allows users to create a new music album with tracks.
 * 
 * @component
 * @example
 * return (
 *   <NewAlbum />
 * )
 * 
 * @returns {JSX.Element} The NewAlbum component.
 * 
 * @description
 * This component provides a form to input album details such as title, artist, year released, image URL, and description.
 * It also allows users to add multiple tracks to the album, each with a track number, title, lyrics, and video URL.
 * 
 * @function
 * @name NewAlbum
 * 
 * @property {function} useNavigate - React Router hook for navigation.
 * @property {object} albumData - State object for storing album details.
 * @property {function} setAlbumData - Function to update albumData state.
 * @property {Array} tracks - State array for storing track details.
 * @property {function} setTracks - Function to update tracks state.
 * @property {object} newTrack - State object for storing new track details.
 * @property {function} setNewTrack - Function to update newTrack state.
 * @property {function} handleInputChange - Function to handle input changes for album data.
 * @property {function} handleAddTrack - Function to add a new track to the tracks state.
 * @property {function} handleSubmit - Function to handle form submission and create a new album.
 */
const NewAlbum = () => {
 const navigate = useNavigate();
 
 // State for album data
 const [albumData, setAlbumData] = useState({
   title: '',
   artist: '',
   description: '',
   yearReleased: '',
   imageUrl: ''
 });

 // State for tracks
 const [tracks, setTracks] = useState([]);
 
 // State for new track form
 const [newTrack, setNewTrack] = useState({
   title: '',
   number: '',
   lyrics: '',
   videoUrl: ''
 });

 // Handle input changes for album data
 const handleInputChange = (e) => {
   const { name, value } = e.target;
   setAlbumData(prev => ({
     ...prev,
     [name]: value
   }));
 };

 // Add a new track to the tracks state
 const handleAddTrack = () => {
   if (newTrack.title && newTrack.number) {
     setTracks(prev => [...prev, { ...newTrack }]);
     // Reset the new track form
     setNewTrack({
       title: '',
       number: '',
       lyrics: '',
       videoUrl: ''
     });
   }
 };

 // Handle form submission
 const handleSubmit = async (e) => {
   e.preventDefault();
   try {
     // Create the album using the dataSource
     const albumResponse = await dataSource.createAlbum({
       ...albumData,
       tracks
     });
     console.log('Album created:', albumResponse);
     // Navigate back to the home page
     navigate('/');
   } catch (error) {
     console.error('Error creating album:', error);
     // Log the full error object for debugging
     console.error('Error creating album:', error.toJSON());
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
              <label className="form-label">Track Number</label>
              <input
                type="number"
                className="form-control"
                value={newTrack.number}
                onChange={(e) => setNewTrack(prev => ({ ...prev, number: e.target.value }))}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Track Title</label>
              <input
                type="text"
                className="form-control"
                value={newTrack.title}
                onChange={(e) => setNewTrack(prev => ({ ...prev, title: e.target.value }))}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Lyrics</label>
              <textarea
                className="form-control"
                value={newTrack.lyrics}
                onChange={(e) => setNewTrack(prev => ({ ...prev, lyrics: e.target.value }))}
                rows="3"
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Video URL</label>
              <input
                type="url"
                className="form-control"
                value={newTrack.videoUrl}
                onChange={(e) => setNewTrack(prev => ({ ...prev, videoUrl: e.target.value }))}
              />
            </div>
            <button 
              type="button" 
              className="btn btn-secondary mb-3"
              onClick={handleAddTrack}
            >
              Add Track
            </button>

            {tracks.length > 0 && (
              <div className="mb-3">
                <h4>Added Tracks:</h4>
                <ul className="list-group">
                  {tracks.map((track, index) => (
                    <li key={index} className="list-group-item">
                      {track.number}. {track.title}
                    </li>
                  ))}
                </ul>
              </div>
            )}
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

export default NewAlbum;