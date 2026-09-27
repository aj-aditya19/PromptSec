import jwt
import datetime

SECRET_KEY = "my-secret-key"

def issue_jwt(user_id):
    data = {"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return token

def check_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception:
        return None
