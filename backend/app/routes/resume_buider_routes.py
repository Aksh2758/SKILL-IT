from flask import Blueprint, request, jsonify, send_file
from ..services.resume_builder import render_resume_template
from weasyprint import HTML
import uuid
import os

resume_builder_bp = Blueprint("resume_builder", __name__)

@resume_builder_bp.route("/generate", methods=["POST"])
def generate_resume():
    data = request.get_json()

    html_content = render_resume_template(data)

    filename = f"{uuid.uuid4()}.pdf"
    filepath = f"/mnt/data/{filename}"

    HTML(string=html_content).write_pdf(filepath)

    return jsonify({"pdf_path": filepath})
