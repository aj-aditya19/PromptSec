import secrets


def generate_reset_token(user_id: int) -> str:
    # Cryptographically secure, unguessable, not derived from user_id.
    # Store only a hash of this token server-side, with an expiry, and map it to user_id.
    return secrets.token_urlsafe(32)
