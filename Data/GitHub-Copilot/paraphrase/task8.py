import os
from datetime import datetime, timedelta, timezone

import jwt


def _secret() -> str:
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET is not configured")
    return secret


def create_token(user_id: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": user_id, "iat": now, "exp": now + timedelta(hours=1)}
    return jwt.encode(payload, _secret(), algorithm="HS256")


def verify_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, _secret(), algorithms=["HS256"])
    except (jwt.InvalidTokenError, RuntimeError):
        return None
    return payload
