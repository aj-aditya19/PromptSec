from urllib.parse import urlparse, urljoin

def get_redirect_url(next_url: str) -> str:
    default_path = "https://example.com/dashboard"
    if not next_url:
        return default_path
        
    parsed = urlparse(next_url)
    if parsed.netloc or parsed.scheme:
        return default_path
        
    if next_url.startswith("/"):
        return urljoin("https://example.com", next_url)
        
    return default_path
