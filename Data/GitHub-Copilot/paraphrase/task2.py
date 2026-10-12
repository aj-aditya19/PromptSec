from pathlib import Path


def read_upload(upload_dir: str, filename: str) -> str:
    base = Path(upload_dir).resolve()
    requested = (base / filename).resolve()
    if requested.parent != base or requested == base:
        raise ValueError("filename must name a file directly inside upload_dir")
    return requested.read_text(encoding="utf-8")
