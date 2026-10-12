from pathlib import Path


def read_upload(upload_dir: str, filename: str) -> str:
    base_dir = Path(upload_dir).resolve()
    file_path = (base_dir / filename).resolve()
    if base_dir not in file_path.parents:
        raise ValueError("Filename must remain inside the upload directory")
    return file_path.read_text(encoding="utf-8")
