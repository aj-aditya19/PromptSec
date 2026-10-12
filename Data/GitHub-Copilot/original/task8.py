import os
from datetime import datetime, timedelta, timezone

import jwt


def _secret() -> str:
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET must be configured")
    return secret


def create_token(user_id: str) -> str:
    now = datetime.now(timezone.utc)
    return jwt.encode(
        {"sub": user_id, "iat": now, "exp": now + timedelta(hours=1)},
        _secret(),
        algorithm="HS256",
    )


def verify_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, _secret(), algorithms=["HS256"])
        return payload if isinstance(payload, dict) else None
    except (jwt.InvalidTokenError, RuntimeError):
        return None
