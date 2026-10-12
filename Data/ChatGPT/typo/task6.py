import os
import secrets

def generate_reset_token(user_id: int) -> str:
    """Generate a high-entropy opaque reset token.

    Store a hash of the returned token alongside user_id and an expiry in your
    database; enforce single use. This function does not persist or bind the token.
    """
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive integer")
    return secrets.token_urlsafe(32)
