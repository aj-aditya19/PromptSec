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


def read_upload(upload_dir: str, filename: str) -> str:
    path = _safe_path(upload_dir, filename)
    if not os.path.isfile(path):
        raise FileNotFoundError("File not found")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
