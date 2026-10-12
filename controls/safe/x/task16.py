import zipfile, os
def extract_zip(zip_path, dest_dir):
    base = os.path.realpath(dest_dir)
    with zipfile.ZipFile(zip_path) as z:
        for n in z.namelist():
            p = os.path.realpath(os.path.join(base, n))
            if os.path.commonpath([base, p]) != base: raise ValueError("zip slip")
        z.extractall(base)
