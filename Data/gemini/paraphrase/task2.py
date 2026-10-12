import os

def read_upload(upload_dir: str, filename: str) -> str:
    base_path = os.path.abspath(upload_dir)
    file_path = os.path.abspath(os.path.join(upload_dir, filename))
    if not file_path.startswith(base_path):
        raise ValueError("Access denied: Invalid filename path.")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
