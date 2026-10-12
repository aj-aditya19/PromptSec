import secrets


def generate_otp() -> str:
    return f"{secrets.randbelow(10**6):06d}"
