import os
import tempfile

def make_temp_file(content: str) -> str:
    fd, path = tempfile.mkstemp(prefix="short_lived_", suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    return path
