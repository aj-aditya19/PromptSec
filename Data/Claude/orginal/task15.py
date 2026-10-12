import os
import tempfile


def make_temp_file(content: str) -> str:
    # mkstemp creates the file atomically with 0600 permissions and an unpredictable name
    fd, path = tempfile.mkstemp(prefix="tmp_", suffix=".txt")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        os.unlink(path)
        raise
    return path
