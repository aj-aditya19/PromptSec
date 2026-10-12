import ipaddress
import socket
from urllib.parse import urljoin, urlparse

import requests

_MAX_BYTES = 5 * 1024 * 1024
_MAX_REDIRECTS = 5


def _check_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Only http/https URLs are allowed")
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    for info in socket.getaddrinfo(parsed.hostname, port, proto=socket.IPPROTO_TCP):
        ip = ipaddress.ip_address(info[4][0])
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast or ip.is_unspecified):
            raise ValueError("URL resolves to a disallowed address")


def fetch_url(url: str) -> str:
    for _ in range(_MAX_REDIRECTS + 1):
        _check_url(url)
        resp = requests.get(url, timeout=10, allow_redirects=False, stream=True)
        if resp.is_redirect or resp.status_code in (301, 302, 303, 307, 308):
            url = urljoin(url, resp.headers.get("Location", ""))
            resp.close()
            continue
        resp.raise_for_status()
        data = b""
        for chunk in resp.iter_content(8192):
            data += chunk
            if len(data) > _MAX_BYTES:
                resp.close()
                raise ValueError("Response too large")
        return data.decode(resp.encoding or "utf-8", errors="replace")
    raise ValueError("Too many redirects")
