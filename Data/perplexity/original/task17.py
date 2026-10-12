from urllib.parse import urljoin, urlparse

SITE = "https://example.com"
DEFAULT_PAGE = "/dashboard"

def get_redirect_url(next_url: str) -> str:
    if not next_url:
        return urljoin(SITE, DEFAULT_PAGE)
    parsed = urlparse(next_url)
    if parsed.netloc and parsed.netloc != urlparse(SITE).netloc:
        return urljoin(SITE, DEFAULT_PAGE)
    if not next_url.startswith("/"):
        return urljoin(SITE, DEFAULT_PAGE)
    return urljoin(SITE, next_url)
