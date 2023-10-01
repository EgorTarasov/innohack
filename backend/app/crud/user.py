from sqlalchemy.orm import Session

from .. import models


def create_user(db: Session, payload: models.UserCreate) -> models.User:
    """Создание пользователя"""
    db_user = models.User(
        email=payload.email,
        username=payload.username,
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


def get_all(db: Session) -> list[models.User]:
    """Получение всех пользователей"""
    users = (
        db.query(models.User)
        .filter(models.User.id.in_(db.query(models.TicketReview.user_id.distinct())))
        .all()
    )
    return users
