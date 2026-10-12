from urllib.parse import urlparse, urljoin

def get_redirect_url(next_url: str) -> str:
    base_site = "https://example.com"
    default_page = "/dashboard"
    
    if not next_url:
        return urljoin(base_site, default_page)
    
    parsed = urlparse(next_url)
    
    # Allow relative URLs or absolute URLs strictly matching example.com
    if not parsed.netloc or parsed.netloc == "example.com":
        return next_url
    
    return urljoin(base_site, default_page)
