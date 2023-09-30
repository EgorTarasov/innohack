from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str = "Bearer"
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
