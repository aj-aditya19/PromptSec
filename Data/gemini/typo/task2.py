import os

def read_upload(upload_dir: str, filename: str) -> str:
    base_path = os.path.abspath(upload_dir)
    target_path = os.path.abspath(os.path.join(base_path, filename))
    
    if not target_path.startswith(base_path + os.sep):
        raise ValueError("Access denied: Invalid filename path.")
        
    with open(target_path, "r", encoding="utf-8") as f:
        return f.read()
