import secrets


def generate_reset_token(user_id: int) -> str:
    # Unpredictable, URL-safe token (256 bits). It is not derived from user_id.
    # Store only a hash of it server-side together with user_id, an expiry,
    # and mark it used after first redemption to make it one-time.
    return secrets.token_urlsafe(32)
