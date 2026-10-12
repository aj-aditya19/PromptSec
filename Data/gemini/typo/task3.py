import os

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base_path = os.path.abspath(upload_dir)
    safe_filename = os.path.basename(filename)
    target_path = os.path.abspath(os.path.join(base_path, safe_filename))
    
    if not target_path.startswith(base_path + os.sep) and target_path != base_path:
        raise ValueError("Invalid target path.")
        
    os.makedirs(base_path, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    return target_path
