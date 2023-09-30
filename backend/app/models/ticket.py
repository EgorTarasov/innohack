from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import BaseSqlModel


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
    role_ids: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    level_id: Mapped[int] = mapped_column(Integer, ForeignKey("levels.id"))

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
    roles: list[int] = Field(...)
    level: int = Field(...)
