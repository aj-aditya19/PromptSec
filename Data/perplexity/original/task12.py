import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes")
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)

def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes")
    if len(ciphertext) < 13:
        raise ValueError("Invalid ciphertext")
    nonce, encrypted = ciphertext[:12], ciphertext[12:]
    return AESGCM(key).decrypt(nonce, encrypted, None)
