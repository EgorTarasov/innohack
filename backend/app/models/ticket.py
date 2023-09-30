from datetime import datetime

from app.db import BaseSqlModel
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Ticket(BaseSqlModel):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sprint_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)
    reporter_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )
    due_date: Mapped[datetime] = mapped_column(DateTime)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))
    level_id: Mapped[int] = mapped_column(Integer, ForeignKey("levels.id"))

    role = relationship("Role")
    level = relationship("Level")

    durations = relationship("TicketReview")

    def __repr__(self):
        return f"<Ticket {self.title}>"


class TicketCreate(BaseModel):

    model_config = ConfigDict(json_schema_extra={})

    title: str = Field(...)
    description: str = Field(...)
    reporter_id: int | None = Field(None)
    assignee_id: int | None = Field(None)
    due_date: datetime | None = Field(None)
    priority: int = Field(..., ge=1, le=3)
    role_id: int = Field(...)
    level_id: int = Field(...)
