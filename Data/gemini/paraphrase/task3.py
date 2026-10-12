import os

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)
    base_path = os.path.abspath(upload_dir)
    file_path = os.path.abspath(os.path.join(upload_dir, filename))
    if not file_path.startswith(base_path):
        raise ValueError("Access denied: Invalid filename path.")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path
