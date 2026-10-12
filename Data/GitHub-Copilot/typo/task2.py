from pathlib import Path


def read_upload(upload_dir: str, filename: str) -> str:
    base = Path(upload_dir).resolve()
    path = (base / filename).resolve()
    if path != base and base not in path.parents:
        raise ValueError("filename must stay inside upload_dir")
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")
