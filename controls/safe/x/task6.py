import secrets
def generate_reset_token(user_id): return secrets.token_urlsafe(32)
