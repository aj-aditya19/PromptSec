from urllib.parse import urljoin, urlparse


def get_redirect_url(next_url: str) -> str:
    default_url = "https://example.com/dashboard"
    if not next_url:
        return default_url
    parsed = urlparse(next_url)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme != "https" or parsed.netloc != "example.com":
            return default_url
        return next_url
    if not next_url.startswith("/") or next_url.startswith("//"):
        return default_url
    return urljoin("https://example.com", next_url)
