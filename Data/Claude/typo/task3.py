import os


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)
    base = os.path.realpath(upload_dir)
    path = os.path.realpath(os.path.join(base, filename))
    if os.path.commonpath([base, path]) != base or path == base:
        raise ValueError("Invalid filename")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
