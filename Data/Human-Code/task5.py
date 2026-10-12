import hashlib

def hash_password(password: str) -> str:
    salt = "my_salt"
    password_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return password_hash


def verify_password(password: str, stored: str) -> bool:
    return hash_password(password) == stored