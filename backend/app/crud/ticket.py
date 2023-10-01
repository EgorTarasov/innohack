import logging
from typing import Type

from app import models
from sqlalchemy.orm import Session


def create(db: Session, payload: models.TicketCreate) -> models.Ticket:

    ticket = models.Ticket(
        title=payload.title,
        description=payload.description,
        reporter_id=payload.reporter_id,
        assignee_id=payload.assignee_id,
        due_date=payload.due_date,
        role_id=payload.role_id,
        level_id=payload.level_id,
        priority=payload.priority,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def update(db: Session, payload: models.TicketCreate) -> models.Ticket:
    ticket = models.Ticket(
        title=payload.title,
        description=payload.description,
        reporter_id=payload.reporter_id,
        assignee_id=payload.assignee_id,
        due_date=payload.due_date,
    )
    db.merge(ticket)
    db.refresh(ticket)
    return ticket


def get(db: Session, id: int) -> models.Ticket:

    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).one_or_none()

    if not ticket:
        logging.error(f"Ticket with id {id} not found")
        raise Exception(f"Ticket with id {id} not found")
    return ticket


def get_all(db: Session) -> list[models.Ticket]:
    """Получение задач из бэклога
    задача считается не распределенной, если у нее нет sprint_id

    Args:
        db (Session): Сессия подключения к бд

    Returns:
        list[models.Ticket]: бэклог
    """
    return db.query(models.Ticket).filter(models.Ticket.sprint_id == None).all()


def get_all_by_role(db: Session, role_id: int) -> list[models.Ticket]:
    return (
        db.query(models.Ticket)
        .filter((models.Ticket.sprint_id == None) & (models.Ticket.role_id == role_id))
        .all()
    )


def get_backlog(
    db: Session,
) -> list[models.Ticket]:
    return db.query(models.Ticket).filter(models.Ticket.sprint_id == None).all()


def bulk_create(db: Session, tickets: list[models.Ticket]) -> list[models.Ticket]:
    # length = len(tickets)
    db.add_all(tickets)

    db.commit()
    for ticket in tickets:
        db.refresh(ticket)

    return tickets
