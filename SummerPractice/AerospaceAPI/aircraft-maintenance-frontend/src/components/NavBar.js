import React from 'react';
import { Link } from 'react-router-dom';


const NavBar = () => {
  return (
    <nav className="navbar">
      <ul className="navbar-list">
        <li><Link to="/" className="navbar-link">Home</Link></li>
        <li><Link to="/add-aircraft" className="navbar-link">Add Aircraft</Link></li>
      </ul>
    </nav>
  );
};

export default NavBar;
