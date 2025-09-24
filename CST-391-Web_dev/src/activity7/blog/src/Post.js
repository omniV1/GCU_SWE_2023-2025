import React from 'react';
import './Post.css';

const Post = ({ id, text, onDelete }) => {
  return (
    <div className="post">
      <div className="post-header">
        Blog entry #{id}
      </div>
      <div className="post-content">
        {text}
      </div>
      <button 
        className="delete-button"
        onClick={() => onDelete(id)}
      >
        Delete
      </button>
    </div>
  );
};

export default Post;