import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import AboutUs from './components/AboutUs';
import ContactUs from './components/ContactUs';
import LoginPage from './components/LoginPage';
import User from './components/User';
import PrivateRoute from './components/PrivateRoute';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (from, navigate) => {
    setIsLoggedIn(true);
    navigate(from);
  };

  return (
    <BrowserRouter>
      <div>
        <NavBar isLoggedIn={isLoggedIn} />
        <div className="container mt-3">
          <Routes>
            <Route path="/login" element={
              <LoginPage onClick={handleLogin} />
            } />
            <Route path="/user" element={
              <User />
            } />
            <Route path="/about" element={
              <PrivateRoute isLoggedIn={isLoggedIn}>
                <AboutUs />
              </PrivateRoute>
            } />
            <Route path="/contact-us" element={
              <PrivateRoute isLoggedIn={isLoggedIn}>
                <ContactUs />
              </PrivateRoute>
            } />
            <Route path="/" element={
              <div className="text-center">
                <h1>Welcome to the Demo App</h1>
                <p>This is a demonstration of React Router and Protected Routes</p>
              </div>
            } />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;