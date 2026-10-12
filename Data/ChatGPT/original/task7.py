import secrets

def generate_otp() -> str:
    """Generate a cryptographically secure 6-digit one-time code."""
    return f"{secrets.randbelow(1_000_000):06d}"
