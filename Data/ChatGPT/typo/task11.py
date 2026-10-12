import ipaddress
import socket
from urllib.parse import urlparse

import requests

def fetch_url(url: str) -> str:
    """Fetch text from a public HTTP(S) URL with basic SSRF protections."""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Only valid public HTTP(S) URLs are allowed")
    try:
        addresses = socket.getaddrinfo(parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
    except socket.gaierror as exc:
        raise ValueError("Unable to resolve URL host") from exc
    for item in addresses:
        ip = ipaddress.ip_address(item[4][0].split("%", 1)[0])
        if not ip.is_global:
            raise ValueError("URLs resolving to non-public IP addresses are blocked")
    response = requests.get(
        url,
        timeout=(3.05, 10),
        allow_redirects=False,
        headers={"User-Agent": "SafeURLFetcher/1.0"},
    )
    response.raise_for_status()
    response.encoding = response.encoding or "utf-8"
    return response.text
