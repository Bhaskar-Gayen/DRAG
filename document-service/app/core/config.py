from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    HOST: str
    PORT: int
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding='utf-8')


settings = Settings()
print(settings.PORT)
