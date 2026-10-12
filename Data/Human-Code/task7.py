import random

def generate_otp() -> str:    
    otp = random.randint(100000, 999999)
    return str(otp)