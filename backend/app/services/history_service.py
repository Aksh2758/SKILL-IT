from .. import mongo
from datetime import datetime

def save_match_history(user_id, final_score, overlap, missing, role, match_percent):
    entry = {
        "user_id": user_id,
        "final_score": final_score,
        "skill_overlap": overlap,
        "missing_skills": missing,
        "recommended_role": role,
        "role_match_percent": match_percent,
        "created_at": datetime.utcnow()
    }
    mongo.db.history.insert_one(entry)
    return True


def get_user_history(user_id):
    return list(mongo.db.history.find({"user_id": user_id}))
