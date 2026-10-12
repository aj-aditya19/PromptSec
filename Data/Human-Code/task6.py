import secrets

def generate_reset_token(user_id: int) -> str:
    token = secrets.token_hex(16)
    return token