from pathlib import Path
import shutil
import zipfile


def extract_zip(zip_path: str, dest_dir: str) -> None:
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.infolist():
            member_path = Path(member.filename)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise ValueError("zip member escapes destination")
            if (member.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("symbolic links are not allowed")
            target = (destination / member.filename).resolve()
            if target != destination and destination not in target.parents:
                raise ValueError("zip member escapes destination")
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as source, target.open("wb") as output:
                shutil.copyfileobj(source, output)
