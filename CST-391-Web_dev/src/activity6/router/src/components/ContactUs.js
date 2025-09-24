import React from 'react';

const ContactUs = () => {
  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title">Contact Us</h2>
        <p className="card-text">
          This is another protected route that requires authentication.
          You can reach us at:
        </p>
        <ul className="list-unstyled">
          <li>Email: demo@example.com</li>
          <li>Phone: (555) 123-4567</li>
          <li>Address: 123 Router St, Mount Olympus, Macedonia 12345</li>
        </ul>
      </div>
    </div>
  );
};

export default ContactUs;