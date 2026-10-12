import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)

def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    nonce, encrypted = ciphertext[:12], ciphertext[12:]
    return AESGCM(key).decrypt(nonce, encrypted, None)
