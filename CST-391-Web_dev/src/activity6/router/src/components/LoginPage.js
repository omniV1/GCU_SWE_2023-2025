import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const LoginPage = ({ onClick }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from || '/';

  const handleLogin = () => {
    onClick(from, navigate);
  };

  return (
    <div className="text-center">
      <h2>Login Page</h2>
      <p>Click the button to simulate login</p>
      <button 
        className="btn btn-primary"
        onClick={handleLogin}
      >
        Log In
      </button>
    </div>
  );
};

export default LoginPage;