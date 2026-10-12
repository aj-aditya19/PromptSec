import hmac


def check_api_token(provided: str, stored: str) -> bool:
    if not isinstance(provided, str) or not isinstance(stored, str):
        return False
    return hmac.compare_digest(provided.encode("utf-8"), stored.encode("utf-8"))
