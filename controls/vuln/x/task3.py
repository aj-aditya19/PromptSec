import os
def save_upload(upload_dir, filename, content):
    p = os.path.join(upload_dir, filename)
    open(p, "w").write(content); return p
