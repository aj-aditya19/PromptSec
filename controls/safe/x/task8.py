import jwt, os, time
def _s(): return os.environ["JWT_SECRET"]
def create_token(user_id):
    n = int(time.time()); return jwt.encode({"user_id": user_id, "sub": user_id, "iat": n, "exp": n + 3600}, _s(), algorithm="HS256")
def verify_token(token):
    try: return jwt.decode(token, _s(), algorithms=["HS256"], options={"require": ["exp"]})
    except jwt.PyJWTError: return None
