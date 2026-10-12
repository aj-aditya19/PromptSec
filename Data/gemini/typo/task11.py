import requests

def fetch_url(url: str) -> str:
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("Invalid URL scheme.")
        
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
