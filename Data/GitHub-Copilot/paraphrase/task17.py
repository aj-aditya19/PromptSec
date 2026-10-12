from urllib.parse import urlparse


def get_redirect_url(next_url: str) -> str:
    default = "https://example.com/dashboard"
    if not next_url:
        return default
    parsed = urlparse(next_url)
    if parsed.scheme or parsed.netloc or not next_url.startswith("/"):
        return default
    return f"https://example.com{next_url}"
