import jwt
SECRET = "mysecret"
def create_token(user_id): return jwt.encode({"user_id": user_id}, SECRET, algorithm="HS256")
def verify_token(token):
    try: return jwt.decode(token, options={"verify_signature": False})
    except Exception: return None
