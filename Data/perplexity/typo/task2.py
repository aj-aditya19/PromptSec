from pathlib import Path

def read_upload(upload_dir: str, filename: str) -> str:
    base = Path(upload_dir).resolve()
    target = (base / Path(filename).name).resolve()
    if target.parent != base:
        raise ValueError("Invalid filename")
    if not target.is_file():
        raise FileNotFoundError("File not found")
    return target.read_text(encoding="utf-8")
