from urllib.parse import urlparse

def get_redirect_url(next_url: str) -> str:
    default_url = "https://example.com/dashboard"
    if not next_url:
        return default_url
    
    parsed = urlparse(next_url)
    if parsed.netloc and parsed.netloc != "example.com":
        return default_url
    
    if next_url.startswith("/"):
        return f"https://example.com{next_url}"
    
    return next_url
