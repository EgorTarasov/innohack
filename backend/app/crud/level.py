from sqlalchemy.orm import Session
from app import crud, models


def create(db: Session, payload: models.LevelCreate) -> models.Level:
    """Создание уровня

    Args:
        db (Session): сессия к бд
        payload (models.LevelCreate): данные уровня

    Returns:
        models.LevelDto: данные уровня
    """
    db_level = models.Level(
        label=payload.label,
    )
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level


def get(db: Session, _id: int) -> models.Level:
    db_level = db.query(models.Level).filter(models.Level.id == _id).first()
    if not db_level:
        raise Exception(f"Level {_id} not found")
    return db_level


def get_all(db: Session) -> list[models.Level]:
    return db.query(models.Level).all()
