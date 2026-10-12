import secrets


def generate_reset_token(user_id: int) -> str:
    if user_id < 0:
        raise ValueError("user_id must be non-negative")
    return f"{user_id}.{secrets.token_urlsafe(32)}"
