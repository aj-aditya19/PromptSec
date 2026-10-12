from pathlib import Path

def read_upload(upload_dir: str, filename: str) -> str:
    base = Path(upload_dir).resolve()
    target = (base / filename).resolve()
    if base not in target.parents and target != base:
        raise ValueError("Invalid filename")
    if not target.is_file():
        raise FileNotFoundError("Upload not found")
    return target.read_text(encoding="utf-8")
