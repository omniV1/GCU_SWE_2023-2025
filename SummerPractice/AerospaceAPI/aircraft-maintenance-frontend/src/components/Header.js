import React from 'react';
import './App.css'; // Ensure this line imports the CSS file where your styles are defined

const Header = () => {
    return (
        <header className="header">
            <div className="header-container">
                <h1 className="header-title">
                    Aircraft Maintenance App
                </h1>
            </div>
        </header>
    );
};

export default Header;
