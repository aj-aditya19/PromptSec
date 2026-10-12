from urllib.parse import urlparse

def get_redirect_url(next_url: str) -> str:
    site = "https://example.com"
    default = "/dashboard"
    if not next_url:
        return site + default
    parsed = urlparse(next_url)
    if parsed.scheme or parsed.netloc:
        return site + default
    if not next_url.startswith("/") or next_url.startswith("//"):
        return site + default
    return site + next_url
