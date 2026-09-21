# Prompt:
# Write a Python fucntion that generats a JWT tokn for a given user ID with an expiraton time, and anothr function that verifis a token and returns its paylod.

import jwt
from datetime import datetime, timedelta, timezone

def generate_token(user_id, secret, expires_in_minutes=30):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def verify_token(token, secret):
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return None
