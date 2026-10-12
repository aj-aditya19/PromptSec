import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def _check_key(key: bytes) -> None:
    if not isinstance(key, (bytes, bytearray)) or len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes")


def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    _check_key(key)
    nonce = os.urandom(12)  # unique per message
    ct = AESGCM(bytes(key)).encrypt(nonce, plaintext, None)
    return nonce + ct


def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    _check_key(key)
    if len(ciphertext) < 12 + 16:
        raise ValueError("Ciphertext too short")
    nonce, ct = ciphertext[:12], ciphertext[12:]
    # Raises InvalidTag if tampered with or wrong key
    return AESGCM(bytes(key)).decrypt(nonce, ct, None)
