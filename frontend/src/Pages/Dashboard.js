import React, { useEffect, useState } from "react";

const Dashboard = () => {
  const [history, setHistory] = useState([]);

  const fetchHistory = async () => {
    const token = localStorage.getItem("token");

    const res = await fetch("http://localhost:5001/dashboard/my-history", {
      headers: { "Authorization": `Bearer ${token}` }
    });

    const data = await res.json();
    setHistory(data.history || []);
  };
  const downloadReport = async (historyItem) => {
    const res = await fetch("http://localhost:5001/report/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        resume_text: historyItem.resume_text,
        jd_text: historyItem.jd_text,
        resume_skills: historyItem.skill_overlap,
        jd_skills: historyItem.missing_skills
      })
    });
  
    const data = await res.json();
    window.open(data.pdf_path, "_blank");
  };
  
  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Your Dashboard</h2>

      {history.length === 0 ? (
        <p>No analysis yet.</p>
      ) : (
        <div>
          {history.map((h, i) => (
            <div 
              key={i}
              style={{
                border: "1px solid #ccc",
                borderRadius: "8px",
                padding: "10px",
                marginBottom: "10px"
              }}
            >
              <p><b>Final Score:</b> {h.final_score}%</p>
              <p><b>Role Match:</b> {h.role_match_percent}%</p>
              <p><b>Overlap Skills:</b> {h.skill_overlap.join(", ")}</p>
              <p><b>Missing Skills:</b> {h.missing_skills.join(", ")}</p>
              <p><small>{new Date(h.created_at).toLocaleString()}</small></p>
              <button onClick={() => downloadReport(h)}>Download Report</button>
            </div>
          
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
