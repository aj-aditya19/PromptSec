import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def _check_key(key: bytes) -> None:
    if not isinstance(key, bytes) or len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes")


def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    _check_key(key)
    nonce = os.urandom(12)  # fresh random nonce for every message
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)


def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    _check_key(key)
    if len(ciphertext) < 12 + 16:
        raise ValueError("Ciphertext too short")
    nonce, body = ciphertext[:12], ciphertext[12:]
    return AESGCM(key).decrypt(nonce, body, None)  # raises InvalidTag if tampered
