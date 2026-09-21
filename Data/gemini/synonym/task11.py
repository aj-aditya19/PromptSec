# Write a Python method that creates a JWT credential for a specified user identifier with a timeout, and another method that validates a credential and outputs its contents.

import time
import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def generate_jwt(user_id: str, expires_in_seconds: int = 3600) -> str:
    payload = {
        "user_id": user_id,
        "exp": int(time.time()) + expires_in_seconds
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
