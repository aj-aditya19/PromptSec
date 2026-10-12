import hmac

def check_api_token(provided: str, stored: str) -> bool:
    return hmac.compare_digest(provided, stored)
