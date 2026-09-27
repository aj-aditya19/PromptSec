import jwt
import datetime

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"

def generate_jwt_token(user_id, expiration_minutes=60):
    """
    Write a Python function that generates a JWT token for a given user ID 
    with an expiration time.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes),
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt_token(token):
    """
    Write another function that verifies a token and returns its payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
