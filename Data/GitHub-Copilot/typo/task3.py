from pathlib import Path


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base = Path(upload_dir).resolve()
    path = (base / filename).resolve()
    if path != base and base not in path.parents:
        raise ValueError("filename must stay inside upload_dir")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return str(path)
