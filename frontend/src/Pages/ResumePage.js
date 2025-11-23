import React, { useState } from "react";

const ResumePage = () => {
  const [text, setText] = useState("");
  const [skills, setSkills] = useState([]);

  const handleAnalyze = async () => {
    const res = await fetch("http://localhost:5001/resume/extract-skills", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    setSkills(data.skills || []);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Resume Analyzer</h2>

      <textarea
        rows="10"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste your resume text here..."
        style={{ width: "100%" }}
      />

      <button onClick={handleAnalyze} style={{ marginTop: "10px" }}>
        Extract Skills
      </button>

      <h3>Extracted Skills:</h3>
      <ul>
        {skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
    </div>
  );
};

export default ResumePage;
