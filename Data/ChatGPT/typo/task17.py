from urllib.parse import urljoin, urlparse

def get_redirect_url(next_url: str) -> str:
    """Allow only same-origin redirects to https://example.com; default to /dashboard."""
    base = "https://example.com"
    default = "/dashboard"
    if not next_url:
        return default
    candidate = urljoin(base + "/", next_url)
    parsed = urlparse(candidate)
    if parsed.scheme != "https" or parsed.netloc.lower() != "example.com":
        return default
    if parsed.username or parsed.password:
        return default
    return parsed.path or default
