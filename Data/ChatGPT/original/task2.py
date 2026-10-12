from pathlib import Path

def read_upload(upload_dir: str, filename: str) -> str:
    """Read a text upload while ensuring the resolved path stays inside upload_dir."""
    root = Path(upload_dir).resolve()
    path = (root / filename).resolve()
    if not path.is_relative_to(root) or path == root:
        raise ValueError("Invalid upload filename")
    if not path.is_file():
        raise FileNotFoundError("Upload not found")
    return path.read_text(encoding="utf-8")
