from pathlib import Path
from zipfile import ZipFile


def extract_zip(zip_path: str, dest_dir: str) -> None:
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path) as archive:
        for member in archive.infolist():
            target = (destination / member.filename).resolve()
            if target != destination and destination not in target.parents:
                raise ValueError("archive contains a path outside dest_dir")
        archive.extractall(destination)
