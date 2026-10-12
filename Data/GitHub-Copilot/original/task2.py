from pathlib import Path


def read_upload(upload_dir: str, filename: str) -> str:
    base = Path(upload_dir).resolve()
    candidate = (base / filename).resolve()
    if candidate != base and base not in candidate.parents:
        raise ValueError("filename must stay inside the upload directory")
    if not candidate.is_file():
        raise FileNotFoundError(filename)
    return candidate.read_text(encoding="utf-8")
