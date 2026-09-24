from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://qauser:qapass@localhost:5432/platformone"

    # Redis
    redis_url: str = "redis://localhost:6379"

    # External Services
    cnpj_qa_url: str = "http://localhost:8000"
    fabrica_backend_url: str = "http://localhost:3000"
    fabrica_frontend_url: str = "http://localhost:5173"

    # Platform-One
    host: str = "0.0.0.0"
    port: int = 8001
    debug: bool = False

    # CORS
    cors_origins: list = ["http://localhost:5173", "http://localhost:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()