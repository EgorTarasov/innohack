from pydantic import BaseModel, Field, ConfigDict

from sqlalchemy.orm import Session, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from app.db import BaseSqlModel


class Role(BaseSqlModel):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    label: Mapped[str] = mapped_column(String, index=True)

    def __repr__(self):
        return f"<Role {self.label}>"


class RoleDto(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "label": "Frontend",
            }
        },
    )

    id: int = Field(...)
    label: str = Field(...)


class RoleCreate(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "label": "Frontend",
            }
        },
    )

    label: str = Field(...)
