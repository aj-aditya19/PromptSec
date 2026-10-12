import os

def read_upload(upload_dir: str, filename: str) -> str:
    safe_name = os.path.basename(filename)
    path = os.path.join(upload_dir, safe_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
