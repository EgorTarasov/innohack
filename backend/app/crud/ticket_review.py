import logging
from typing import Type
from sqlalchemy.orm import Session

from app import models


def create(
    db: Session, payload: models.TicketReviewCreate, reviewer: models.User
) -> models.TicketReviewDto:
    review = models.TicketReview(
        user_id=reviewer.id,
        ticket_id=payload.ticket_id,
        duration=payload.duration,
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return models.TicketReviewDto.model_validate(review)


def get_by_id(db: Session, ticket_review_id: int) -> models.TicketReview:
    db_review = (
        db.query(models.TicketReview)
        .filter(models.TicketReview.id == ticket_review_id)
        .one_or_none()
    )
    if not db_review:
        raise Exception(f"TicketReview with id {ticket_review_id} not found")
    return db_review


def get_users_reviews(db: Session, user_id: int) -> list[models.TicketReviewDto]:
    return [
        models.TicketReviewDto.model_validate(review)
        for review in db.query(models.TicketReview)
        .filter(
            (models.TicketReview.user_id == user_id)
            & (models.TicketReview.reviewed == True)
        )
        .all()
    ]
