from pathlib import Path
from zipfile import ZipFile


def extract_zip(zip_path: str, dest_dir: str) -> None:
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path) as archive:
        for member in archive.infolist():
            member_path = (destination / member.filename).resolve()
            if destination not in member_path.parents and member_path != destination:
                raise ValueError("Archive contains an unsafe path")
            if member.is_dir():
                member_path.mkdir(parents=True, exist_ok=True)
            else:
                member_path.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as source, member_path.open("wb") as target:
                    target.write(source.read())
