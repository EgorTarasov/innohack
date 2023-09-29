from .. import models
from sqlalchemy.orm import Session


def create_user(db: Session, payload: models.UserCreate) -> models.User:
    """Создание пользователя"""
    db_user = models.User(
        email=payload.email,
        hashed_password=payload.password,
        is_active=True,
        is_superuser=False,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str) -> models.User:
    """Получение пользователя по email"""
    print(email)
    user = db.query(models.User).where(models.User.email == email).one_or_none()
    if user:

        return user

    else:
        raise Exception("User not found")
