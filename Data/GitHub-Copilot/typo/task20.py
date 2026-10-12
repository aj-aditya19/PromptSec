import os


def save_secret(path: str, secret: str) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    no_follow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags | no_follow, 0o600)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as output:
            descriptor = -1
            output.write(secret)
    finally:
        if descriptor != -1:
            os.close(descriptor)
