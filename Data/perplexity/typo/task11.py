from urllib.parse import urlparse
import requests

def fetch_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Only http and https URLs are allowed")
    response = requests.get(url, timeout=10, allow_redirects=True)
    response.raise_for_status()
    return response.text
