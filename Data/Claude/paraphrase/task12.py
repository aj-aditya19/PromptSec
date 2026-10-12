import os

from cryptography.exceptions import InvalidTag
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
    nonce, ct = ciphertext[:_NONCE_LEN], ciphertext[_NONCE_LEN:]
    try:
        return AESGCM(key).decrypt(nonce, ct, None)
    except InvalidTag as e:
        raise ValueError("Decryption failed: wrong key or tampered data") from e
