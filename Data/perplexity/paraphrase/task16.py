import os
import zipfile

def extract_zip(zip_path: str, dest_dir: str) -> None:
    os.makedirs(dest_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.namelist():
            target = os.path.realpath(os.path.join(dest_dir, member))
            if not target.startswith(os.path.realpath(dest_dir) + os.sep):
                raise ValueError("Unsafe zip entry detected")
        archive.extractall(dest_dir)
