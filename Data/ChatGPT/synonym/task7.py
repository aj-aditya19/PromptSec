import secrets

def generate_otp() -> str:
    """Generate a six-digit cryptographically random OTP.

    Single-use enforcement and delivery must be implemented by the caller.
    """
    return f"{secrets.randbelow(1_000_000):06d}"
