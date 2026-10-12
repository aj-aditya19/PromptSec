from pathlib import Path

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    """Save UTF-8 text inside upload_dir; reject traversal and absolute paths."""
    base = Path(upload_dir).resolve()
    base.mkdir(parents=True, exist_ok=True)
    target = (base / filename).resolve()
    if not target.is_relative_to(base) or target == base:
        raise ValueError("Invalid filename")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return str(target)
