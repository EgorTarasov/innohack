import logging
from typing import Type
from sqlalchemy.orm import Session

from app import models


def create(db: Session, payload: models.TicketCreate) -> models.Ticket:

    ticket = models.Ticket(
        title=payload.title,
        description=payload.description,
        reporter_id=payload.reporter_id,
        assignee_id=payload.assignee_id,
        due_date=payload.due_date,
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
    return db.query(models.Ticket).all()


def get_backlog(
    db: Session,
) -> list[models.Ticket]:
    return db.query(models.Ticket).filter(models.Ticket.sprint_id == None).all()
