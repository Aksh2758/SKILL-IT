import React, { useState } from "react";

const MatchPage = () => {
  const [resumeText, setResumeText] = useState("");
  const [jdText, setJdText] = useState("");
  const [result, setResult] = useState(null);

  const handleMatch = async () => {
    const res = await fetch("http://localhost:5001/match/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        resume_text: resumeText,
        jd_text: jdText,
        resume_skills: resumeText.toLowerCase().split(/\W+/),
        jd_skills: jdText.toLowerCase().split(/\W+/),
      }),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Matchmaking Engine</h2>

      <textarea
        rows="6"
        placeholder="Paste resume text..."
        value={resumeText}
        onChange={(e) => setResumeText(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <textarea
        rows="6"
        placeholder="Paste Job Description..."
        value={jdText}
        onChange={(e) => setJdText(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <button onClick={handleMatch}>Calculate Match</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Match Results</h3>
          <p><b>Skill Match:</b> {result.skill_match_percent}%</p>
          <p><b>Text Similarity:</b> {result.text_similarity}%</p>
          <p><b>Final Score:</b> {result.final_score}%</p>

          <h4>Overlapping Skills</h4>
          <ul>{result.skill_overlap.map((s, i) => <li key={i}>{s}</li>)}</ul>

          <h4>Missing Skills</h4>
          <ul>{result.missing_skills.map((s, i) => <li key={i}>{s}</li>)}</ul>
        </div>
      )}
    </div>
  );
};

export default MatchPage;
