import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


SECRET = os.getenv('SECRET')
ALGORITHM = os.getenv('ALGORITHM')


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}"

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='allow'
    )


settings = Settings()


def get_auth_data():
    return {"secret_key": SECRET, "algorithm": ALGORITHM}