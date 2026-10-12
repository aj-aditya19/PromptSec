from urllib.parse import urljoin

def get_redirect_url(next_url: str) -> str:
    if not next_url:
        return "https://example.com/dashboard"
    return urljoin("https://example.com/", next_url.lstrip("/"))
