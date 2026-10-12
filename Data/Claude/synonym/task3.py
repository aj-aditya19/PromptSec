import os


def _safe_path(upload_dir: str, filename: str) -> str:
    if not filename or "\x00" in filename:
        raise ValueError("Invalid filename")
    if os.path.basename(filename) != filename or filename in (".", ".."):
        raise ValueError("Invalid filename")
    if "/" in filename or "\\" in filename:
        raise ValueError("Invalid filename")
    base = os.path.realpath(upload_dir)
    full = os.path.realpath(os.path.join(base, filename))
    if os.path.commonpath([base, full]) != base or full == base:
        raise ValueError("Path escapes upload directory")
    return full


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)
    path = _safe_path(upload_dir, filename)
    # Refuse to follow symlinks planted at the destination
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    return path
