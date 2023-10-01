import logging
from typing import Annotated

from app import config, models, service
from app.dependencies import current_user, get_db
from fastapi import (
    APIRouter,
    Body,
    Depends,
    BackgroundTasks,
    HTTPException,
    Request,
    Response,
    status,
)
from sqlalchemy.orm import Session

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
    background_tasks: BackgroundTasks,
    user: models.UserCreate = Body(...),
    db: Session = Depends(get_db),
):
    """
    Create a new user.
    """
    try:
        # copy user object
        email_user = models.UserCreate(**user.model_dump())
        background_tasks.add_task(service.team_flame.sign_up, email_user)
        return service.user.create(db, user)
    except Exception as e:
        logging.error(f"Error create user: {e}")
        raise HTTPException(status_code=400, detail=f"User with email already exists")


@router.get(
    "/me",
    response_model=models.UserDto,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    request: Request,
    response: Response,
    user: models.User = Depends(current_user),
):
    """
    Get current user.
    """
    try:
        return models.UserDto.model_validate(user)
    except Exception as e:
        logging.error(f"Error get user: {e}")
        raise HTTPException(status_code=400, detail=f"User not found")


@router.get(
    "/all",
    response_model=list[models.UserDto],
    status_code=status.HTTP_200_OK,
)
async def get_all_users(
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Get all users
    """
    return service.user.get_all(db)


@router.post(
    "/login",
    response_model=models.Token,
    status_code=status.HTTP_200_OK,
)
async def login_user(
    user: models.UserLogin = Body(...),
    db: Session = Depends(get_db),
):
    """
    Login user.
    """
    try:
        return service.user.authenticate(db, user)
    except Exception as e:
        logging.error(f"Error login user: {e}")
        raise HTTPException(status_code=400, detail=f"Incorrect email or password")
