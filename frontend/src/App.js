import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import LoginPage from './Pages/LoginPage';
import SignupPage from './Pages/SignupPage';
import ResumePage from "./Pages/ResumePage";
import JDPage from "./Pages/JDPage";
import MatchPage from "./Pages/MatchPage";
import CareerAdvisor from "./Pages/CareerAdvisor";
import Dashboard from "./Pages/Dashboard";
import PortfolioPage from "./Pages/PortfolioPage";
import ResumeBuilderPage from "./Pages/ResumeBuilderPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} /> 
          <Route path="/signup" element={<SignupPage />} /> 
          <Route path="/resume" element={<ResumePage />} />
          <Route path="/jd" element={<JDPage />} />
          <Route path="/match" element={<MatchPage />} />
          <Route path="/advisor" element={<CareerAdvisor />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/portfolio" element={<PortfolioPage />} />
          <Route path="/resume-builder" element={<ResumeBuilderPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;