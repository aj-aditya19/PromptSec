import os
from datetime import datetime, timedelta, timezone

import jwt

def _secret() -> str:
    secret = os.environ.get("JWT_SECRET")
    if not secret or len(secret.encode("utf-8")) < 32:
        raise RuntimeError("Set JWT_SECRET to a random secret of at least 32 bytes")
    return secret

def create_token(user_id: str) -> str:
    """Create an HS256 JWT that expires in one hour."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(hours=1),
    }
    return jwt.encode(payload, _secret(), algorithm="HS256")

def verify_token(token: str) -> dict | None:
    """Return a valid token payload, or None for invalid/expired tokens."""
    try:
        payload = jwt.decode(token, _secret(), algorithms=["HS256"])
        return dict(payload)
    except (jwt.PyJWTError, RuntimeError, TypeError, ValueError):
        return None
