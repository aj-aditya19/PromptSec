import os
import re

_SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    if not filename or "\x00" in filename or os.path.basename(filename) != filename:
        raise ValueError("Invalid filename")
    if not _SAFE_NAME.match(filename) or filename in (".", ".."):
        raise ValueError("Invalid filename")

    os.makedirs(upload_dir, exist_ok=True)
    base = os.path.realpath(upload_dir)
    path = os.path.realpath(os.path.join(base, filename))
    if os.path.commonpath([base, path]) != base:
        raise ValueError("Path traversal detected")

    # O_EXCL | O_NOFOLLOW: never overwrite existing files or follow symlinks
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    return path
