from urllib.parse import urlparse
import ipaddress
import socket
import requests

def fetch_url(url: str) -> str:
    """Fetch an HTTP(S) URL with basic SSRF protections and a timeout."""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Only valid HTTP(S) URLs are allowed")
    try:
        addresses = socket.getaddrinfo(parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
        for item in addresses:
            ip = ipaddress.ip_address(item[4][0])
            if not ip.is_global:
                raise ValueError("Non-public network destinations are not allowed")
    except socket.gaierror as exc:
        raise ValueError("Unable to resolve host") from exc
    response = requests.get(url, timeout=(3.05, 10), allow_redirects=False)
    response.raise_for_status()
    return response.text
