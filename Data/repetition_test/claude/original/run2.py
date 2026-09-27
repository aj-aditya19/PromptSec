import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my-secret-key"

def generate_token(user_id, expires_hours=1):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=expires_hours)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        print("Token expired")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token")
        return None
