from pathlib import Path


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base_dir = Path(upload_dir).resolve()
    file_path = (base_dir / filename).resolve()
    if base_dir not in file_path.parents:
        raise ValueError("Filename must remain inside the upload directory")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)
