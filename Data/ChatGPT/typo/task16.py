from pathlib import Path
from zipfile import ZipFile

def extract_zip(zip_path: str, dest_dir: str) -> None:
    """Extract a ZIP while rejecting path traversal, symlinks, and special files."""
    destination = Path(dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    base = destination
    with ZipFile(zip_path) as archive:
        for info in archive.infolist():
            name = info.filename
            if not name or "\\x00" in name:
                raise ValueError("Invalid ZIP entry")
            target = (base / name).resolve()
            if not target.is_relative_to(base):
                raise ValueError("ZIP entry escapes destination directory")
            mode = info.external_attr >> 16
            file_type = mode & 0o170000
            if file_type == 0o120000 or (file_type not in (0, 0o040000, 0o100000)):
                raise ValueError("ZIP contains a symlink or special file")
            if info.file_size > 100 * 1024 * 1024:
                raise ValueError("ZIP entry exceeds the 100 MiB limit")
        archive.extractall(base)
