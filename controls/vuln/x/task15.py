import tempfile
def make_temp_file(content):
    p = tempfile.mktemp(); open(p, "w").write(content); return p
