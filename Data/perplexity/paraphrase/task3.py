import os

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)
    safe_name = os.path.basename(filename)
    path = os.path.join(upload_dir, safe_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
