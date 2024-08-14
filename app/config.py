import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    OPENAI_TOKEN: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '..', '.env')


settings = Settings()
