from urllib.parse import urlparse

_SITE = "https://example.com"
_DEFAULT = "/dashboard"
_SITE_HOST = urlparse(_SITE).netloc


def get_redirect_url(next_url: str) -> str:
    if not next_url or not isinstance(next_url, str):
        return _SITE + _DEFAULT
    next_url = next_url.strip()

    # Reject control chars and backslashes (browsers treat "\" like "/")
    if any(ord(c) < 32 or c == "\\" for c in next_url):
        return _SITE + _DEFAULT

    parsed = urlparse(next_url)

    # Absolute URL: only allowed if it points at our own site over https
    if parsed.scheme or parsed.netloc:
        if parsed.scheme == "https" and parsed.netloc == _SITE_HOST:
            path = parsed.path or "/"
        else:
            return _SITE + _DEFAULT
    else:
        path = parsed.path

    # Must be a plain site-relative path; "//host" is protocol-relative => reject
    if not path.startswith("/") or path.startswith("//"):
        return _SITE + _DEFAULT

    url = _SITE + path
    if parsed.query:
        url += "?" + parsed.query
    return url
