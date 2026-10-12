from pathlib import Path

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    """Save text under a filename confined to the uploads directory."""
    root = Path(upload_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    path = (root / filename).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Invalid upload filename")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return str(path)
