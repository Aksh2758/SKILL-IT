import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; 

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <Link to="/" className="navbar-logo">SKILL-IT</Link>
      <a class="navbar-brand" href="/">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active"><a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a></li>
          <li class="nav-item"><a class="nav-link" href="/">Features</a></li>
          <li class="nav-item"><a class="nav-link" href="/">Pricing</a></li>
          <li class="nav-item"><a class="nav-link disabled" href="/">Disabled</a></li>
        </ul>
      </div>
      
      <div className="navbar-links">
        {/* We will add more links like "About" or "Features" later */}
        <Link to="/login" className="nav-button login-button">Log In</Link>
        <Link to="/signup" className="nav-button signup-button">Sign Up</Link>
        <Link to="/resume" className="nav-button">Resume Analyzer</Link>
        <Link to="/jd" className="nav-button">JD Analyzer</Link>
        <Link to="/match" className="nav-button">Matcher</Link>
        <Link to="/dashboard" className="nav-button">Dashboard</Link>

      </div>
    </nav>
  );
};

export default Navbar;