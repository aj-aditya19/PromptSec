import requests

def fetch_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text
