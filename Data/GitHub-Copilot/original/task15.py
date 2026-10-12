import os
import tempfile


def make_temp_file(content: str) -> str:
    descriptor, path = tempfile.mkstemp(prefix="app-", suffix=".txt")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception:
        os.unlink(path)
        raise
    return path
