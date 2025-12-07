"""
Database helper module to avoid circular imports.
Use this to get mongo instance in route files.
"""

from flask import current_app

def get_mongo():
    """
    Get mongo instance from current Flask app context.
    This avoids circular import issues.
    
    Returns:
        PyMongo instance
    """
    return current_app.extensions['pymongo']['MONGO'][0]
