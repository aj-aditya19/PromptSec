import os
import stat
from pathlib import Path


def save_secret(path: str, secret: str) -> None:
    secret_path = Path(path)
    secret_path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    mode = stat.S_IRUSR | stat.S_IWUSR
    file_descriptor = os.open(secret_path, flags, mode)
    try:
        with os.fdopen(file_descriptor, "w", encoding="utf-8") as secret_file:
            file_descriptor = -1
            secret_file.write(secret)
    finally:
        if file_descriptor != -1:
            os.close(file_descriptor)
