import logging

from app import models
from sqlalchemy.orm import Session


def assemble_sprint(db: Session, sprint_create: models.SprintCreate) -> list[models.Ticket]:
    tickets = db.query(models.Ticket).filter(models.Ticket.sprint_id == None).all()
    users = db.query(
    return tickets
