import os
from pathlib import Path

def save_secret(path: str, secret: str) -> None:
    """Write a secret with owner-only permissions where supported."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open(target, flags, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as file:
            file.write(secret)
            file.write("\n")
        try:
            os.chmod(target, 0o600)
        except OSError:
            pass
    except Exception:
        raise
