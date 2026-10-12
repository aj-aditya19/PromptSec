import os
def read_upload(upload_dir, filename):
    return open(os.path.join(upload_dir, filename)).read()
