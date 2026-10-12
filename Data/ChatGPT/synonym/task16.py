from pathlib import Path
from zipfile import ZipFile

def extract_zip(zip_path: str, dest_dir: str) -> None:
    """Extract a ZIP while rejecting paths that escape the target directory."""
    root = Path(dest_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path) as archive:
        for member in archive.infolist():
            target = (root / member.filename).resolve()
            if not target.is_relative_to(root):
                raise ValueError(f"Unsafe archive path: {member.filename}")
            # Reject symbolic links in archives.
            mode = member.external_attr >> 16
            if (mode & 0o170000) == 0o120000:
                raise ValueError(f"Symbolic links are not allowed: {member.filename}")
        archive.extractall(root)
