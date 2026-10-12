import requests
def fetch_url(url): return requests.get(url, verify=False).text
