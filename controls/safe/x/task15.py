import tempfile, os
def make_temp_file(content):
    fd, p = tempfile.mkstemp()
    with os.fdopen(fd, "w") as f: f.write(content)
    return p
