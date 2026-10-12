from pathlib import Path
from zipfile import ZipFile
import os

def extract_zip(zip_path: str, dest_dir: str) -> None:
    """Safely extract ZIP entries while rejecting path traversal and symlinks."""
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path) as archive:
        for info in archive.infolist():
            name = info.filename
            if not name or "\x00" in name:
                raise ValueError("Invalid ZIP entry name")
            mode = info.external_attr >> 16
            if (mode & 0o170000) == 0o120000:
                raise ValueError("ZIP symlinks are not allowed")
            target = (destination / name).resolve()
            if target != destination and destination not in target.parents:
                raise ValueError("ZIP entry escapes destination directory")
        archive.extractall(destination)
