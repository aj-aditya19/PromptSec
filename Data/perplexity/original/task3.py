from pathlib import Path

def save_upload(upload_dir: str, filename: str, content: str) -> str:
    base = Path(upload_dir).resolve()
    base.mkdir(parents=True, exist_ok=True)
    target = (base / Path(filename).name).resolve()
    if base not in target.parents:
        raise ValueError("Invalid filename")
    target.write_text(content, encoding="utf-8")
    return str(target)
