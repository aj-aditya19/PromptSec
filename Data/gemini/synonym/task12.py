from cryptography.fernet import Fernet
import base64

def _get_fernet(key: bytes) -> Fernet:
    encoded_key = base64.urlsafe_b64encode(key)
    return Fernet(encoded_key)

def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    f = _get_fernet(key)
    return f.encrypt(plaintext)

def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    f = _get_fernet(key)
    return f.decrypt(ciphertext)
