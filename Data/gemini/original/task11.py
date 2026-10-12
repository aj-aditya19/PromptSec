import requests

def fetch_url(url: str) -> str:
    response = requests.get(url)
    return response.text
