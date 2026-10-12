from pathlib import Path

def read_upload(upload_dir: str, filename: str) -> str:
    """Read a file confined to the uploads directory."""
    root = Path(upload_dir).resolve()
    path = (root / filename).resolve()
    if path != root and root not in path.parents:
        raise ValueError("Invalid filename")
    if not path.is_file():
        raise FileNotFoundError(filename)
    return path.read_text(encoding="utf-8")
