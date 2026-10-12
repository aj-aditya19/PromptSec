import tempfile
import os

def make_temp_file(content: str) -> str:
    fd, path = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        os.remove(path)
        raise
    return path
