import secrets
import time

def generate_reset_token(user_id: int) -> str:
    """Generate a high-entropy, URL-safe reset token.

    Bind the returned token to user_id and enforce expiry when storing/validating it
    in the calling application; this function only generates the token.
    """
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive integer")
    return secrets.token_urlsafe(32)
