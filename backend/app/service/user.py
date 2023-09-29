from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


from sqlalchemy.orm import Session
from .. import models, crud, utils

from ..config import config
import logging


def create(db: Session, user: models.UserCreate) -> models.Token:
    """Создание пользователя

    Args:
        db (Session): сессия к бд
        user (models.UserCreate): данные пользователя

    Raises:
        Exception: Нарушение уникальности полей

    Returns:
        str: токен для авторизации (access_token)
    """

    try:
        user.password = utils.auth.get_password_hash(user.password)
        crud.create_user(db, user)
        return models.Token(
            access_token=utils.auth.create_access_token(data={"sub": user.email}),
            token_type="bearer",
        )
    except Exception as e:
        logging.error(f"Error create user: {e}")
        raise Exception(f"Error create user: {e}")


def authenticate(db: Session, payload: models.UserLogin) -> models.Token:
    """Авторизация пользователя
    """
    user = crud.get_user_by_email(db, payload.email)
    if utils.auth.verify_password(payload.password, user.hashed_password):
        return models.Token(
            access_token=utils.auth.create_access_token(data={"sub": user.email}),
            token_type="bearer",
        )
    else:
        raise Exception("Incorrect email or password")


async def get_current_user(db: Session, cookie_token: str) -> models.UserDto:
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
