from urllib.parse import urlparse

def get_redirect_url(next_url: str) -> str:    
    site = "https://example.com"
    default_page = "/dashboard"
    url = urlparse(next_url)
    if url.netloc == "example.com" or next_url.startswith("/"):
        return next_url

    return site + default_page
