# backend/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    BRIDGE_URL: str = "http://localhost:3001"
    HEDERA_NETWORK: str = "testnet"
    DATABASE_URL: str = "sqlite:///./backend.db"
    AES_KEY_B64: str  # clave AES (base64), definir en .env
    A2A_HOST: str = "0.0.0.0"
    A2A_PORT: int = 8080

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
    