from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import db, service, routers


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@asynccontextmanager
async def lifespan(_: FastAPI):

    db.BaseSqlModel.metadata.create_all(bind=db.engine)
    service.mailing.init_email_service()
    yield


def create_app() -> FastAPI:
    _app = FastAPI(lifespan=lifespan)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(routers.user.router)
    _app.include_router(routers.ticket.router)
    _app.include_router(routers.mailing.router)

    return _app


app = create_app()
