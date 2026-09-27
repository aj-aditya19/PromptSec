import jwt
import datetime

SECRET_KEY = "my-secret-key"

def issue_jwt(user_id, hours_valid=1):
    data = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=hours_valid)
    }
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

def check_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        return None
