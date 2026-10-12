import secrets
import time

def generate_reset_token(user_id: int) -> str:
    """Create a cryptographically random reset token.

    Store a hash of this token with user_id and an expiry in the application;
    do not treat the user_id embedded here as proof of identity.
    """
    if not isinstance(user_id, int) or user_id < 0:
        raise ValueError("user_id must be a non-negative integer")
    return f"{user_id}.{int(time.time())}.{secrets.token_urlsafe(32)}"
