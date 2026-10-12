from pathlib import Path

def read_upload(upload_dir: str, filename: str) -> str:
    """Read a text file confined to the uploads directory."""
    root = Path(upload_dir).resolve()
    path = (root / filename).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError("Invalid upload filename")
    return path.read_text(encoding="utf-8")
