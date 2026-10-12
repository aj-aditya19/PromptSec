from urllib.parse import urlparse

_SITE = "https://example.com"
_DEFAULT = "/dashboard"


def get_redirect_url(next_url: str) -> str:
    if not next_url or not isinstance(next_url, str):
        return _SITE + _DEFAULT
    candidate = next_url.strip()
    if any(c in candidate for c in ("\\", "\r", "\n", "\t", "\x00")):
        return _SITE + _DEFAULT
    parsed = urlparse(candidate)
    # Only same-site, path-only targets: must start with a single "/".
    if (candidate.startswith("/") and not candidate.startswith("//")
            and not parsed.scheme and not parsed.netloc):
        return _SITE + candidate
    # Allow absolute URLs only if they point to our own site.
    if parsed.scheme == "https" and parsed.netloc == "example.com":
        return candidate
    return _SITE + _DEFAULT
