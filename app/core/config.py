from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "LeadSense"
    Database_URL: str = "sqlite+aiosqlite:///./leadsense.db"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()