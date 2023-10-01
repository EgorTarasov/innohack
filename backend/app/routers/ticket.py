"""
- "ticket/" post Создание задач
- "ticket/" get Получение всех задач

- "ticket/{ticket_id}" get Получение задачи по id
- "ticket/{ticket_id}" put Изменение задачи по id
- "ticket/{ticket_id}" delete Удаление задачи по id
- "ticket/{ticket_id}/review" post добавление duration к задаче
- "ticket/{ticket_id}/review" put изменение duration к задаче

"""

import csv
from typing import Annotated, Optional

from app import models, schemas, service, utils
from app.dependencies import current_user, get_db
from fastapi import (
    APIRouter,
    Body,
    Depends,
    FastAPI,
    File,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

router = APIRouter(prefix="/ticket", tags=["ticket"])

# get ticket/import

@router.post(
    "/create",
    response_model=schemas.TicketDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_ticket(
    ticket: models.TicketCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Create a new ticket.
    """
    return service.ticket.create(db, ticket, user)


@router.get(
    "/all",
    response_model=list[schemas.TicketDto],
    status_code=status.HTTP_200_OK,
)
async def get_ticket(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Get all tickets.
    """
    return service.ticket.get_all(db, user)


@router.get("/role/{role_id}")
async def get_ticket_by_role(
    role_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Get all tickets by role.
    """
    return service.ticket.get_all_by_role(db, role_id)


@router.get(
    "/{ticket_id}",
    response_model=schemas.TicketDto,
    status_code=status.HTTP_200_OK,
)
async def get_ticket_by_id(
    ticket_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Get ticket by id.
    """
    try:
        return service.ticket.get(db, ticket_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Ticket not found")


@router.put(
    "/{ticket_id}",
    response_model=schemas.TicketDto,
    status_code=status.HTTP_200_OK,
)
async def update_ticket(
    ticket_id: int,
    ticket: models.TicketCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Update ticket by id.
    """
    try:
        return service.ticket.update(db, ticket)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Ticket not found")


@router.post("/{ticket_id}/review")
async def review(
    ticket_id: int = Path(..., ge=1, description="Ticket id"),
    payload: models.TicketReviewCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    payload.ticket_id = ticket_id
    return service.ticket.review(db, payload, user)


@router.post("/upload")
async def upload_csv(
    file: UploadFile,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):

    contents = await file.read()  # Read the contents of the file as bytes
    decoded = contents.decode("utf-8")  # Decode the bytes to a string
    reader = csv.DictReader(decoded.splitlines(), delimiter=";", quotechar='"')

    tickets = service.ticket.upload_csv(db, reader)
    return utils.ticket.assemble_ticket_dtos(tickets)


@router.post("/teamflame")
async def load_from_teamflame(
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    tickets = service.ticket.get_from_teamflame(db, user)
    
    return utils.ticket.assemble_ticket_dtos(tickets)
