from contextlib import asynccontextmanager


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import db, service, routers


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
    _app.include_router(routers.metadata.router)
    _app.include_router(routers.sprint.router)

    return _app
