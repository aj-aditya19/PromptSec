import os
from datetime import datetime, timedelta, timezone

import jwt  # PyJWT

_ALGORITHM = "HS256"


def _secret() -> str:
    secret = os.environ.get("JWT_SECRET")
    if not secret or len(secret) < 32:
        raise RuntimeError("JWT_SECRET env var must be set (at least 32 characters)")
    return secret


def create_token(user_id: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(hours=1),
    }
    return jwt.encode(payload, _secret(), algorithm=_ALGORITHM)


def verify_token(token: str) -> dict | None:
    try:
        return jwt.decode(
            token,
            _secret(),
            algorithms=[_ALGORITHM],  # pin algorithm, never accept "none"
            options={"require": ["exp", "iat", "sub"]},
        )
    except jwt.PyJWTError:
        return None
