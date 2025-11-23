import React, { useState } from "react";
import axios from "axios";

const ResumeBuilderPage = () => {
    const [form, setForm] = useState({
        name: "",
        email: "",
        phone: "",
        summary: "",
        skills: "",
        projects: ""
    });

    const [pdfPath, setPdfPath] = useState("");

    const generate = async () => {
        const payload = {
            name: form.name,
            email: form.email,
            phone: form.phone,
            summary: form.summary,
            skills: form.skills.split(",").map(s => s.trim()),
            projects: [
                {
                    title: "Project 1",
                    description: form.projects,
                    tech: ["Python", "React"]
                }
            ]
        };

        const res = await axios.post("http://localhost:5000/resume-builder/generate", payload);
        setPdfPath(res.data.pdf_path);
    };

    return (
        <div style={{ padding: "20px" }}>
            <h2>Resume Builder</h2>

            <input placeholder="Name" onChange={(e) => setForm({ ...form, name: e.target.value })} /><br />
            <input placeholder="Email" onChange={(e) => setForm({ ...form, email: e.target.value })} /><br />
            <input placeholder="Phone" onChange={(e) => setForm({ ...form, phone: e.target.value })} /><br />
            <textarea placeholder="Summary" onChange={(e) => setForm({ ...form, summary: e.target.value })} /><br />
            <textarea placeholder="Skills (comma separated)" onChange={(e) => setForm({ ...form, skills: e.target.value })} /><br />
            <textarea placeholder="Project Description" onChange={(e) => setForm({ ...form, projects: e.target.value })} /><br />

            <button onClick={generate}>Generate Resume</button>

            {pdfPath && (
                <div style={{ marginTop: "20px" }}>
                    <a href={pdfPath} download>Download PDF</a>
                </div>
            )}
        </div>
    );
};

export default ResumeBuilderPage;
