from pathlib import Path
from zipfile import ZipFile
import shutil

def extract_zip(zip_path: str, dest_dir: str) -> None:
    """Extract ZIP entries only when each resolved target stays inside dest_dir."""
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path) as archive:
        for info in archive.infolist():
            target = (destination / info.filename).resolve()
            if not target.is_relative_to(destination):
                raise ValueError(f"Unsafe ZIP entry: {info.filename}")
            # Reject symbolic links rather than creating filesystem links.
            mode = (info.external_attr >> 16) & 0o170000
            if mode == 0o120000:
                raise ValueError(f"Symbolic links are not allowed: {info.filename}")
        archive.extractall(destination)
