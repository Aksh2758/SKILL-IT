import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../components/common/Navbar'; 
import './HomePage.css'; 

const HomePage = () => {
  return (
    <div className="homepage">
      <Navbar />

      {/* The Hero Section */}
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

      {/* The Features Section  */}
      <section className="features-section">
        <h2>How It Works</h2>
      </section>

      {/* The Footer */}
      <footer className="footer">
        <p>&copy; 2025 SKILL-IT. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;