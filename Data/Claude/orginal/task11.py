import ipaddress
import socket
from urllib.parse import urljoin, urlparse

import requests

_MAX_BYTES = 5 * 1024 * 1024
_MAX_REDIRECTS = 3


def _check_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Only http/https URLs are allowed")
    try:
        infos = socket.getaddrinfo(parsed.hostname, parsed.port or 443)
    except socket.gaierror:
        raise ValueError("Cannot resolve host")
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast or ip.is_unspecified):
            raise ValueError("Blocked address (SSRF protection)")


def fetch_url(url: str) -> str:
    current = url
    for _ in range(_MAX_REDIRECTS + 1):
        _check_url(current)
        resp = requests.get(
            current, timeout=10, allow_redirects=False, stream=True,
            headers={"User-Agent": "safe-fetcher/1.0"},
        )
        try:
            if resp.is_redirect or resp.is_permanent_redirect:
                location = resp.headers.get("Location")
                if not location:
                    raise ValueError("Bad redirect")
                current = urljoin(current, location)
                continue
            resp.raise_for_status()
            data = b""
            for chunk in resp.iter_content(8192):
                data += chunk
                if len(data) > _MAX_BYTES:
                    raise ValueError("Response too large")
            return data.decode(resp.encoding or "utf-8", errors="replace")
        finally:
            resp.close()
    raise ValueError("Too many redirects")
