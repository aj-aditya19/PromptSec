import os

def save_secret(path: str, secret: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(secret)
    # Set restrictive file permissions (read/write only by owner)
    os.chmod(path, 0o600)
