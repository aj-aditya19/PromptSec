import os
from pathlib import Path


def save_secret(path: str, secret: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as secret_file:
        secret_file.write(secret)
    try:
        os.chmod(destination, 0o600)
    except OSError:
        if os.name != "nt":
            raise
