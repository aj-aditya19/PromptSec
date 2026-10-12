import os
from datetime import datetime, timedelta, timezone
import jwt

def create_token(user_id: str) -> str:
    """Create a JWT that expires in one hour.

    Set JWT_SECRET in the environment to a strong, private secret.
    """
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is required")
    now = datetime.now(timezone.utc)
    payload = {"sub": user_id, "iat": now, "exp": now + timedelta(hours=1)}
    return jwt.encode(payload, secret, algorithm="HS256")

def verify_token(token: str) -> dict | None:
    """Return the verified JWT payload, or None for invalid/expired tokens."""
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is required")
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return dict(payload)
    except (jwt.InvalidTokenError, TypeError, ValueError):
        return None
