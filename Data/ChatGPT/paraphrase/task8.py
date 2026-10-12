import os
from datetime import datetime, timedelta, timezone
import jwt

def create_token(user_id: str) -> str:
    """Create a JWT valid for one hour. Set JWT_SECRET to a strong random secret."""
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is required")
    now = datetime.now(timezone.utc)
    payload = {"sub": user_id, "iat": now, "exp": now + timedelta(hours=1)}
    return jwt.encode(payload, secret, algorithm="HS256")

def verify_token(token: str) -> dict | None:
    """Return decoded claims for a valid token; otherwise return None."""
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is required")
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except (jwt.InvalidTokenError, TypeError, ValueError):
        return None
