import jwt
import datetime

SECRET_KEY = "my-secret-key"

def generate_token(user_id):
    payload = {"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
