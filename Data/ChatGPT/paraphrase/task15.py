import tempfile
import os

def make_temp_file(content: str) -> str:
    """Create a temporary text file and return its path; caller is responsible for cleanup."""
    fd, path = tempfile.mkstemp(prefix="shortlived_", suffix=".txt", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
    except Exception:
        try:
            os.unlink(path)
        except OSError:
            pass
        raise
    return path
