from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db import BaseSqlModel


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

    created_tickets = relationship(
        "Ticket", back_populates="author", primaryjoin="User.id==Ticket.author_id"
    )
    taken_tickets = relationship(
        "Ticket", back_populates="worker", primaryjoin="User.id==Ticket.worker_id"
    )


class UserCreate(BaseModel):
    # define extra schema for UserCreate with example
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
