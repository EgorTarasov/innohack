from collections import defaultdict
import logging

from app import models
from sqlalchemy.orm import Session


def assemble_sprint(db: Session, sprint_create: models.SprintCreate) -> models.SprintDto:
    # get all tickets sprint_id is Null order by due_date(asc, None as inf), priority(desc)
    
    tickets = db.query(models.Ticket).filter(models.Ticket.sprint_id == None).order_by(models.Ticket.due_date.asc_nulls_last(), models.Ticket.priority.desc()).all()
    users = db.query(models.User).all()
    ticket_reviews = db.query(models.TicketReview).filter(models.TicketReview.ticket_id.in_([t.id for t in tickets]) & (models.TicketReview.duration != None)).all()

    # make dict ticket_id: [(user_id, duration)]
    ticket_review_dict = defaultdict(list)
    for tr in ticket_reviews:
        ticket_review_dict[tr.ticket_id].append((tr.user_id, tr.duration))
    
    for ticket_id in ticket_review_dict.keys():
        ticket_review_dict[ticket_id].sort(key=lambda x: x[1])
    
    # assemble tickets by users
    user_tickets = defaultdict(list)
    for ticket in tickets:
        if ticket.id in ticket_review_dict:
            user_id, _ = ticket_review_dict[ticket.id][0]
            user_tickets[user_id].append(ticket)
        else:
            user_tickets[None].append(ticket)

    return user_tickets
