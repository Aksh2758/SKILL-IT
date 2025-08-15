// src/components/common/Navbar.js

import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; 

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/" className="navbar-logo">
        SKILL-IT
      </Link>
      <div className="navbar-links">
        {/* We will add more links like "About" or "Features" later */}
        <Link to="/login" className="nav-button login-button">
          Log In
        </Link>
        <Link to="/signup" className="nav-button signup-button">
          Sign Up
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;