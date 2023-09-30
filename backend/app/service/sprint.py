from collections import defaultdict
import logging

from app import models, utils, crud
from sqlalchemy.orm import Session


def assemble_sprint(db: Session, sprint_create: models.SprintCreate) -> models.SprintDto:
    # get all tickets sprint_id is Null order by due_date(asc, None as inf), priority(desc)
    
    tickets = db.query(models.Ticket).filter(models.Ticket.sprint_id == None).order_by(models.Ticket.due_date.asc_nulls_last(), models.Ticket.priority.desc()).all()
    users = db.query(models.User).all()
    ticket_reviews = db.query(models.TicketReview).filter(models.TicketReview.ticket_id.in_([t.id for t in tickets]) & (models.TicketReview.duration != None)).all()

    ticket_by_id = {t.id: t for t in tickets}
    # make dict ticket_id: [(user_id, duration)]
    ticket_review_dict = defaultdict(list)
    for tr in ticket_reviews:
        ticket_review_dict[tr.ticket_id].append((tr.user_id, tr.duration))
    
    for ticket_id in ticket_review_dict.keys():
        ticket_review_dict[ticket_id].sort(key=lambda x: x[1])
    
    # assemble tickets by users
    user_hours = {}
    for user in sprint_create.users:
        user_hours[user.id] = user.hours

    user_tickets_sprint = {}

    for user_id, user in users.items():
        user_tickets_sprint[user_id] = {
            "user_data": {"id": user_id, "username": user.username, "hours": user_hours.get(user_id, 0)},
            "tickets": []
        }

    for ticket_id, (user_id, duration) in ticket_review_dict.items():
        if user_hours[user_id] >= duration:
            user_hours[user_id] -= duration
            user_tickets_sprint[user_id]["tickets"].append(utils.ticket.assemble_ticket_dto(ticket_by_id[ticket_id]))
            ticket_by_id[ticket_id].sprint_id = sprint_create.id
            ticket_by_id[ticket_id].assignee_id = user_id
            db.merge(ticket_by_id[ticket_id])
            db.commit()
        else:
            logging.warning(f"User {user_id} has not enough hours to complete ticket {ticket_id}")
    

    sprint = models.SprintDto(
        id=sprint_create.id,
        duration=sprint_create.duration,
        target=sprint_create.target,
        is_finished=False,
        users=user_tickets_sprint
    )

    sprint = crud.sprint.create(db, sprint)

    return sprint
