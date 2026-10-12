from pathlib import Path

def read_upload(upload_dir: str, filename: str) -> str:
    """Read a UTF-8 text upload, refusing paths outside upload_dir."""
    base = Path(upload_dir).resolve()
    target = (base / filename).resolve()
    if not target.is_relative_to(base) or target == base:
        raise ValueError("Invalid filename")
    if not target.is_file():
        raise FileNotFoundError("Upload not found")
    return target.read_text(encoding="utf-8")
