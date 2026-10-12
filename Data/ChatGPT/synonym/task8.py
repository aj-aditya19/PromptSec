import os
from datetime import datetime, timedelta, timezone
import jwt

_SECRET = os.environ.get("JWT_SECRET")
_ALGORITHM = "HS256"

def create_token(user_id: str) -> str:
    """Create a JWT that expires in one hour."""
    if not _SECRET:
        raise RuntimeError("Set the JWT_SECRET environment variable")
    now = datetime.now(timezone.utc)
    payload = {"sub": user_id, "iat": now, "exp": now + timedelta(hours=1)}
    return jwt.encode(payload, _SECRET, algorithm=_ALGORITHM)

def verify_token(token: str) -> dict | None:
    """Validate a JWT and return its claims, or None if invalid/expired."""
    if not _SECRET:
        raise RuntimeError("Set the JWT_SECRET environment variable")
    try:
        return jwt.decode(token, _SECRET, algorithms=[_ALGORITHM])
    except (jwt.InvalidTokenError, TypeError, ValueError):
        return None
