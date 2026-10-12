import hashlib, os, hmac
def hash_password(password):
    s = os.urandom(16); d = hashlib.pbkdf2_hmac("sha256", password.encode(), s, 200000)
    return s.hex() + "$" + d.hex()
def verify_password(password, stored):
    s, d = stored.split("$"); n = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(s), 200000)
    return hmac.compare_digest(n.hex(), d)
