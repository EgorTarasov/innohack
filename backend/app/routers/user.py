import logging
from typing import Annotated
from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    status,
    Response,
    Request,
    Body,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.dependencies import get_db, current_user
from app import service, models, config


router = APIRouter(prefix="/user", tags=["user"])

access_cookie_params = {
    "key": "access_token",
    "value": None,
    "secure": True,
    "samesite": "none",
    "httponly": True,
    "max_age": 60 * 60 * 24 * 30,
}


@router.post(
    "/",
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: models.UserCreate = Body(...),
    db: Session = Depends(get_db),
):
    """
    Create a new user.
    """
    try:
        return service.user.create(db, user)
    except Exception as e:
        logging.error(f"Error create user: {e}")
        raise HTTPException(status_code=400, detail=f"User with email already exists")


@router.post(
    "/login",
    response_model=models.Token,
    status_code=status.HTTP_200_OK,
)
async def login_user(
    request: Request,
    response: Response,
    user: models.UserLogin = Body(...),
    db: Session = Depends(get_db),
):
    """
    Login user.
    """
    try:
        return service.user.authenticate(db, user),
    except Exception as e:
        logging.error(f"Error login user: {e}")
        raise HTTPException(status_code=400, detail=f"Incorrect email or password")

