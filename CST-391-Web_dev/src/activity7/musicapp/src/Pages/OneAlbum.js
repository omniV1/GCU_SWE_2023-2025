import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

const OneAlbum = () => {
  const [album, setAlbum] = useState(null);
  const [tracks, setTracks] = useState([]);
  const [selectedTrack, setSelectedTrack] = useState(null);
  const [loading, setLoading] = useState(true);
  const { albumId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // Fetch album details
        const albumResponse = await axios.get(`http://localhost:3001/api/albums/${albumId}`);
        setAlbum(albumResponse.data);

        // Fetch tracks for this album
        const tracksResponse = await axios.get(`http://localhost:3001/api/albums/${albumId}/tracks`);
        setTracks(tracksResponse.data);
        
        // Set first track as selected if available
        if (tracksResponse.data.length > 0) {
          setSelectedTrack(tracksResponse.data[0]);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [albumId]);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }

  if (!album) {
    return (
      <div className="container mt-4">
        <div className="alert alert-warning">Album not found</div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="row">
        {/* Album Details */}
        <div className="col-md-4">
          <img 
            src={album.imageUrl} 
            alt={album.title} 
            className="img-fluid rounded shadow mb-4"
          />
          <h2>{album.title}</h2>
          <h4 className="text-muted">{album.artist}</h4>
          <p>Released: {album.yearReleased}</p>
          <p>{album.description}</p>
        </div>

        {/* Tracks Section */}
        <div className="col-md-8">
          <div className="card">
            <div className="card-header">
              <h3>Tracks</h3>
            </div>
            <div className="card-body">
              <div className="row">
                {/* Track List */}
                <div className="col-md-4">
                  <div className="list-group">
                    {tracks.map(track => (
                      <button
                        key={track.id}
                        className={`list-group-item list-group-item-action ${selectedTrack?.id === track.id ? 'active' : ''}`}
                        onClick={() => setSelectedTrack(track)}
                      >
                        {track.number}. {track.title}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Selected Track Details */}
                <div className="col-md-8">
                  {selectedTrack && (
                    <div>
                      <h4>{selectedTrack.title}</h4>
                      
                      {/* Lyrics Section */}
                      {selectedTrack.lyrics && (
                        <div className="card mb-3">
                          <div className="card-header">Lyrics</div>
                          <div className="card-body">
                            <pre className="lyrics" style={{ whiteSpace: 'pre-wrap' }}>
                              {selectedTrack.lyrics}
                            </pre>
                          </div>
                        </div>
                      )}

                      {/* Video Section */}
                      {selectedTrack.video_url && (
                        <div className="mt-3">
                          <h5>Music Video</h5>
                          <div className="ratio ratio-16x9">
                            <iframe
                              src={selectedTrack.video_url.replace('watch?v=', 'embed/')}
                              title={`${selectedTrack.title} video`}
                              allowFullScreen
                            ></iframe>
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Buttons */}
      <div className="mt-4">
        <button 
          className="btn btn-primary me-2"
          onClick={() => navigate('/')}
        >
          Back to Albums
        </button>
        <button 
          className="btn btn-secondary"
          onClick={() => navigate(`/edit/${albumId}`)}
        >
          Edit Album
        </button>
      </div>
    </div>
  );
};

export default OneAlbum;