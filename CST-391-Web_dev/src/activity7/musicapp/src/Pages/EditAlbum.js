import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

/**
 * EditAlbum component allows users to edit an existing album's details and its tracks.
 * 
 * @component
 * @example
 * return (
 *   <EditAlbum />
 * )
 * 
 * @returns {JSX.Element} The rendered EditAlbum component.
 * 
 * @description
 * This component fetches album and track data from the server when it mounts, and allows users to update the album's details and tracks.
 * Users can also add new tracks or delete existing ones. The form submission updates the album and tracks data on the server.
 * 
 * @function
 * @name EditAlbum
 * 
 * @requires useParams - To get the albumId from the URL.
 * @requires useNavigate - To navigate to different routes.
 * @requires useState - To manage component state.
 * @requires useEffect - To fetch data when the component mounts.
 * @requires axios - To make HTTP requests.
 * 
 * @returns {JSX.Element} The rendered EditAlbum component.
 */
const EditAlbum = () => {
  const { albumId } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  // Initialize album data state with empty values
  const [albumData, setAlbumData] = useState({
    title: '',
    artist: '',
    description: '',
    yearReleased: '',
    imageUrl: ''
  });
  const [tracks, setTracks] = useState([]);
  // Initialize new track form with empty values
  const [newTrack, setNewTrack] = useState({
    title: '',
    number: '',
    lyrics: '',
    video_url: ''
  });

  // Load album and track data when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const albumResponse = await axios.get(`http://localhost:3001/api/albums/${albumId}`);
        setAlbumData(albumResponse.data);
        
        const tracksResponse = await axios.get(`http://localhost:3001/api/albums/${albumId}/tracks`);
        setTracks(tracksResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    if (albumId) {
      fetchData();
    }
  }, [albumId]);

  // Handle changes to album form inputs
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setAlbumData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  // Handle changes to existing track fields
  const handleTrackChange = (index, field, value) => {
    const updatedTracks = [...tracks];
    updatedTracks[index] = {
      ...updatedTracks[index],
      [field]: value
    };
    setTracks(updatedTracks);
  };

  // Add a new track to the tracks list
  const handleAddTrack = () => {
    if (newTrack.title && newTrack.number) {
      setTracks([...tracks, { ...newTrack, albumId }]);
      // Reset the new track form
      setNewTrack({
        title: '',
        number: '',
        lyrics: '',
        video_url: ''
      });
    }
  };

  // Remove a track from the list
  const handleDeleteTrack = (index) => {
    setTracks(tracks.filter((_, i) => i !== index));
  };

  // Handle form submission - updated to use PUT endpoints
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log('Attempting to update album:', {
        albumId,
        albumData
      });

      // Update album details using PUT
      const albumResult = await axios.put(`http://localhost:3001/api/albums/${albumId}`, albumData);
      console.log('Album update response:', albumResult.data);

      console.log('Attempting to update tracks:', tracks);
      // Update all tracks in one call
      const tracksResult = await axios.put(`http://localhost:3001/api/albums/${albumId}/tracks`, tracks);
      console.log('Tracks update response:', tracksResult.data);

      navigate(`/album/${albumId}`);
    } catch (error) {
      console.error('Detailed error information:', {
        message: error.message,
        response: error.response?.data,
        status: error.response?.status,
        endpoint: `http://localhost:3001/api/albums/${albumId}`,
        sentData: albumData
      });
    }
  };
  
  // Show loading spinner while data is being fetched
  if (loading) {
    return <div className="text-center mt-5"><div className="spinner-border" /></div>;
  }

  return (
    <div className="container mt-4">
      <h2>Edit Album</h2>
      <form onSubmit={handleSubmit}>
        <div className="row">
          {/* Album Details Section */}
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

          {/* Tracks Section */}
          <div className="col-md-6">
            <h3>Tracks</h3>
            {/* Existing Tracks List */}
            {tracks.map((track, index) => (
              <div key={index} className="card mb-3">
                <div className="card-body">
                  <div className="row">
                    <div className="col-2">
                      <input
                        type="number"
                        className="form-control"
                        value={track.number}
                        onChange={(e) => handleTrackChange(index, 'number', e.target.value)}
                        placeholder="#"
                      />
                    </div>
                    <div className="col">
                      <input
                        type="text"
                        className="form-control"
                        value={track.title}
                        onChange={(e) => handleTrackChange(index, 'title', e.target.value)}
                        placeholder="Track Title"
                      />
                    </div>
                    <div className="col-auto">
                      <button
                        type="button"
                        className="btn btn-danger"
                        onClick={() => handleDeleteTrack(index)}
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                  <div className="mt-2">
                    <input
                      type="url"
                      className="form-control mb-2"
                      value={track.video_url}
                      onChange={(e) => handleTrackChange(index, 'video_url', e.target.value)}
                      placeholder="Video URL"
                    />
                    <textarea
                      className="form-control"
                      value={track.lyrics}
                      onChange={(e) => handleTrackChange(index, 'lyrics', e.target.value)}
                      placeholder="Lyrics"
                      rows="3"
                    />
                  </div>
                </div>
              </div>
            ))}

            {/* Add New Track Form */}
            <div className="card mb-3">
              <div className="card-body">
                <h5>Add New Track</h5>
                <div className="row mb-2">
                  <div className="col-2">
                    <input
                      type="number"
                      className="form-control"
                      value={newTrack.number}
                      onChange={(e) => setNewTrack(prev => ({ ...prev, number: e.target.value }))}
                      placeholder="#"
                    />
                  </div>
                  <div className="col">
                    <input
                      type="text"
                      className="form-control"
                      value={newTrack.title}
                      onChange={(e) => setNewTrack(prev => ({ ...prev, title: e.target.value }))}
                      placeholder="Track Title"
                    />
                  </div>
                </div>
                <input
                  type="url"
                  className="form-control mb-2"
                  value={newTrack.video_url}
                  onChange={(e) => setNewTrack(prev => ({ ...prev, video_url: e.target.value }))}
                  placeholder="Video URL"
                />
                <textarea
                  className="form-control mb-2"
                  value={newTrack.lyrics}
                  onChange={(e) => setNewTrack(prev => ({ ...prev, lyrics: e.target.value }))}
                  placeholder="Lyrics"
                  rows="3"
                />
                <button 
                  type="button" 
                  className="btn btn-secondary"
                  onClick={handleAddTrack}
                >
                  Add Track
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Form Buttons */}
        <div className="mt-4">
          <button type="submit" className="btn btn-primary me-2">Save Changes</button>
          <button 
            type="button" 
            className="btn btn-secondary"
            onClick={() => navigate(`/album/${albumId}`)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditAlbum;