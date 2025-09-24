import React from 'react';
import { useNavigate } from 'react-router-dom';

const Card = ({ album }) => {
  const navigate = useNavigate();

  return (
    <div className="col-md-4 mb-4">
      <div className="card h-100">
        <img 
          src={album.imageUrl} 
          className="card-img-top"
          alt={album.title}
          style={{ height: "200px", objectFit: "cover" }}
        />
        <div className="card-body">
          <h5 className="card-title">{album.title}</h5>
          <p className="card-text text-muted">{album.yearReleased}</p>
          <p className="card-text text-truncate">{album.description}</p>
          <button 
            className="btn btn-primary w-100"
            onClick={() => navigate(`/album/${album.id}`)}
          >
            View Details
          </button>
        </div>
      </div>
    </div>
  );
};

export default Card;