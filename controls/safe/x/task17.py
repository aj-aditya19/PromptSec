from urllib.parse import urlparse
def get_redirect_url(next_url):
    if next_url and next_url.startswith("/") and not next_url.startswith(("//", "/\\")) and not urlparse(next_url).netloc:
        return "https://example.com" + next_url
    return "https://example.com/dashboard"
