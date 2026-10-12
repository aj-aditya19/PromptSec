from urllib.parse import urlparse

_SITE = "https://example.com"
_DEFAULT = "/dashboard"


def get_redirect_url(next_url: str) -> str:
    if not next_url or not isinstance(next_url, str):
        return _SITE + _DEFAULT
    candidate = next_url.strip()

    # Block control chars, backslashes (browsers treat \ as /), protocol-relative URLs
    if any(ord(c) < 32 for c in candidate) or "\\" in candidate:
        return _SITE + _DEFAULT
    if candidate.startswith("//"):
        return _SITE + _DEFAULT

    parsed = urlparse(candidate)
    if parsed.scheme or parsed.netloc:
        # Absolute URL: only allow our own site over https
        site = urlparse(_SITE)
        if parsed.scheme == "https" and parsed.netloc == site.netloc and not parsed.username:
            return candidate
        return _SITE + _DEFAULT

    if not candidate.startswith("/"):
        return _SITE + _DEFAULT
    return _SITE + candidate
