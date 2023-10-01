import httpx
import logging
from pydantic import BaseModel, Field


class UserSignUp(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    password: str = Field(...)
    email: str = Field(..., description="test@test.com")


class UserDto(BaseModel):
    id: str = Field(...)
    phoneVerified: bool = Field(...)
    email: str = Field(...)
    emailVerified: bool = Field(...)
    active: bool = Field(...)
    avatar: str = Field(...)
    role: str = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    surName: str = Field(...)


class UserSignIn(BaseModel):
    email: str = Field(...)
    password: str = Field(...)


class AccessToken(BaseModel):
    accessToken: str = Field(...)
    expiresIn: int = Field(...)


class TeamFlameClient:
    def __init__(self) -> None:
        # https://auth-api.teamflame.ru/#/
        # reference to the API

        self.client = httpx.Client(
            base_url="https://auth-api.teamflame.ru/",
            headers={"Content-Type": "application/json"},
        )
        self.accessToken: None | AccessToken = None
        self.user: None | UserDto = None

    def sign_up(self, user: UserSignUp) -> UserDto | None:
        print(str(self.client.base_url) + "auth/sign-up")
        response = self.client.post(
            "auth/sign-up",
            json=user.model_dump(),
        )
        if response.status_code == 200 or response.status_code == 201:

            logging.info(response.json())

            return UserDto(**response.json())

    def sign_in(self, user: UserSignIn) -> UserDto:
        response = self.client.post(
            "auth/sign-in",
            json=user.model_dump(),
        )
        tokens = response.json()["tokens"]
        logging.info(response.json())
        self.accessToken = AccessToken(**tokens["accessToken"])
        self.user = UserDto(**response.json()["user"])
        return UserDto(**response.json()["user"])

    def refresh_token(self):
        response = self.client.post(
            "auth/refresh-token",
            json={"refreshToken": self.refreshToken},
        )
        logging.info(response.json())
        tokens = response.json()["tokens"]
        self.accessToken = tokens["accessToken"]
        self.refreshToken = tokens["refreshToken"]
        return UserDto(**response.json()["user"])

    def get_user(self):
        response = self.client.get(
            "auth/user",
            headers={"Authorization": f"Bearer {self.accessToken}"},
        )
        logging.info(response.json())
        return UserDto(**response.json())


if __name__ == "__main__":
    client = TeamFlameClient()
    user = UserSignUp(
        firstName="test",
        lastName="test",
        password="test",
        email="test9238108312098390118@test.com",
    )
    data = client.sign_up(user)
    print(data)
