"""
Pydantic settings module.
"""

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    PG_PW: str = "changeme"
    PG_USER: str = "postgres_user"
    PG_HOST: str = "localhost"
    PG_DB: str = "postgres"


settings = Settings()
