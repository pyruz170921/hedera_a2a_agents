# backend/utils/encryption.py
"""
AES-GCM encrypt/decrypt helpers. Entrada y salida en base64 string.
"""
import base64, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM  # ← Corrección aquí

def encrypt_message(plaintext: str, key_b64: str) -> str:
    key = base64.b64decode(key_b64)
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ct = aes.encrypt(nonce, plaintext.encode(), None)
    return base64.b64encode(nonce + ct).decode()

def decrypt_message(payload_b64: str, key_b64: str) -> str:
    key = base64.b64decode(key_b64)
    data = base64.b64decode(payload_b64)
    nonce, ct = data[:12], data[12:]
    aes = AESGCM(key)
    return aes.decrypt(nonce, ct, None).decode()
