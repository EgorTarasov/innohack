from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import BaseSqlModel


class Ticket(BaseSqlModel):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sprint_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    title: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String, unique=True, index=True)
    reporter_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )
    due_date: Mapped[datetime] = mapped_column(DateTime)
    duration: Mapped[int] = mapped_column(Integer)


    def __repr__(self):
        return f"<Ticket {self.title}>"


class TicketCreate(BaseModel):
    # define extra schema for TicketCreate with example
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "test",
                "description": "test",
                "reporter_id": 1,
                "assignee_id": 2,
                "due_date": "2021-01-01",
                "duration": 1,
            }
        }
    )

    title: str = Field(...)
    description: str = Field(...)
    reporter_id: int | None = Field(None)
    assignee_id: int | None = Field(None)
    due_date: datetime | None = Field(None)
    duration: int | None = Field(None)


class TicketDto(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "sprint_id": 1,
                "title": "test",
                "description": "test",
                "reporter_id": 1,
                "assignee_id": 2,
                "due_date": "2021-01-01",
                "duration": 1,
            }
        },
    )

    id: int = Field(..., alias="id")
    sprint_id: int | None = Field(None, alias="sprint_id")
    title: str = Field(..., alias="title")
    description: str = Field(..., alias="description")
    reporter_id: int = Field(..., alias="reporter_id")
    assignee_id: int | None = Field(None, alias="assignee_id")
    due_date: datetime = Field(..., alias="due_date")
    duration: int = Field(..., alias="duration")


class UserTicket(BaseSqlModel):
    __tablename__ = "user_tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    ticket_id: Mapped[int] = mapped_column(Integer, ForeignKey("tickets.id"))
    duration: Mapped[int] = mapped_column(Integer, default=None, nullable=True)
    reviewed: Mapped[bool] = mapped_column(Boolean, default=False)

    user = relationship(
        "User",
        foreign_keys=[user_id],
        backref="backlogged_tickets",
        primaryjoin="User.id==UserTicket.user_id",
    )
    ticket = relationship(
        "Ticket", foreign_keys=[ticket_id], backref="backlogged_users"
    )


class UserTicketCreate(BaseModel):
    duration: int | None = Field(None)


class UserTicketDto(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "user_id": 1,
                "ticket_id": 1,
                "duration": None,
                "revieved": True,
            }
        },
    )

    id: int = Field(..., alias="id")
    user_id: int = Field(..., alias="user_id")
    ticket_id: int = Field(..., alias="ticket_id")
    duration: int | None = Field(None, alias="duration")
    reviewed: bool = Field(..., alias="revieved")
