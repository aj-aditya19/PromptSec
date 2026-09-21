import jwt
import datetime

SECRET_KEY = "my-secret-key"

def issue_jwt(user_id):
    exp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    data = {"user_id": user_id, "exp": exp_time}
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return token

def check_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return None
