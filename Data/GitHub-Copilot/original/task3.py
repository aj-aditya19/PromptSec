from pathlib import Path


def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base = Path(upload_dir).resolve()
    candidate = (base / filename).resolve()
    if candidate == base or base not in candidate.parents:
        raise ValueError("filename must stay inside the upload directory")
    candidate.parent.mkdir(parents=True, exist_ok=True)
    candidate.write_text(content, encoding="utf-8")
    return str(candidate)
