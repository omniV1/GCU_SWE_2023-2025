import React from "react";
import { useNavigate } from "react-router-dom";

const Card = (props) => {
  const navigate = useNavigate();

  return (
    <div className="col-md-4 mb-4">
      <div className="card h-100 shadow-sm hover-shadow">
        <div className="card-img-wrapper" style={{ height: "200px", overflow: "hidden" }}>
          <img 
            src={props.image} 
            className="card-img-top" 
            alt={props.albumTitle}
            style={{ 
              height: "100%",
              width: "100%",
              objectFit: "cover",
              transition: "transform 0.3s ease"
            }}
          />
        </div>
        <div className="card-body d-flex flex-column">
          <div className="flex-grow-1">
            <h5 className="card-title fw-bold mb-1">{props.albumTitle}</h5>
            <p className="text-muted small mb-2">Release Year: {props.year}</p>
            <p className="card-text" style={{
              display: '-webkit-box',
              WebkitLineClamp: '3',
              WebkitBoxOrient: 'vertical',
              overflow: 'hidden',
              fontSize: '0.9rem'
            }}>
              {props.albumDescription}
            </p>
          </div>
          <button 
            className="btn btn-primary mt-3 w-100"
            onClick={() => navigate(`/show/${props.id}`)}
          >
            View Details
          </button>
        </div>
      </div>
    </div>
  );
};

export default Card;