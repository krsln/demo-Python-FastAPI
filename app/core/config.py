from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App info
    PROJECT_NAME: str = Field(default="Demo Python FastAPI")
    VERSION: str = Field(default="1.0.0")
    ENV: str = Field(default="dev")

    # Server config
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    # Database config
    DB_USER: str = Field(default="postgres")
    DB_PASSWORD: str = Field(default="postgres")
    DB_HOST: str = Field(default="localhost")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="fastapi_db")

    @property
    def DATABASE_URL(self) -> str:
        """Builds the full database connection string."""
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
