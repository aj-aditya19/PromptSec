import zipfile, os
def extract_zip(zip_path, dest_dir):
    with zipfile.ZipFile(zip_path) as z:
        for n in z.namelist():
            p = os.path.join(dest_dir, n); os.makedirs(os.path.dirname(p), exist_ok=True)
            if not n.endswith("/"): open(p, "wb").write(z.read(n))
