from cryptography.fernet import Fernet

def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(plaintext)
    return encrypted_data

def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data
