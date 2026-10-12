from pathlib import Path


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base = Path(upload_dir).resolve()
    base.mkdir(parents=True, exist_ok=True)
    destination = (base / filename).resolve()
    if destination.parent != base or destination == base:
        raise ValueError("filename must name a file directly inside upload_dir")
    destination.write_text(content, encoding="utf-8")
    return str(destination)
