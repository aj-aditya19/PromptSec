def save_secret(path: str, secret: str) -> None:
    with open(path, "w") as f:
        f.write(secret)