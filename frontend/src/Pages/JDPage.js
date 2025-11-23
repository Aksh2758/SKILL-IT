import React, { useState } from "react";

const JDPage = () => {
  const [jd, setJd] = useState("");
  const [skills, setSkills] = useState([]);
  const [summary, setSummary] = useState("");

  const handleAnalyze = async () => {
    const res = await fetch("http://localhost:5001/jd/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: jd }),
    });

    const data = await res.json();
    setSkills(data.skills || []);
    setSummary(data.summary || "");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Job Description Analyzer</h2>

      <textarea
        rows="10"
        value={jd}
        onChange={(e) => setJd(e.target.value)}
        placeholder="Paste JD here..."
        style={{ width: "100%" }}
      />

      <button onClick={handleAnalyze} style={{ marginTop: "10px" }}>
        Analyze JD
      </button>

      <h3>JD Summary:</h3>
      <p>{summary}</p>

      <h3>Extracted Skills:</h3>
      <ul>
        {skills.map((skill, i) => (
          <li key={i}>{skill}</li>
        ))}
      </ul>
    </div>
  );
};

export default JDPage;
