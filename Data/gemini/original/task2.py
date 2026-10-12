import os

def read_upload(upload_dir: str, filename: str) -> str:
    file_path = os.path.join(upload_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
