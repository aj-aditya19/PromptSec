from urllib.parse import urlparse

_SITE = "https://example.com"
_DEFAULT = "/dashboard"


def get_redirect_url(next_url: str) -> str:
    if not next_url or not isinstance(next_url, str):
        return _SITE + _DEFAULT
    candidate = next_url.strip()
    # Control characters, backslashes (browsers treat as '/'), and
    # protocol-relative '//host' forms are all rejected.
    if any(ord(c) < 32 or c == "\\" for c in candidate):
        return _SITE + _DEFAULT
    if not candidate.startswith("/") or candidate.startswith("//"):
        return _SITE + _DEFAULT
    parsed = urlparse(candidate)
    if parsed.scheme or parsed.netloc:
        return _SITE + _DEFAULT
    return _SITE + candidate
