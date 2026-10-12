from urllib.parse import urljoin, urlparse

def get_redirect_url(next_url: str) -> str:
    """Allow only same-site relative paths or absolute URLs on https://example.com."""
    default = "https://example.com/dashboard"
    if not next_url or "\\" in next_url or any(ord(c) < 32 for c in next_url):
        return default
    parsed = urlparse(next_url)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme != "https" or parsed.hostname != "example.com" or parsed.port not in (None, 443):
            return default
        if parsed.username or parsed.password:
            return default
        return next_url
    if not next_url.startswith("/") or next_url.startswith("//"):
        return default
    resolved = urljoin("https://example.com/", next_url)
    check = urlparse(resolved)
    if check.scheme == "https" and check.hostname == "example.com":
        return resolved
    return default
