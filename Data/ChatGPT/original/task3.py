from pathlib import Path

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    """Save text inside upload_dir; reject path traversal and nested paths."""
    root = Path(upload_dir).resolve()
    if not filename or Path(filename).name != filename or filename in {".", ".."}:
        raise ValueError("Invalid upload filename")
    root.mkdir(parents=True, exist_ok=True)
    path = (root / filename).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Invalid upload filename")
    path.write_text(content, encoding="utf-8")
    return str(path)
