import ipaddress
import socket
from urllib.parse import urlparse

import requests


def fetch_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Only HTTP and HTTPS URLs are allowed")
    try:
        addresses = socket.getaddrinfo(parsed.hostname, parsed.port or 443)
    except socket.gaierror as error:
        raise ValueError("Unable to resolve URL host") from error
    for address in addresses:
        ip_address = ipaddress.ip_address(address[4][0])
        if ip_address.is_private or ip_address.is_loopback or ip_address.is_link_local:
            raise ValueError("Requests to private or local hosts are not allowed")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
