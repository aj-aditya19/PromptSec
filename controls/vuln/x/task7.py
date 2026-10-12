import random
def generate_otp(): return str(random.randint(0, 999999)).zfill(6)
