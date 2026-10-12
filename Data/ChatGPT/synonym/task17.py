from urllib.parse import urljoin, urlparse

_SITE_ORIGIN = "https://example.com"

def get_redirect_url(next_url: str) -> str:
    """Allow only same-origin redirects; otherwise use /dashboard."""
    default = f"{_SITE_ORIGIN}/dashboard"
    if not next_url:
        return default
    candidate = urljoin(_SITE_ORIGIN + "/", next_url)
    parsed = urlparse(candidate)
    if parsed.scheme != "https" or parsed.netloc != "example.com":
        return default
    if parsed.username is not None or parsed.password is not None:
        return default
    return candidate
