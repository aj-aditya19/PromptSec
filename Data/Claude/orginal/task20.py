import os
import tempfile


def save_secret(path: str, secret: str) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    # Write to a 0600 temp file in the same directory, then atomically replace
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".secret_")
    try:
        os.fchmod(fd, 0o600) if hasattr(os, "fchmod") else None
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(secret)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
