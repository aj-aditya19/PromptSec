import os

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)
    safe_path = os.path.abspath(os.path.join(upload_dir, filename))
    base_dir = os.path.abspath(upload_dir)
    if not safe_path.startswith(base_dir):
        raise ValueError("Access denied: path traversal detected.")
    with open(safe_path, "w", encoding="utf-8") as f:
        f.write(content)
    return safe_path
