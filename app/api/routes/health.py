import logging

from fastapi import APIRouter
from app.core.settings import settings

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
def health() -> dict[str, str]:
    logger.info("Healthcheck requested")
    return {
            "status": "ok",
            "enviroment": settings.app_env,
            "debug": str(settings.app_debug)
           }