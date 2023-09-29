from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column


from .config import config

engine = create_engine(
    f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
    f"{config.POSTGRES_SERVER}/{config.POSTGRES_DB}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class BaseSqlModel(Base):
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
