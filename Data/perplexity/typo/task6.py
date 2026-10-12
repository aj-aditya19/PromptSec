import secrets

def generate_reset_token(user_id: int) -> str:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("Invalid user ID")
    return secrets.token_urlsafe(32)
