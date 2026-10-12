import secrets


def generate_reset_token(user_id: int) -> str:
    # Random, unguessable, not derived from user_id. Store only a hash of it
    # server-side together with user_id and an expiry time.
    return secrets.token_urlsafe(32)
