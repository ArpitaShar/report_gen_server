from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "Report Generator API"
    API_PREFIX: str = "/api"
    ENV: str = "dev"
    PORT: int = 8011

    # storage
    DATA_DIR: str = "./data"
    REPORTS_DIR: str = "./data/reports"

    # CORS
    ALLOW_ORIGINS: str = "http://localhost:5173"

    # Auth
    API_KEY: str = "change-me"

    # DB (optional)
    DATABASE_URL: str | None = None

    # LLM / Agents
    OLLAMA_BASE_URL: str | None = "http://localhost:11434"
    LLM_MODEL: str = "llama3.1:8b"  # any local model in Ollama
    MAX_TOKENS: int = 2048
    TEMPERATURE: float = 0.2

    # Web search
    SEARCH_MAX_RESULTS: int = 5

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

Path(settings.DATA_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.REPORTS_DIR).mkdir(parents=True, exist_ok=True)
