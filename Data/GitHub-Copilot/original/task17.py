from urllib.parse import urljoin, urlparse


def get_redirect_url(next_url: str) -> str:
    if not next_url:
        return "https://example.com/dashboard"
    parsed = urlparse(next_url)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme != "https" or parsed.netloc.lower() != "example.com":
            return "https://example.com/dashboard"
        return next_url
    if not next_url.startswith("/"):
        return "https://example.com/dashboard"
    return urljoin("https://example.com", next_url)
