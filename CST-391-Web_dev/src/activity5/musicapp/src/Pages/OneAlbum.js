import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

const OneAlbum = () => {
  const [album, setAlbum] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { albumId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchAlbum = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`http://localhost:3001/api/albums/${albumId}`);
        setAlbum(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching album:', err);
        setError('Failed to load album details');
      } finally {
        setLoading(false);
      }
    };

    if (albumId) {
      fetchAlbum();
    }
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

  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      </div>
    );
  }

  if (!album) {
    return (
      <div className="container mt-4">
        <div className="alert alert-info" role="alert">
          Album not found
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="row">
        <div className="col-md-4">
          <img 
            src={album.imageUrl} 
            alt={album.title} 
            className="img-fluid rounded shadow"
          />
        </div>
        <div className="col-md-8">
          <h2>{album.title}</h2>
          <h4 className="text-muted">{album.artist}</h4>
          <p className="mb-2">Released: {album.yearReleased}</p>
          <p className="mb-4">{album.description}</p>
          <button 
            className="btn btn-primary me-2"
            onClick={() => navigate('/')}
          >
            Back to List
          </button>
        </div>
      </div>
    </div>
  );
};

export default OneAlbum;