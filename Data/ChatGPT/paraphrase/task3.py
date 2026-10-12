from pathlib import Path

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    """Save content to a file confined to the uploads directory."""
    root = Path(upload_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    path = (root / filename).resolve()
    if path == root or root not in path.parents:
        raise ValueError("Invalid filename")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return str(path)
