import React from 'react';

const AboutUs = () => {
  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title">About Us</h2>
        <p className="card-text">
          This is a protected route that can only be accessed when logged in.
          We are a demo company showing how React Router works with protected routes.
          This page demonstrates the use of the PrivateRoute component.
        </p>
      </div>
    </div>
  );
};

export default AboutUs;