import os
def read_upload(upload_dir, filename):
    base = os.path.realpath(upload_dir); p = os.path.realpath(os.path.join(base, filename))
    if os.path.commonpath([base, p]) != base: raise ValueError("bad path")
    return open(p).read()
