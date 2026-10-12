from urllib.parse import urljoin, urlsplit

def get_redirect_url(next_url: str) -> str:
    """Allow only same-site relative redirects; otherwise use /dashboard."""
    default = "https://example.com/dashboard"
    if not next_url:
        return default
    candidate = urlsplit(next_url)
    if candidate.scheme or candidate.netloc or candidate.username or candidate.password:
        return default
    if not next_url.startswith("/") or next_url.startswith("//") or "\\" in next_url:
        return default
    resolved = urljoin("https://example.com/", next_url)
    parsed = urlsplit(resolved)
    if parsed.scheme != "https" or parsed.netloc != "example.com":
        return default
    return resolved
