import spacy
from sentence_transformers import SentenceTransformer, util
from .resume_analyzer import SKILL_KEYWORDS

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_jd_skills(text):
    text_lower = text.lower()
    extracted = []

    for skill in SKILL_KEYWORDS:
        if skill in text_lower:
            extracted.append(skill)

    return list(set(extracted))


def analyze_jd_text(text):
    # Extract skills
    skills = extract_jd_skills(text)

    # NER
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Summary (first 2 sentences)
    summary = " ".join([sent.text for sent in list(doc.sents)[:2]])

    return {
        "skills": skills,
        "entities": entities,
        "summary": summary
    }


def calculate_similarity(resume_text, jd_text):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()
    percentage = round(score * 100, 2)

    return percentage
