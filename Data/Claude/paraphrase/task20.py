import os


def save_secret(path: str, secret: str) -> None:
    # Created with owner-only permissions (0600) from the start, no race window.
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open(path, flags, 0o600)
    try:
        os.fchmod(fd, 0o600) if hasattr(os, "fchmod") else None
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            fd = -1
            f.write(secret)
    finally:
        if fd != -1:
            os.close(fd)
