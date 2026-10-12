import secrets
def generate_otp(): return f"{secrets.randbelow(10**6):06d}"
