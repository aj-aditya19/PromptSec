import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

_NONCE_LEN = 12


def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes")
    nonce = os.urandom(_NONCE_LEN)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)


def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes")
    if len(ciphertext) < _NONCE_LEN + 16:
        raise ValueError("Ciphertext too short")
    nonce, data = ciphertext[:_NONCE_LEN], ciphertext[_NONCE_LEN:]
    return AESGCM(key).decrypt(nonce, data, None)  # raises InvalidTag if tampered
