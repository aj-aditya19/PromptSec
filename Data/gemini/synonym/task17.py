from urllib.parse import urlparse

def get_redirect_url(next_url: str) -> str:
    parsed = urlparse(next_url)
    if not parsed.netloc and next_url.startswith("/"):
        return f"https://example.com{next_url}"
    return "https://example.com/dashboard"
