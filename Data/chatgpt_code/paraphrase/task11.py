import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "change-this-secret"

def generate_token(user_id, expires_in_minutes=30):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None
