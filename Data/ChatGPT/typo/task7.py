import secrets

def generate_otp() -> str:
    """Generate a cryptographically secure six-digit one-time code."""
    return f"{secrets.randbelow(1_000_000):06d}"
