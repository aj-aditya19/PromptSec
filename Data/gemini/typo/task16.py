import os
import zipfile

def extract_zip(zip_path: str, dest_dir: str) -> None:
    dest_path = os.path.abspath(dest_dir)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            target_path = os.path.abspath(os.path.join(dest_path, member.filename))
            if not target_path.startswith(dest_path + os.sep):
                raise ValueError("Illegal path in zip file.")
        zip_ref.extractall(dest_path)
