import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
def encrypt_data(key, plaintext):
    n = os.urandom(12); return n + AESGCM(key).encrypt(n, plaintext, None)
def decrypt_data(key, ciphertext): return AESGCM(key).decrypt(ciphertext[:12], ciphertext[12:], None)
