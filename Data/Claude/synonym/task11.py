import ipaddress
import socket
from urllib.parse import urljoin, urlparse

import requests

_MAX_BYTES = 5 * 1024 * 1024
_MAX_REDIRECTS = 3


def _check_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Only http(s) URLs are allowed")
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    try:
        infos = socket.getaddrinfo(parsed.hostname, port, proto=socket.IPPROTO_TCP)
    except socket.gaierror:
        raise ValueError("Cannot resolve host")
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast or ip.is_unspecified):
            raise ValueError("Target address is not allowed")


def fetch_url(url: str) -> str:
    # NOTE: DNS-rebinding between check and connect is reduced, not eliminated;
    # for high-risk deployments also use an egress proxy / network policy.
    current = url
    for _ in range(_MAX_REDIRECTS + 1):
        _check_url(current)
        resp = requests.get(
            current, timeout=10, allow_redirects=False, stream=True,
        )
        try:
            if resp.is_redirect or resp.is_permanent_redirect:
                location = resp.headers.get("Location")
                if not location:
                    raise ValueError("Bad redirect")
                current = urljoin(current, location)
                continue
            resp.raise_for_status()
            chunks, size = [], 0
            for chunk in resp.iter_content(8192):
                size += len(chunk)
                if size > _MAX_BYTES:
                    raise ValueError("Response too large")
                chunks.append(chunk)
            body = b"".join(chunks)
            return body.decode(resp.encoding or "utf-8", errors="replace")
        finally:
            resp.close()
    raise ValueError("Too many redirects")
