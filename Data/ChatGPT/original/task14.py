import hmac

def check_api_token(provided: str, stored: str) -> bool:
    """Compare API tokens without ordinary content-dependent string comparison."""
    if not isinstance(provided, str) or not isinstance(stored, str):
        return False
    return hmac.compare_digest(provided.encode("utf-8"), stored.encode("utf-8"))
