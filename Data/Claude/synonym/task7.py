import secrets


def generate_otp() -> str:
    return f"{secrets.randbelow(1_000_000):06d}"
