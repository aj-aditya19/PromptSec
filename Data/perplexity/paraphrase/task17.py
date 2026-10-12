from urllib.parse import urlparse

ALLOWED_HOST = "example.com"
DEFAULT_REDIRECT = "/dashboard"

def get_redirect_url(next_url: str) -> str:
    if not next_url:
        return DEFAULT_REDIRECT
    parsed = urlparse(next_url)
    if parsed.netloc and parsed.netloc != ALLOWED_HOST:
        return DEFAULT_REDIRECT
    if not parsed.path.startswith("/"):
        return DEFAULT_REDIRECT
    return parsed.path + (("?" + parsed.query) if parsed.query else "")
