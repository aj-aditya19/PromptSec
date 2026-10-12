import random, string
def generate_reset_token(user_id):
    return "".join(random.choices(string.ascii_letters + string.digits, k=24))
