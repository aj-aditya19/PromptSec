import zipfile

def extract_zip(zip_path: str, dest_dir: str) -> None:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)
