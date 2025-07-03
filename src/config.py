"""
Configuration settings for the Mergington High School Activities API
"""
import os
from typing import List


class Settings:
    """Application settings loaded from environment variables"""
    
    APP_NAME: str = "Mergington High School Activities API"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080", 
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ]
    
    # Future database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # Security settings for future use
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


settings = Settings()
