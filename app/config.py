from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    APP_NAME: str = "GymAPI"
    DB_URL: str
    DEBUG: bool = True

    model_config = SettingsConfigDict(env_file=".env")

config = Config()