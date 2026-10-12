import secrets

def generate_otp() -> str:
    """Generate a cryptographically secure six-digit OTP, including leading zeroes."""
    return f"{secrets.randbelow(1_000_000):06d}"
