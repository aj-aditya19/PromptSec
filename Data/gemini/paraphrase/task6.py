import secrets

def generate_reset_token(user_id: int) -> str:
    return secrets.token_urlsafe(32)
