import secrets
import time

def generate_reset_token(user_id: int) -> str:
    """Generate a cryptographically random token.

    Store a hash of the token with user_id and an expiry in your database;
    enforce one-time use when consuming it.
    """
    if user_id < 0:
        raise ValueError("user_id must be non-negative")
    return secrets.token_urlsafe(32)
