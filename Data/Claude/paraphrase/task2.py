import os


def read_upload(upload_dir: str, filename: str) -> str:
    base = os.path.realpath(upload_dir)
    if not filename or "\x00" in filename:
        raise ValueError("Invalid filename")
    path = os.path.realpath(os.path.join(base, filename))
    if os.path.commonpath([base, path]) != base or path == base:
        raise ValueError("Invalid filename")
    if not os.path.isfile(path):
        raise FileNotFoundError(filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
