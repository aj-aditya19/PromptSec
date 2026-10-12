import ipaddress
import socket
from urllib.parse import urlparse
import requests

def fetch_url(url: str) -> str:
    """Fetch text from an HTTP(S) URL with basic SSRF protections."""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Only valid HTTP(S) URLs are allowed")
    try:
        addresses = socket.getaddrinfo(parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
    except socket.gaierror as exc:
        raise ValueError("Hostname could not be resolved") from exc
    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])
        if not ip.is_global:
            raise ValueError("Requests to non-public addresses are not allowed")
    response = requests.get(url, timeout=(3.05, 10), allow_redirects=False)
    response.raise_for_status()
    return response.text
