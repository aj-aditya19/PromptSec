import zipfile
from pathlib import Path, PurePosixPath

def extract_zip(zip_path: str, dest_dir: str) -> None:
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.infolist():
            target = (destination / PurePosixPath(member.filename)).resolve()
            if destination not in target.parents and target != destination:
                raise ValueError("Unsafe zip entry path")
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as src, target.open("wb") as dst:
                    dst.write(src.read())
