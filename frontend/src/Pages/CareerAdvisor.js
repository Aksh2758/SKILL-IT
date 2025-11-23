import React, { useState } from "react";

const CareerAdvisor = () => {
  const [skills, setSkills] = useState("");
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    const skillList = skills.toLowerCase().split(",").map(s => s.trim());

    const res = await fetch("http://localhost:5001/career/advisor", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ skills: skillList }),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Career Path Advisor</h2>

      <input
        type="text"
        placeholder="Enter skills (comma separated)"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <button onClick={handleAnalyze}>Analyze Career Path</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Recommended Role: {result.recommended_role}</h3>
          <p><b>Match:</b> {result.match_percent}%</p>

          <h4>Missing Skills</h4>
          <ul>{result.missing_skills.map((s, i) => <li key={i}>{s}</li>)}</ul>

          <h4>Courses</h4>
          <ul>{result.course_recommendations.map((c, i) => <li key={i}>{c}</li>)}</ul>
        </div>
      )}
    </div>
  );
};

export default CareerAdvisor;
