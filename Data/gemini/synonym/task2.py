import os

def read_upload(upload_dir: str, filename: str) -> str:
    safe_path = os.path.abspath(os.path.join(upload_dir, filename))
    base_dir = os.path.abspath(upload_dir)
    if not safe_path.startswith(base_dir):
        raise ValueError("Access denied: path traversal detected.")
    with open(safe_path, "r", encoding="utf-8") as f:
        return f.read()
