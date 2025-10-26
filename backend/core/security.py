# backend/core/security.py
from passlib.context import CryptContext
from typing import Tuple
import os, base64

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_ctx.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)

# Helper para generar AES key (usar una vez y colocar en .env)
def generate_aes_key_b64() -> str:
    key = os.urandom(32)  # 256 bits
    return base64.b64encode(key).decode()
