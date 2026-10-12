import os
def save_upload(upload_dir, filename, content):
    base = os.path.realpath(upload_dir); p = os.path.realpath(os.path.join(base, os.path.basename(filename)))
    if os.path.commonpath([base, p]) != base: raise ValueError("bad path")
    open(p, "w").write(content); return p
