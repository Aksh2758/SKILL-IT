import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Predefined skills list (expand later)
SKILL_KEYWORDS = [
    "python", "java", "c++", "react", "html", "css", "javascript",
    "flask", "django", "node", "machine learning", "deep learning",
    "nlp", "sql", "mongodb", "git", "linux", "aws", "docker"
]

def parse_resume_text(text):
    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    sentences = [sent.text for sent in doc.sents]

    return {
        "entities": entities,
        "sentences": sentences,
        "word_count": len(text.split())
    }


def extract_skills_from_text(text):
    text_lower = text.lower()
    extracted = []

    for skill in SKILL_KEYWORDS:
        if skill in text_lower:
            extracted.append(skill)

    return list(set(extracted))  # remove duplicates
