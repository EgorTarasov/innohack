from fastapi import Cookie, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal
import logging
from . import models, service, utils



# from app.service.auth import get_current_user
# from app.utils.logging import log
# from app.data import models


def get_db():
    with SessionLocal() as db:
        yield db


async def current_user(
    db: Session = Depends(get_db),
    access_token: str | None = Depends(utils.auth.oauth2_scheme),
) -> models.User:
    logging.debug(id(db))
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated (current_user)",
        )
    return await service.user.get_current_user(db, access_token)
