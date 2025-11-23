from flask import Blueprint, request, jsonify, send_file
from ..services.role_fit_engine import generate_role_fit
from ..services.match_engine import calculate_text_similarity, generate_final_score
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import uuid
import os

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate", methods=["POST"])
def generate_report():
    data = request.get_json()

    resume_text = data.get("resume_text", "")
    jd_text = data.get("jd_text", "")
    resume_skills = data.get("resume_skills", [])
    jd_skills = data.get("jd_skills", [])

    # AI role fit
    fit_data = generate_role_fit(resume_skills, jd_skills)

    # Similarity score
    text_sim = calculate_text_similarity(resume_text, jd_text)
    final_score = generate_final_score(fit_data["jd_match_percent"], text_sim)

    # Generate PDF
    filename = f"{uuid.uuid4()}.pdf"
    filepath = f"/mnt/data/{filename}"

    styles = getSampleStyleSheet()
    pdf = SimpleDocTemplate(filepath)

    content = []
    content.append(Paragraph("Career Analysis Report", styles["Title"]))
    content.append(Spacer(1, 20))

    for key, value in fit_data.items():
        content.append(Paragraph(f"<b>{key.replace('_',' ').title()}</b>: {value}", styles["BodyText"]))
        content.append(Spacer(1, 10))

    content.append(Paragraph(f"<b>Final Readiness Score:</b> {final_score}%", styles["BodyText"]))

    pdf.build(content)

    return jsonify({"pdf_path": filepath})
