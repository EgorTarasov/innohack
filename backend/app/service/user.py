from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


from sqlalchemy.orm import Session
from app import models
from app import crud
from app.config import config
import logging


async def get_current_user(db: Session, cookie_token: str) -> models.User:
    """ "Получение текущего пользователя"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials {e}",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            str(cookie_token), config.SECRET_KEY, algorithms=[config.ALGORITHM]
        )
        email: str = payload.get("sub")  # type: ignore
        if email is None:
            logging.debug(f"email is None")
            raise credentials_exception
        token_data = models.TokenData(email=email)
    except JWTError as e:
        logging.debug(f"JWTError: {e}")
        raise credentials_exception
    if not token_data.email:
        logging.debug(f"token_data.email is None")
        raise credentials_exception
    user = crud.get_user_by_email(db, token_data.email)
    if user is None:
        logging.debug(f"User no found")
        raise credentials_exception
    return user
