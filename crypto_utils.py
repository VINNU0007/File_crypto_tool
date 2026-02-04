import os
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

BACKEND = default_backend()
ITERATIONS = 100000


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits
        salt=salt,
        iterations=ITERATIONS,
        backend=BACKEND
    )
    return kdf.derive(password.encode())


def encrypt_file(input_path, output_path, password):
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = derive_key(password, salt)

    with open(input_path, "rb") as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=BACKEND)
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_path, "wb") as f:
        f.write(salt + iv + encrypted)


def decrypt_file(input_path, output_path, password):
    with open(input_path, "rb") as f:
        content = f.read()

    salt = content[:16]
    iv = content[16:32]
    encrypted_data = content[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=BACKEND)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(plaintext)
