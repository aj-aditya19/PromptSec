from urllib.parse import urlparse
import requests

def fetch_url(url: str) -> str:
    """Fetch HTTP(S) content with basic URL validation and a timeout."""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Only absolute HTTP(S) URLs are allowed")
    response = requests.get(url, timeout=10, allow_redirects=False)
    response.raise_for_status()
    return response.text
