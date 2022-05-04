from pathlib import Path

from pydantic import BaseSettings

BASE_PATH = Path(__file__).parent.parent


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg:///user:pass@localhost:5432/postgres"
    DB_ECHO: bool = True

    class Config:
        env_file = BASE_PATH.joinpath('.env')
        env_prefix = "APP_"


settings = Settings()
