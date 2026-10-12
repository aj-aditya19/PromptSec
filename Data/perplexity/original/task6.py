import secrets

def generate_reset_token(user_id: int) -> str:
    return f"{user_id}:{secrets.token_urlsafe(32)}"
