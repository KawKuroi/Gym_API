from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "GymAPI"
    DB_URL: str
    DEBUG: bool = True
    SENTRY_KEY: str | None = None
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
