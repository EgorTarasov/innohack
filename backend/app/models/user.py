from datetime import datetime

from app.db import BaseSqlModel
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(BaseSqlModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    created_tickets = relationship("Ticket", primaryjoin="User.id==Ticket.reporter_id")
    assigned_tickets = relationship("Ticket", primaryjoin="User.id==Ticket.assignee_id")

    def __repr__(self):
        return f"<User {self.email}>"


class UserCreate(BaseModel):
    # TODO: add assigned_tickets
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "test@test.com",
                "username": "test",
                "password": "test",
            }
        }
    )

    email: str
    username: str
    password: str


class UserLogin(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={"example": {"email": "test@test.com", "password": "test"}}
    )

    email: str
    password: str


class UserDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., alias="id")
    email: str = Field(..., alias="email")
    username: str = Field(..., alias="username")
    is_active: bool = Field(..., alias="is_active")
    is_superuser: bool = Field(..., alias="is_superuser")
    created_at: datetime = Field(..., alias="created_at")
    updated_at: datetime = Field(..., alias="updated_at")
