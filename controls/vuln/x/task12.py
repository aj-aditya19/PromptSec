from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def _pad(b): n = 16 - len(b) % 16; return b + bytes([n]) * n
def encrypt_data(key, plaintext):
    e = Cipher(algorithms.AES(key), modes.ECB()).encryptor(); return e.update(_pad(plaintext)) + e.finalize()
def decrypt_data(key, ciphertext):
    d = Cipher(algorithms.AES(key), modes.ECB()).decryptor(); p = d.update(ciphertext) + d.finalize(); return p[:-p[-1]]
