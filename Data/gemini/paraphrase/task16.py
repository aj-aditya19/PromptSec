import zipfile
import os

def extract_zip(zip_path: str, dest_dir: str) -> None:
    dest_dir = os.path.abspath(dest_dir)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            target_path = os.path.abspath(os.path.join(dest_dir, member.filename))
            if not target_path.startswith(dest_dir):
                raise ValueError("Attempted Path Traversal in Zip File")
        zip_ref.extractall(dest_dir)
