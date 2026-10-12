import secrets

def generate_reset_token(user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    return f"{user_id}_{token}"
