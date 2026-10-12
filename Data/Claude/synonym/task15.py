import os
import tempfile


def make_temp_file(content: str) -> str:
    fd, path = tempfile.mkstemp(prefix="tmp_", suffix=".txt")  # created with mode 0600
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        os.unlink(path)
        raise
    return path
