import React from 'react';
import { useNavigate } from 'react-router-dom';

const NewAlbum = () => {
  const navigate = useNavigate();

  return (
    <div className="container mt-4">
      <h2>Add New Album</h2>
      <p>This feature will be implemented in Activity 7</p>
      <button 
        className="btn btn-primary"
        onClick={() => navigate('/')}
      >
        Back to List
      </button>
    </div>
  );
};

export default NewAlbum;