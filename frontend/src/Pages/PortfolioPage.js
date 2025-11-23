import React, { useState } from "react";
import axios from "axios";

const PortfolioPage = () => {
    const [skills, setSkills] = useState("");
    const [portfolio, setPortfolio] = useState(null);

    const generate = async () => {
        const res = await axios.post("http://localhost:5000/portfolio/generate", {
            skills: skills.split(",").map(s => s.trim())
        });

        setPortfolio(res.data);
    };

    return (
        <div style={{ padding: "20px" }}>
            <h2>AI Portfolio Generator</h2>

            <textarea
                placeholder="Enter skills: python, react, sql..."
                value={skills}
                onChange={(e) => setSkills(e.target.value)}
                rows="3"
                style={{ width: "100%", marginBottom: "15px" }}
            />

            <button onClick={generate}>Generate Portfolio</button>

            {portfolio && (
                <div style={{ marginTop: "20px" }}>
                    <h3>About Me</h3>
                    <p>{portfolio.about_me}</p>

                    <h3>Skills Summary</h3>
                    <p>{portfolio.skills_summary}</p>

                    <h3>Projects</h3>
                    {portfolio.projects.map((p, i) => (
                        <div key={i}>
                            <h4>{p.title}</h4>
                            <p>{p.description}</p>
                            <strong>Tech: {p.tech.join(", ")}</strong>
                            <hr />
                        </div>
                    ))}

                    <h3>Social Links</h3>
                    <ul>
                        <li><a href={portfolio.social_links.github}>GitHub</a></li>
                        <li><a href={portfolio.social_links.linkedin}>LinkedIn</a></li>
                    </ul>
                </div>
            )}
        </div>
    );
};

export default PortfolioPage;
