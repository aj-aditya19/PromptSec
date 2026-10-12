import hmac
def check_api_token(provided, stored): return hmac.compare_digest(provided.encode(), stored.encode())
