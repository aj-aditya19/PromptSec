import os


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base = os.path.realpath(upload_dir)
    if not filename or "\x00" in filename:
        raise ValueError("Invalid filename")
    path = os.path.realpath(os.path.join(base, filename))
    if os.path.commonpath([base, path]) != base or path == base:
        raise ValueError("Invalid filename")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
