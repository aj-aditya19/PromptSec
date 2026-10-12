import os
import tempfile

def make_temp_file(content: str) -> str:
    """Write content to a securely created temporary UTF-8 file and return its path."""
    fd, path = tempfile.mkstemp(prefix="upload_", suffix=".txt")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception:
        try:
            os.unlink(path)
        except OSError:
            pass
        raise
    return path
