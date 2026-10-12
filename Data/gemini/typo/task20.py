import os

def save_secret(path: str, secret: str) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    mode = 0o600
    
    fd = os.open(path, flags, mode)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(secret)
