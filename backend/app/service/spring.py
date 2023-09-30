import logging

from app import models
from sqlalchemy.orm import Session


def assemble_sprint(db: Session) -> list[models.Ticket]:
    tickets = db.query(models.Ticket).filter(models.Ticket.sprint_id == None).all()
    return tickets
