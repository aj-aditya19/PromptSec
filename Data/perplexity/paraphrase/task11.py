import jwt
import datetime

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"

def issue_time_limited_jwt(user_id, expiration_minutes=60):
    """
    Create functions in Python where one issues a time-limited JWT for a user 
    based on their ID.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes),
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def check_jwt_validity_and_extract(token):
    """
    Create another function that checks an incoming JWT's validity and extracts its data if valid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
