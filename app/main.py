
import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routes.health import router as health_router
from app.api.routes.query import router as query_router

from app.core.settings import settings
from app.core.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting up")

    yield

    logger.info("Application shutting down")


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(query_router)
