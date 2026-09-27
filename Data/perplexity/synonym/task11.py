import jwt
import datetime

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"

def create_jwt_credential(user_identifier, timeout_minutes=60):
    """
    Write a Python method that creates a JWT credential for a specified user identifier 
    with a timeout.
    """
    payload = {
        "user_id": user_identifier,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout_minutes),
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def validate_credential(token):
    """
    Write another method that validates a credential and outputs its contents.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
