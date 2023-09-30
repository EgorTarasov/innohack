from app import models
from sqlalchemy.orm import Session


def create(db: Session, payload: models.RoleCreate) -> models.Role:
    """Создание роли

    Args:
        db (Session): сессия к бд
        payload (models.RoleCreate): данные роли

    Returns:
        models.RoleDto: данные роли
    """
    db_role = models.Role(label=payload.label)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get(db: Session, _id: int) -> models.Role:
    """Получение роли по id

    Args:
        db (Session): сессия к бд
        _id (int): id роли

    Returns:
        models.RoleDto: данные роли
    """
    db_role = db.query(models.Role).filter(models.Role.id == _id).one_or_none()
    if not db_role:
        raise Exception(f"Role with id {_id} not found")
    return db_role


def get_all(db: Session) -> list[models.Role]:
    """Получение всех ролей

    Args:
        db (Session): сессия к бд

    Returns:
        list[models.RoleDto]: список ролей
    """
    return db.query(models.Role).all()
