from typing import Optional

from app.db import BaseSqlModel
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TicketReview(BaseSqlModel):
    __tablename__ = "ticket_reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    ticket_id: Mapped[int] = mapped_column(Integer, ForeignKey("tickets.id"))
    duration: Mapped[int] = mapped_column(Integer, default=None, nullable=True)
    reviewed: Mapped[bool] = mapped_column(Boolean, default=False)

    user = relationship(
        "User",
        foreign_keys=[user_id],
        primaryjoin="User.id==TicketReview.user_id",
    )
    # ticket = relationship("Ticket", foreign_keys=[ticket_id])


class TicketReviewCreate(BaseModel):
    ticket_id: int | None = Field(None)
    duration: int | None = Field(None)


class TicketReviewDto(BaseModel):
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
    reviewed: bool = Field(..., alias="reviewed")
