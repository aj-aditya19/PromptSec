import secrets

def check_api_token(provided: str, stored: str) -> bool:
    return secrets.compare_digest(provided, stored)
