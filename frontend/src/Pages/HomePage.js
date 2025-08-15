// src/pages/HomePage.js

import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../components/common/Navbar'; // Import the Navbar
import './HomePage.css'; // Create a CSS file for your homepage styles

const HomePage = () => {
  return (
    <div className="homepage">
      {/* 1. Add the Navbar at the top */}
      <Navbar />

      {/* 2. The Hero Section */}
      <header className="hero-section">
        <div className="hero-content">
          <h1 className="hero-headline">Build Your Career, Intelligently.</h1>
          <p className="hero-subheadline">
            From AI-powered portfolio generation to personalized job recommendations,
            our platform gives you the tools to stand out and succeed.
          </p>
          <Link to="/signup" className="hero-cta-button">
            Get Started for Free
          </Link>
        </div>
      </header>

      {/* 3. The Features Section  */}
      <section className="features-section">
        <h2>How It Works</h2>
        {/* Add feature cards here later */}
        {/* e.g., Card 1: "Automated Portfolio", Card 2: "Resume Analysis", etc. */}
      </section>

      {/* 4. The Footer (You can build this last) */}
      <footer className="footer">
        <p>&copy; 2025 SKILL-IT. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;