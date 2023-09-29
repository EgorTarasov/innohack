from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    LOGGING_LEVEL=debug

    POSTGRES_ADMIN_EMAIL=test@test.com
    POSTGRES_ADMIN_PASSWORD=test1234
    POSTGRES_SERVER=localhost
    POSTGRES_USER=test
    POSTGRES_PASSWORD=test123
    POSTGRES_DB=dev

    PROJECT_NAME=InnoHackBackend
    DOMAIN=localhost

    SECRET_KEY=sfhagskjhfkjqwhrkhdskajfhaksdjhfaskjnvjkanjknjkfnasjkfnasdkjfn
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    """

    model_config = SettingsConfigDict(env_file=".env")

    LOGGING_LEVEL: str
    POSTGRES_ADMIN_EMAIL: str
    POSTGRES_ADMIN_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    PROJECT_NAME: str
    DOMAIN: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


config = Config()  # type: ignore
