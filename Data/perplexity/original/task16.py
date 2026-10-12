from pathlib import Path
import zipfile

def extract_zip(zip_path: str, dest_dir: str) -> None:
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.infolist():
            target = (destination / member.filename).resolve()
            if destination not in target.parents and target != destination:
                raise ValueError("Unsafe zip entry")
        archive.extractall(destination)
