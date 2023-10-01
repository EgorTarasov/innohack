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

    SERVICE_MAIL_USER=misis.larek.deda@mail.ru
    SERVICE_MAIL_PASSWORD=3TRtoPT3y*ap
    SERVICE_MAIL_HOST=smtp.mail.ru
    SERVICE_MAIL_PORT=587

    LE_EMAIL=test@test.com
    CF_API_EMAIL=SHSHS
    CF_API_KEY=SHSHS
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

    SERVICE_MAIL_USER: str
    SERVICE_MAIL_PASSWORD: str
    SERVICE_MAIL_HOST: str
    SERVICE_MAIL_PORT: int

    LE_EMAIL: str
    CF_API_EMAIL: str
    CF_API_KEY: str


config = Config()  # type: ignore
