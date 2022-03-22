from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    DATABASE_USERNAME: str
    OATH_SECRET_KEY: str

    class Config:
        env_file = "/home/bismutoso/PycharmProjects/FastAPI_Example/Config/.env"


settings = Settings()
