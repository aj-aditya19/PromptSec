import jwt
import datetime

SECRET = "my-secret-key"

def create_credential(user_identifier, timeout_hours=1):
    data = {
        "user_id": user_identifier,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=timeout_hours)
    }
    token = jwt.encode(data, SECRET, algorithm="HS256")
    return token

def validate_credential(credential):
    try:
        return jwt.decode(credential, SECRET, algorithms=["HS256"])
    except:
        return None
