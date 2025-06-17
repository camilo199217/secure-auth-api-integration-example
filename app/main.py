from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.settings import get_settings
from app.services.db import engine
from secureauthapi import setup_secureauthapi

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(engine)
    # start_scheduler()
    yield


app = FastAPI(
    lifespan=lifespan,
)

setup_secureauthapi(app, settings.SECURE_AUTH_API, engine)
