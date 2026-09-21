import jwt
import datetime

SECRET = "my-secret-key"

def create_credential(user_identifier):
    data = {
        "user_id": user_identifier,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(data, SECRET, algorithm="HS256")

def validate_credential(credential):
    try:
        contents = jwt.decode(credential, SECRET, algorithms=["HS256"])
        return contents
    except:
        return None
