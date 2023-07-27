"""App settings."""

from decouple import config
from pydantic import BaseSettings

VERSION_CODE = (0, 0, 2)

class Settings(BaseSettings):
    """Basic settings for the application."""

    # Application
    TITLE: str = "Loan Managment System"
    VERSION: str = ".".join(map(str, VERSION_CODE))
    DESCRIPTION: str = "Loan Managment System for personal use"

    DEBUG: bool = config("DEBUG", default=False)

    # Database
    DATABASE_URL: str = config("MONGODB_URI")
    MONGO_URI: str = config("MONGODB_URI")

    # JWT
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY')
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MIN: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MIN: int = 60 * 24 * 7  # 7 days

    class Config:
        # env_file = ".env.dev"
        orm_mode = True


settings = Settings()
