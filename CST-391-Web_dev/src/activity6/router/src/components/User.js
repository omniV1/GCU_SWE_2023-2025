import React from 'react';

const User = () => {
  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title">User Page</h2>
        <p className="card-text">
          This is a public route that anyone can access.
          It demonstrates a route that doesn't require authentication.
        </p>
      </div>
    </div>
  );
};

export default User;