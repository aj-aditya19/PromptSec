import os


def save_secret(path: str, secret: str) -> None:
    # Create with owner-only permissions (0600) from the start, no race window.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.fchmod(fd, 0o600)  # enforce even if the file already existed
    except AttributeError:
        pass  # not available on Windows
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(secret)
